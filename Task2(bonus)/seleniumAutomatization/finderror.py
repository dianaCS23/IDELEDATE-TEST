from selenium import webdriver 
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
import time 
import os 

# https://docs.google.com/document/d/1cPCq4K05iMIoekG7kujPauO3qLHy6day/edit?usp=sharing&ouid=116061247327698525967&rtpof=true&sd=true

# Path to the ChromeDriver
dirname = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(dirname, "..", "chromedriver.exe")
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Load the example page
    driver.get("https://buggy.justtestit.org/make/ckl2phsabijs71623vk0")
    
    # Wait for the link with the class 'navbar-brand' to be present
    try:
        logo_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "navbar-brand"))
        )
        
        # Click on the logo link
        logo_link.click()
        time.sleep(2)  # Wait for the page to load
        
        # Check if the URL is the homepage after the click
        if driver.current_url == "https://buggy.justtestit.org/":
            print("The logo correctly redirects to the homepage.")
        else:
            print(f"Error: The logo does not redirect correctly. Current URL: {driver.current_url}")
    
    except Exception as e:
        print("Error: Could not find the logo link in the navbar.")
        print(str(e))

finally:
    driver.quit()  # Close the browser and end the WebDriver session
