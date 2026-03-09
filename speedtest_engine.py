import speedtest

class SpeedTestEngine:

    def run_test(self):

        st = speedtest.Speedtest()

        # get server list
        st.get_servers()

        # choose best server
        st.get_best_server()

        # run tests
        download = st.download()
        upload = st.upload()

        ping = st.results.ping

        return {
            "download": round(download / 1_000_000, 2),
            "upload": round(upload / 1_000_000, 2),
            "ping": round(ping, 2),
            "server": st.results.server["name"]
        }