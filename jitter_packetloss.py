from ping3 import ping
import statistics

def measure_jitter(host="8.8.8.8", count=10):

    pings = []

    for _ in range(count):
        delay = ping(host)
        if delay:
            pings.append(delay*1000)

    if len(pings) > 1:
        jitter = statistics.stdev(pings)
    else:
        jitter = 0

    return round(jitter,2)


def packet_loss(host="8.8.8.8", count=10):

    lost = 0

    for _ in range(count):
        if ping(host) is None:
            lost += 1

    return round((lost/count)*100,2)