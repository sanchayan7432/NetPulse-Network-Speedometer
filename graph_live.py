import matplotlib.pyplot as plt

class LiveGraph:

    def __init__(self):
        self.d = []
        self.u = []

    def update(self, download, upload):

        self.d.append(download)
        self.u.append(upload)

        plt.clf()

        plt.plot(self.d,label="Download Mbps")
        plt.plot(self.u,label="Upload Mbps")

        plt.xlabel("Time")
        plt.ylabel("Speed")
        plt.legend()

        plt.pause(0.01)