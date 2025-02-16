# **LibB: Library Seat Reservation System**

## 📌 Overview
LibB is a smart **library seat reservation system** that allows students to book seats in advance, ensuring **efficient space utilization** and reducing manual effort. The system integrates **real-time seat availability indicators** using IoT sensors and provides a **user-friendly web interface** for seamless booking and management.

---

## 🚀 Features
✅ **Real-Time Seat Monitoring**: IoT-enabled seat status indicators using ESP8266 microcontrollers.  
✅ **Online Seat Reservation**: Users can book library seats through an intuitive web interface.  
✅ **Automated Seat Availability Updates**: Real-time seat occupancy detection.  
✅ **User Notifications**: Alerts for booking confirmations, reminders, and availability updates.  
✅ **Booking Management**: Modify or cancel reservations easily.  
✅ **Analytics & Reporting**: Provides data insights on seat utilization and user behavior.  

---

## 🏗 System Architecture
The system consists of three main components:

1. **Backend**: Built using **Node.js** and **Express.js** for handling seat reservations and user interactions.
2. **Frontend**: Web interface developed with **HTML, CSS, and JavaScript** for easy user access.
3. **IoT Integration**: **ESP8266 microcontrollers** with **LED indicators** to display real-time seat availability.

---

## 🛠 Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Node.js, Express.js
- **Database**: JSON-based storage for seat reservations
- **IoT Devices**: ESP8266 microcontrollers for real-time seat monitoring
- **Networking**: HTTP GET requests for communication between the server and IoT devices

---

## 📥 Installation & Setup
### 🔧 Prerequisites
- **Node.js** and **npm** installed
- **ESP8266 microcontrollers** with Arduino IDE setup
- **WiFi network** for IoT communication

### ⚡ Steps to Run the Project
#### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/LibB.git
cd LibB
```
#### 2️⃣ **Install Dependencies**
```bash
npm install
```
#### 3️⃣ **Start the Backend Server**
```bash
node server.js
```
#### 4️⃣ **Run the Web Application**
Open `index.html` in a browser.

#### 5️⃣ **Deploy IoT Devices**
- Flash the ESP8266 code onto the microcontrollers.
- Ensure the devices are connected to the same network as the server.

---

## 🎯 Usage
🔹 **User Login & Signup**: Users can create an account or log in to reserve seats.  
🔹 **Reserve a Seat**: Users can check available seats and book them for a specific time slot.  
🔹 **Modify Bookings**: Users can update or cancel their reservations.  
🔹 **Real-Time Status**: Seat availability is displayed via LED indicators controlled by ESP8266.  

---

## 🎨 Introduction to the User Interface

### 🔐 Login Page
**Description:**
- Allows registered users to log in with their credentials.
- Fields: Registration Number, Password.
- Features: "Remember Me" checkbox and Sign-Up redirection.

📌 *<img width="260" alt="image" src="https://github.com/user-attachments/assets/12882b11-8038-46a7-bda2-f9ae0c13ab93" />
*

### 📝 Signup Page
**Description:**
- New users can register with their name, registration number, school details, and password.
- Ensures data validation before account creation.

📌 <img width="400" alt="image" src="https://github.com/user-attachments/assets/14d49317-c74c-4cd2-8f7d-ba5016e7bb76" />


### 🏠 Home Page
**Description:**
- Displays key features and navigation options.
- Provides buttons to book, modify reservations, and view system insights.

📌 <img width="400" alt="image" src="https://github.com/user-attachments/assets/ec295c48-8c31-4c15-b3af-707106fe4c9c" />


### 📅 Reservation Page
**Description:**
- Shows an interactive library layout for seat selection.
- Users can select desks, input date/time, and confirm their bookings.

📌 <img width="400" alt="image" src="https://github.com/user-attachments/assets/2bc93e28-4148-4e90-ba11-5d15bad79446" />


### 🔄 Modify Bookings Page
**Description:**
- Users can view, update, or cancel existing bookings.
- Provides an option to delete individual bookings or clear all reservations.

📌 <img width="400" alt="image" src="https://github.com/user-attachments/assets/24af809f-9127-49db-a2d5-21a50a5390eb" />


---

## 🌟 Future Enhancements
🔮 **Mobile App Integration** for easier access.  
🔮 **AI-based Prediction** to suggest optimal seating times.  
🔮 **Multi-Campus Support** to manage reservations across multiple libraries.  

---

## 👨‍💻 Contributors
- **Anurag Kumar Kanojiya** (21BRS1155) – Developer & Researcher
- **Dr. Suganya R** – Project Supervisor

---

## 📜 License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📩 Contact
📧 **Email**: ak909412@gmail.com 

---

🚀 *Contributions and feedback are welcome!* 🎉

