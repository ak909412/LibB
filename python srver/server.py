import requests
import json
import time
from datetime import datetime, timedelta
import pytz

def get_org_pool_config(api_url):
   #function to fetch BackEnd Data

# Get data from the first API call
api_data = get_org_pool_config(get_api_url)

# Desk management code
current_date = datetime.now().date()
two_days_before = current_date - timedelta(days=2)
two_days_after = current_date + timedelta(days=2)
bookings_date_from = f"{two_days_before.isoformat()}T00:00:00.000Z"
bookings_date_to = f"{two_days_after.isoformat()}T23:59:00.000Z"
api_url = f'https://digiindia.veris.in/api/v4/organization/32/resources/list/?page_size=200&location=3570&bookings_date_from={bookings_date_from}&bookings_date_to={bookings_date_to}'

actions = {
    "Desk 1": '1',
    "Desk 2": '2',
    
}

def fetch_desk_data(api_url):
    try:
        headers = {
            'authorization': f'token {token_value}',
        }
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from the API. Status code: {response.status_code}")
            print(f"Response content: {response.content}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {str(e)}")
        return None

def is_desk_active(desk):
    return desk and desk.get("availability_status", {}).get("is_active", False)

def is_scheduled(desk):
    if not desk or not desk.get("bookings_all"):
        return False
    return any(booking.get("status", "").lower() == "scheduled" for booking in desk["bookings_all"])

def is_today(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").date()
    current_date = datetime.now().date()
    return date_obj == current_date

def is_desk_inuse_today(desk):
    if not desk or not desk.get("bookings_all"):
        return False
    bookings = desk.get("bookings_all", [])
    if not bookings:
        return False
    first_booking = bookings[0]
    in_time_str = first_booking.get("valid_from", "")
    out_time_str = first_booking.get("valid_till", "")
    if is_today(in_time_str) and is_today(out_time_str):
        in_time = datetime.strptime(in_time_str, "%Y-%m-%dT%H:%M:%SZ").time()
        out_time = datetime.strptime(out_time_str, "%Y-%m-%dT%H:%M:%SZ").time()
        in_time_plus_5_hours = (datetime.combine(datetime.min, in_time) + timedelta(hours=5.5)).time()
        out_time_plus_5_hours = (datetime.combine(datetime.min, out_time) + timedelta(hours=5.5)).time()
        current_time = datetime.now().time()
        return in_time_plus_5_hours <= current_time <= out_time_plus_5_hours
    return False

def is_within_time_limit(out_time_str, time_limit_minutes=5):
    datetime_format = "%Y-%m-%dT%H:%M:%SZ"
    out_time_utc = datetime.strptime(out_time_str, datetime_format)
    ist = pytz.timezone('Asia/Kolkata')
    out_time_ist = out_time_utc.replace(tzinfo=pytz.utc).astimezone(ist)
    current_time_ist = datetime.now(ist)
    time_difference = out_time_ist - current_time_ist
    return time_difference.total_seconds() <= time_limit_minutes * 60

def generate_signals(desk_data):
    signals = []
    if not isinstance(desk_data, dict):
        print("Invalid data format - not a dictionary")
        return signals
    results = desk_data.get("results", [])
    for desk in results:
        desk_name = desk.get("name")
        if desk_name in esp_addresses and is_desk_active(desk):
            print(f"Desk {desk_name} is active")
            if is_scheduled(desk):
                bookings_all = desk.get("bookings_all", [])
                if bookings_all:
                    if is_desk_inuse_today(desk):
                        if is_within_time_limit(bookings_all[0].get("valid_till", ""), time_limit_minutes=5):
                            action = "2"  # Desk is about to be available
                            print(f"{desk_name} is about to be Available")
                        else:
                            action = "1"  # Desk is not available
                            print(f"{desk_name} is Not Available")
                    else:
                        action = "0"  # Desk is available
                        print(f"{desk_name} is Available")
                signals.append((desk_name, action))
            else:
                action = {action}  # Desk is available
                print(f"{desk_name} is Available")
                signals.append((desk_name, action))
        else:
            action = "00"  # Set the default action for inactive desks
    return signals

def send_actions_to_esp(actions, esp_addresses):
    for desk_id, action in actions:
        if desk_id in esp_addresses:
            esp_ip = esp_addresses[desk_id]
            try:
                payload = {"action": action}
                headers = {"Content-type": "application/json"}
                response = requests.post(f"http://192.168.1.128:80/api/receive_signal", json=payload, headers=headers)
                if response.status_code == 200:
                    print(f"Action {action} sent to ESP {desk_id} at IP: {esp_ip}")
                else:
                    print(f"Failed to send action to ESP {desk_id} at IP: {esp_ip}")
                    print(f"Response status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error sending action to ESP {desk_id} at IP {esp_ip}: {str(e)}")
            finally:
                continue

def main():
    while True:
        desk_data = fetch_desk_data(api_url)
        if desk_data:
            print("Desk data fetched successfully.")
            actions = generate_signals(desk_data)
            print("Generated signals:")
            print(actions)
            send_actions_to_esp(actions, esp_addresses)
        else:
            print("No desk data found from the API.")
        time.sleep(5)

if __name__ == "__main__":
    main()
s
