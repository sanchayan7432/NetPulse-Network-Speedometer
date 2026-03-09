import streamlit as st
import speedtest
import plotly.graph_objects as go
import time
import random

st.set_page_config(
    page_title="NetPulse",
    page_icon="https://img.icons8.com/fluency/96/speed.png",
    layout="centered"
)

# ---------- DARK BACKGROUND ----------
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

div.stButton > button{
background-color:#111827;
color:white;
border-radius:10px;
padding:10px 20px;
font-size:16px;
border:1px solid #374151;
}

div.stButton > button:hover{
background:#1f2937;
}
</style>
""", unsafe_allow_html=True)


# ---------- SPEEDOMETER FUNCTION ----------
def speedometer(value):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={'suffix': " Mb/s"},
        gauge={
            'axis': {'range': [0, 150]},
            'bar': {'color': "#7c83fd"},
            'steps': [
                {'range': [0, 50], 'color': "#1f2937"},
                {'range': [50, 100], 'color': "#374151"},
                {'range': [100, 150], 'color': "#4b5563"}
            ],
        }
    ))

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font={'color': "white", 'size': 28}
    )

    return fig


# ---------- TITLE ----------
st.title("⚡ NETPULSE")
st.write("Real-time Internet Speed Meter")


# ---------- PLACEHOLDERS ----------
gauge_placeholder = st.empty()

col1, col2, col3 = st.columns(3)

ping_box = col1.empty()
download_box = col2.empty()
upload_box = col3.empty()

ping_box.metric("Ping", "-- ms")
download_box.metric("Download", "-- Mb/s")
upload_box.metric("Upload", "-- Mb/s")


# ---------- START TEST ----------
if st.button("🚀 Start Speed Test"):

    s = speedtest.Speedtest()

    # ---------- DOWNLOAD PHASE ----------
    st.write("⬇ Testing Download Speed")

    for i in range(25):
        val = random.uniform(1, 80)
        gauge_placeholder.plotly_chart(
            speedometer(val),
            use_container_width=True,
            key=f"download_sim_{i}"
        )
        time.sleep(0.08)

    s.get_best_server()

    download_speed = s.download() / 1_000_000

    for i in range(30):
        value = download_speed * (i / 30)
        gauge_placeholder.plotly_chart(
            speedometer(value),
            use_container_width=True,
            key=f"download_real_{i}"
        )
        time.sleep(0.03)

    download_box.metric("Download", f"{download_speed:.2f} Mb/s")


    # ---------- UPLOAD PHASE ----------
    st.write("⬆ Testing Upload Speed")

    for i in range(25):
        val = random.uniform(1, 50)
        gauge_placeholder.plotly_chart(
            speedometer(val),
            use_container_width=True,
            key=f"upload_sim_{i}"
        )
        time.sleep(0.08)

    upload_speed = s.upload() / 1_000_000

    for i in range(30):
        value = upload_speed * (i / 30)
        gauge_placeholder.plotly_chart(
            speedometer(value),
            use_container_width=True,
            key=f"upload_real_{i}"
        )
        time.sleep(0.03)

    upload_box.metric("Upload", f"{upload_speed:.2f} Mb/s")


    # ---------- PING ----------
    ping = s.results.ping
    ping_box.metric("Ping", f"{ping:.2f} ms")

    st.success("✅ Speed Test Completed")


# ---------- RESTART ----------
if st.button("🔄 Restart Test"):
    st.rerun()