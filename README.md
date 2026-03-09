# ⚡ NetPulse Internet Speed Meter

NetPulse is a modern **Internet Speed Testing Dashboard** built with
**Python and Streamlit**.\
It provides real-time **download and upload speed measurement** with a
**live animated speedometer meter** similar to professional tools.

------------------------------------------------------------------------

# 🚀 Features

-   📡 **Real Internet Speed Testing**
-   ⚡ **Live Speedometer Gauge (Download + Upload)**
-   🔄 **Refresh Button to Restart Test**
-   🌙 **Dark Themed Modern UI**
-   📊 **Real-time Speed Updates**
-   📶 **Server Detection**
-   📍 **Latency Measurement**
-   🖥️ **Clean Streamlit Dashboard**
-   📟 **Professional Meter Interface**

------------------------------------------------------------------------

# 🖼️ Preview

The dashboard shows:

-   Live **Speedometer Meter**
-   **Download Speed**
-   **Upload Speed**
-   **Ping / Latency**
-   **Server Location**
-   **Refresh Button**

The UI design is inspired by modern internet testing dashboards.

------------------------------------------------------------------------

# 🧠 Technologies Used

  Technology      Purpose
  --------------- -------------------------------
  Python          Core Programming
  Streamlit       Web Dashboard
  Speedtest-cli   Internet Speed Measurement
  Plotly          Interactive Speedometer Gauge
  HTML/CSS        UI Styling

------------------------------------------------------------------------

# 📦 Project Structure

    netpulse_speedometer/
    │
    ├── speedMeter.py        # Live speedometer Streamlit app
    ├── speedTest.py         # Advanced UI speed test dashboard
    ├── gui.py               # Desktop GUI version
    ├── netpulse_meter_icon.ico
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# ⚙️ Installation

## 1️⃣ Clone the Repository

    git clone https://github.com/yourusername/netpulse-speed-meter.git
    cd netpulse-speed-meter

------------------------------------------------------------------------

## 2️⃣ Create Virtual Environment

    python -m venv venv

Activate it:

### Windows

    venv\Scripts\activate

### Linux / Mac

    source venv/bin/activate

------------------------------------------------------------------------

## 3️⃣ Install Dependencies

    pip install streamlit speedtest-cli plotly

or

    pip install -r requirements.txt

------------------------------------------------------------------------

# ▶️ Running the App

Run the Streamlit dashboard:

    streamlit run speedMeter.py

or

    streamlit run speedTest.py

The app will open automatically in your browser.

------------------------------------------------------------------------

# 📊 How It Works

1.  The app uses **speedtest-cli** to detect the best available server.
2.  It measures **download bandwidth**.
3.  It measures **upload bandwidth**.
4.  Results are displayed on a **live speedometer gauge**.
5.  Streamlit updates the UI dynamically.

------------------------------------------------------------------------

# 📟 Speedometer Meter

The dashboard includes a **live animated gauge meter** showing:

-   0 → 200 Mbps range
-   Color zones for speed ranges
-   Needle animation during testing

This makes the UI similar to modern speed testing tools.

------------------------------------------------------------------------

# 🔄 Restart Speed Test

Click the **Refresh Button** to run the test again.

This will:

-   Reset the meter
-   Recalculate server
-   Run download test
-   Run upload test

------------------------------------------------------------------------

# 🌙 Dark Mode Interface

The application includes a custom **dark theme interface** with:

-   Gradient background
-   Card layout
-   Centered meter display
-   Responsive design

------------------------------------------------------------------------

# 📌 Requirements

Minimum requirements:

-   Python **3.9+**
-   Internet connection
-   Modern browser

Recommended:

-   Python **3.11+**
-   Stable broadband connection

------------------------------------------------------------------------

# 🛠️ Future Improvements

Planned upgrades:

-   🌍 Global server selection
-   📊 Historical speed tracking
-   🧠 AI network analysis
-   📈 Speed history charts
-   📱 Mobile responsive UI
-   ☁️ Cloud deployment
-   🧩 Plugin system

------------------------------------------------------------------------

# 🌐 Deployment

You can deploy this project using:

-   Streamlit Cloud
-   Docker
-   VPS Server
-   Local Network Monitoring

Example:

    streamlit run speedMeter.py --server.port 8501

------------------------------------------------------------------------

# 🤝 Contributing

Contributions are welcome!

Steps:

1.  Fork the repository
2.  Create a new branch
3.  Commit changes
4.  Submit a pull request

------------------------------------------------------------------------

# 🧪 Testing

Test the backend speed test module:

    python
    >>> import speedtest
    >>> st = speedtest.Speedtest()
    >>> st.get_best_server()
    >>> st.download()
    >>> st.upload()

------------------------------------------------------------------------

# 📜 License

This project is licensed under the **MIT License**.

You are free to:

-   Use
-   Modify
-   Distribute

------------------------------------------------------------------------

# 👨‍💻 Author

Developed for learning and experimentation with:

-   Python networking tools
-   Streamlit dashboards
-   Real-time UI components

------------------------------------------------------------------------

# ⭐ Support

If you like this project:

⭐ Star the repository\
🐛 Report issues\
💡 Suggest new features

------------------------------------------------------------------------

# ⚡ NetPulse

**Measure your internet speed with style.**
