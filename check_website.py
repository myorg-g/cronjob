import requests
import logging
from datetime import datetime

# Configuration
URL = "http://google.com"  # Replace with your URL
LOGFILE = "/app/logfile.log"  # Log file path inside the Docker container

# Setup logging
logging.basicConfig(filename=LOGFILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Website {url} is up.")
        else:
            logging.error(f"Website {url} is down. HTTP status code: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Website {url} is down. Exception: {e}")

if __name__ == "__main__":
    check_website(URL)
