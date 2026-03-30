🚗 AI Traffic Intelligence System
Smart Vehicle Detection, Analytics & Number Plate Recognition
📌 Overview

The AI Traffic Intelligence System is a smart application that analyzes traffic videos using Artificial Intelligence to:

Detect vehicles in real-time
Count total vehicles passing through a road
Categorize them into types (car, bus, truck, bike)
Extract vehicle number plates
Display all results in an interactive dashboard

👉 In simple words:
You upload a traffic video, and the system automatically tells you what’s happening on the road.

🎯 Problem It Solves

Managing traffic manually is:

Time-consuming
Error-prone
Not scalable

This system automates traffic analysis using AI, making it useful for:

Smart city monitoring
Traffic management systems
Security & surveillance
Data-driven decision making
⚙️ Features
🚘 1. Real-Time Vehicle Detection
Detects vehicles from video frames
Works on multiple vehicle types
📊 2. Vehicle Analytics Dashboard
Total vehicle count
Category-wise breakdown:
Cars
Buses
Trucks
Bikes
📈 3. Visual Insights
Bar chart showing vehicle distribution
Clean and modern dashboard UI
🔢 4. Number Plate Recognition
Extracts text from vehicles using OCR
Displays detected number plates
📜 5. History Tracking
Stores previously uploaded videos
Shows upload time and file name
🎨 6. Modern UI
Black + Yellow themed dashboard
Clean and visually engaging layout
🧠 How It Works (Simple Explanation)
You upload a video
The system processes it frame-by-frame
AI model detects vehicles
Each detected vehicle is classified
A counter keeps track of totals
OCR extracts text (number plates)
Results are shown in a dashboard
🏗️ Project Structure
vehicle-detect/
│
├── app.py                 # Main dashboard UI (Streamlit)
├── models/
│   └── best.pt           # Trained AI model
│
├── utils/
│   ├── video_utils.py    # Video processing + detection logic
│   └── storage.py        # History storage logic
│
├── assets/
│   └── styles.css        # Custom UI styling
│
└── history.json          # Stores uploaded video history
🛠️ Tech Stack
🧠 AI & Backend
Python
YOLOv8 (Object Detection)
OpenCV (Video Processing)
EasyOCR (Text Recognition)
🌐 Frontend
Streamlit (Dashboard UI)
Custom CSS
🚀 Installation & Setup
1️⃣ Clone the Repository
git clone <your-repo-link>
cd vehicle-detect
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install ultralytics opencv-python streamlit easyocr
4️⃣ Run the Application
streamlit run app.py
▶️ How to Use
Open the app in browser
Go to Upload & Detect
Upload a traffic video
Watch real-time detection
View:
Vehicle counts
Charts
Number plates
📊 Output Example

After processing, you’ll see:

🚗 Cars: XX
🚌 Buses: XX
🚚 Trucks: XX
🏍 Bikes: XX
🚘 Total Vehicles: XX

📈 Plus a chart showing distribution
🔢 Plus detected number plates

⚠️ Limitations
Vehicle count may include duplicates (same vehicle across frames)
OCR may not always detect plates accurately
Number plates are extracted from vehicle region (not a dedicated plate detector)
🔮 Future Improvements
🚀 Vehicle tracking (avoid duplicate counting)
🎯 Dedicated number plate detection model
📄 Export report (PDF/CSV)
🌐 Cloud deployment
🔐 User authentication system
💡 Use Cases
Smart traffic monitoring
Highway analytics
Security surveillance
Urban planning
AI-based research projects
🙌 Conclusion

This project demonstrates how AI can be used to:

Automate real-world problems
Extract meaningful insights from videos
Build intelligent dashboards

👉 It combines computer vision + UI + real-world application, making it a strong end-to-end system.