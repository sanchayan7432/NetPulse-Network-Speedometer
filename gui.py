import tkinter as tk
from threading import Thread

from speedtest_engine import SpeedTestEngine
from network_info import get_network_details
from jitter_packetloss import measure_jitter, packet_loss
from database import save_result, init_db


class NetPulseGUI:

    def __init__(self):

        init_db()

        self.root = tk.Tk()
        self.root.title("NetPulse Speed Test")
        self.root.geometry("650x500")
        self.root.configure(bg="#0b0b0b")

        title = tk.Label(
            self.root,
            text="NetPulse Network Analyzer",
            font=("Segoe UI", 22, "bold"),
            fg="white",
            bg="#0b0b0b"
        )
        title.pack(pady=20)

        self.download = tk.Label(
            self.root,
            text="Download: -- Mbps",
            font=("Segoe UI", 18),
            fg="#00FF9C",
            bg="#0b0b0b"
        )
        self.download.pack(pady=8)

        self.upload = tk.Label(
            self.root,
            text="Upload: -- Mbps",
            font=("Segoe UI", 18),
            fg="#00C8FF",
            bg="#0b0b0b"
        )
        self.upload.pack(pady=8)

        self.ping = tk.Label(
            self.root,
            text="Ping: -- ms",
            font=("Segoe UI", 18),
            fg="#FFD166",
            bg="#0b0b0b"
        )
        self.ping.pack(pady=8)

        self.jitter = tk.Label(
            self.root,
            text="Jitter: -- ms",
            font=("Segoe UI", 18),
            fg="#FF9F1C",
            bg="#0b0b0b"
        )
        self.jitter.pack(pady=8)

        self.loss = tk.Label(
            self.root,
            text="Packet Loss: -- %",
            font=("Segoe UI", 18),
            fg="#FF4D4D",
            bg="#0b0b0b"
        )
        self.loss.pack(pady=8)

        # Network info
        info = get_network_details()

        self.network = tk.Label(
            self.root,
            text=f"{info['org']} | {info['city']} {info['country']} | IP: {info['ip']}",
            font=("Segoe UI", 12),
            fg="#BBBBBB",
            bg="#0b0b0b"
        )
        self.network.pack(pady=20)

        self.status = tk.Label(
            self.root,
            text="Ready",
            font=("Segoe UI", 11),
            fg="#888888",
            bg="#0b0b0b"
        )
        self.status.pack(pady=10)

        self.button = tk.Button(
            self.root,
            text="Run Test",
            font=("Segoe UI", 12, "bold"),
            bg="#1F6FEB",
            fg="white",
            width=15,
            command=self.start_test
        )

        self.button.pack(pady=20)

    def start_test(self):

        self.status.config(text="Running speed test...")

        self.download.config(text="Download: Testing...")
        self.upload.config(text="Upload: Testing...")
        self.ping.config(text="Ping: Testing...")
        self.jitter.config(text="Jitter: Testing...")
        self.loss.config(text="Packet Loss: Testing...")

        self.button.config(state="disabled")

        Thread(target=self.run_test).start()

    def run_test(self):

        try:

            engine = SpeedTestEngine()
            result = engine.run_test()

            jitter = measure_jitter()
            loss = packet_loss()

            self.root.after(
                0,
                lambda: self.update_ui(result, jitter, loss)
            )

        except Exception as e:

            self.root.after(
                0,
                lambda: self.status.config(text=f"Error: {e}")
            )

    def update_ui(self, result, jitter, loss):

        self.download.config(text=f"Download: {result['download']} Mbps")
        self.upload.config(text=f"Upload: {result['upload']} Mbps")
        self.ping.config(text=f"Ping: {result['ping']} ms")
        self.jitter.config(text=f"Jitter: {jitter} ms")
        self.loss.config(text=f"Packet Loss: {loss} %")

        self.status.config(text=f"Server: {result['server']}")

        save_result(
            result['download'],
            result['upload'],
            result['ping'],
            jitter,
            loss
        )

        self.button.config(state="normal")

    def run(self):
        self.root.mainloop()