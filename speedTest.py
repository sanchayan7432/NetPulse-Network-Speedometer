import streamlit as st
import speedtest
import requests
import psutil
import time
import statistics
#from ping3 import ping
import plotly.graph_objects as go
import subprocess
import re

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="NetPulse",
    page_icon="https://img.icons8.com/fluency/96/speed.png",
    layout="wide"
)

# ---------------- STYLE ---------------- #

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

h1, h2, h3 {
color:white;
text-align:center;
}

.metric-container {
background:#111;
padding:15px;
border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.title("NetPuls")

# ---------------- NETWORK INFO ---------------- #

@st.cache_data
def get_network_info():

    ip = requests.get("https://api.ipify.org").text
    data = requests.get("https://ipinfo.io/json").json()

    return {
        "ip": ip,
        "city": data.get("city"),
        "country": data.get("country"),
        "org": data.get("org")
    }

info = get_network_info()

st.markdown(
f"""
**ISP:** {info['org']}  
**Location:** {info['city']} {info['country']}  
**Public IP:** {info['ip']}
"""
)

# ---------------- WIFI SIGNAL ---------------- #

def get_wifi_strength():
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()

        signal = re.search(r"Signal\s*:\s*(\d+)%", output)
        if signal:
            return int(signal.group(1))
    except:
        return None

wifi_signal = get_wifi_strength()

if wifi_signal:
    st.progress(wifi_signal)
    st.write(f"📶 WiFi Signal Strength: **{wifi_signal}%**")

# ---------------- JITTER ---------------- #

#def measure_jitter():

    #samples = []

    #for _ in range(6):
        #delay = ping("8.8.8.8")
        #if delay:
            #samples.append(delay*1000)

    #if len(samples) > 1:
        #return round(statistics.stdev(samples),2)

    #return 0

# ---------------- PACKET LOSS ---------------- #

def packet_loss():

    lost = 0
    total = 6

    for _ in range(total):
        if ping("8.8.8.8") is None:
            lost += 1

    return round((lost/total)*100,2)

# ---------------- SPEED GAUGE ---------------- #

def gauge(value, title):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range':[0,200]},
            'bar':{'color':"#00FF9C"},
            'steps':[
                {'range':[0,60],'color':"#ff4d4d"},
                {'range':[60,120],'color':"#ffd166"},
                {'range':[120,200],'color':"#06d6a0"}
            ]
        }
    ))

    fig.update_layout(height=300)

    return fig

# ---------------- REALTIME GRAPH ---------------- #

graph_placeholder = st.empty()

def live_bandwidth_graph():

    download_data=[]
    upload_data=[]

    start = psutil.net_io_counters()

    for i in range(10):

        time.sleep(1)

        now = psutil.net_io_counters()

        down = (now.bytes_recv-start.bytes_recv)/1_000_000
        up = (now.bytes_sent-start.bytes_sent)/1_000_000

        download_data.append(down)
        upload_data.append(up)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            y=download_data,
            mode="lines+markers",
            name="Download Mbps"
        ))

        fig.add_trace(go.Scatter(
            y=upload_data,
            mode="lines+markers",
            name="Upload Mbps"
        ))

        fig.update_layout(
            title="Live Bandwidth Usage",
            xaxis_title="Seconds",
            yaxis_title="MB transferred"
        )

        graph_placeholder.plotly_chart(fig,use_container_width=True)

# ---------------- SPEED TEST ---------------- #

def run_speedtest():

    stt = speedtest.Speedtest()

    stt.get_servers()
    stt.get_best_server()

    download = stt.download()/1_000_000
    upload = stt.upload()/1_000_000
    ping_val = stt.results.ping

    return round(download,2),round(upload,2),round(ping_val,2)

# ---------------- BUTTON ---------------- #

if st.button("🚀 Run Speed Test"):

    st.subheader("Running Test...")

    live_bandwidth_graph()

    with st.spinner("Measuring speed..."):

        download,upload,ping_val = run_speedtest()

        #jitter = measure_jitter()

        loss = packet_loss()

    col1,col2 = st.columns(2)

    with col1:
        st.plotly_chart(gauge(download,"Download Mbps"),use_container_width=True)

    with col2:
        st.plotly_chart(gauge(upload,"Upload Mbps"),use_container_width=True)

    col3,col4,col5 = st.columns(3)

    col3.metric("Ping",f"{ping_val} ms")
    col4.metric("Jitter",f"{jitter} ms")
    col5.metric("Packet Loss",f"{loss}%")

    st.success("Speed test completed successfully!")

# ---------------- REFRESH ---------------- #

if st.button("🔄 Restart Test"):

    st.rerun()


