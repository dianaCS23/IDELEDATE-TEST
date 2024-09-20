import time  
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.service import Service  
import os

# Path to the ChromeDriver
dirname = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(dirname, "..", "chromedriver.exe")
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    start_time = time.time()  # Record the start time
    
    driver.get("https://buggy.justtestit.org/register")  # Open the registration page
    load_time = time.time() - start_time  # Calculate the loading time
    
    # Check if the loading time is within the expected limit
    if load_time < 5:
        print(f"The page loaded in {load_time:.2f} seconds. (Within expected time)")
    else:
        print(f"The page took too long to load: {load_time:.2f} seconds.")
    
finally:
    driver.quit()  # Close the browser and end the WebDriver session
