import requests
import schedule
import time

# URL of the server
url = "https://free-btc-price-predict.onrender.com/"

# Function to send the request
def keep_alive():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Server responded with status code {response.status_code}. Server is alive.")
        else:
            print(f"Received unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while sending request: {e}")

# Schedule the job to run every hour
schedule.every(1).hour.do(keep_alive)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
