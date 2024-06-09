# Description: This script is used to wait for a service to be available before starting the application.
import socket
import time
import sys

def wait_for_service(host, port, timeout=30):
    start_time = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=1):
                print(f"{host}:{port} is available after {time.time() - start_time} seconds")
                return True
        except Exception as e:
            pass
        if time.time() - start_time > timeout:
            print(f"Timeout occurred after {timeout} seconds")
            return False
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        # Usage: python wait_for_db.py <host> <port>
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    if not wait_for_service(host, port):
        print(f"Failed to connect to {host}:{port}")
        sys.exit(1)
