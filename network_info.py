import requests
import socket

def get_network_details():

    ip = requests.get("https://api.ipify.org").text
    data = requests.get("https://ipinfo.io/json").json()

    return {
        "ip": ip,
        "city": data.get("city"),
        "country": data.get("country"),
        "org": data.get("org"),
        "hostname": socket.gethostname()
    }