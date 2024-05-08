import time
import requests


connected = False
connected_status = "Disconnected"


def check_network_connection_status(url="https://um.ac.ir", timeout=5):
    global connected
    global connected_status
    try:
        requests.get(url=url, timeout=timeout)
        connected = True
        connected_status = "Connected"
    except (requests.ConnectionError, requests.Timeout):
        connected = False
        connected_status = "Disconnected"

def run_check_network_connection_status(url="https://um.ac.ir", timeout=5, seconds=5):
    while True:
        check_network_connection_status(url=url, timeout=timeout)
        time.sleep(seconds)