import time
from datetime import datetime
import requests

# Function to parse the CSV file and get desk data
def parse_desk_data(file_path):
    desk_data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("id"):  # Skip the header line if present
                parts = line.split(', ')
                data = {
                    'id': parts[0],
                    'floor': int(parts[1]),
                    'desk_number': int(parts[2]),
                    'date': parts[3],
                    'time_in': datetime.strptime(parts[4], '%H:%M').time(),
                    'time_out': datetime.strptime(parts[5], '%H:%M').time(),
                }
                desk_data.append(data)
    return desk_data

# Function to check if the current time is within the time range
def is_desk_occupied(time_in, time_out):
    current_time = datetime.now().time()
    return time_in <= current_time <= time_out

# Function to send signals to the ESP8266
def send_signal_to_esp(desk_number, status, ip_address):
    signal = f"{desk_number}{status}"
    print(f"Prepared signal: {signal}")
    try:
        url = f"http://{ip_address}/send_signal"
        requests.get(url, params={'signal': signal})
        print(f"Signal sent: {signal}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending signal: {e}")

# Main function
def monitor_desks(file_path, ip_address):
    while True:
        desk_data = parse_desk_data(file_path)
        total_desks = 6  # Number of desks to monitor

        for desk_number in range(1, total_desks + 1):
            # Check if the desk number is present in the data
            desk_info = next(
                (d for d in desk_data if d['desk_number'] == desk_number), None)
            if desk_info:
                # If desk number is present, check if it is currently occupied
                if is_desk_occupied(desk_info['time_in'], desk_info['time_out']):
                    send_signal_to_esp(desk_number, 1, ip_address)
                else:
                    send_signal_to_esp(desk_number, 0, ip_address)
            else:
                # Desk number is not in data, send default signal
                send_signal_to_esp(desk_number, 0, ip_address)

            time.sleep(0.5)  # Interval between each signal

        time.sleep(3)  # Repeat after 3 seconds

# Usage
# Path to your CSV file
file_path = r'X:\Desktop\SeatHub_Html\Screens\Booking\bookings.txt'
ip_address = '192.168.124.153'  # Replace with your ESP8266's IP address
monitor_desks(file_path, ip_address)
