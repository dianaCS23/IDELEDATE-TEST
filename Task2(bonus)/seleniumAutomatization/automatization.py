import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

# Path to the ChromeDriverr

dirname = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(dirname, "..", "chromedriver.exe")
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# List to store results
results = []

try:
    # Open the registration page
    driver.get("https://buggy.justtestit.org/register")
    time.sleep(2)  # Wait for the page to load

    # Check that the fields exist
    try:
        username_field = driver.find_element(By.ID, "username")
        first_name_field = driver.find_element(By.ID, "firstName")
        last_name_field = driver.find_element(By.ID, "lastName")
        password_field = driver.find_element(By.ID, "password")
        confirm_password_field = driver.find_element(By.ID, "confirmPassword")
        results.append("All required fields are present.")
    except NoSuchElementException as e:
        results.append(f"Error: One of the fields was not found. Details: {e}")
        driver.quit()
        exit()

    # Data to be filled in automatically
    # TODO: Traer estos valores de variables de entorno
    username = "testuser"
    first_name = "John"
    last_name = "Doe"
    password = "Password123!"
    confirm_password = "Password123!"

    # Fill in the form fields
    username_field.send_keys(username)
    first_name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)
    password_field.send_keys(password)
    confirm_password_field.send_keys(confirm_password)

    # Submit the form
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)  # Wait for the registration to process

    # Check for the successful registration message
    try:
        success_message = driver.find_element(By.XPATH, "//div[contains(text(), 'registration is successful')]")
        if success_message:
            results.append("Registration completed successfully.")
    except NoSuchElementException:
        results.append("Error: Successful registration message not found.")

finally:
    # Close the browser
    driver.quit()

# Generate the HTML file with the results
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verification Results</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            color: #333;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            background: #f4f4f4;
            margin: 5px 0;
            padding: 10px;
            border-left: 5px solid green;
        }}
        li.error {{
            border-left-color: red;
        }}
    </style>
</head>
<body>
    <h1>Verification Results</h1>
    <ul>
"""

# Add results to the HTML
for result in results:
    if "Error" in result:
        html_content += f'<li class="error">{result}</li>'
    else:
        html_content += f'<li>{result}</li>'

html_content += """
    </ul>
</body>
</html>
"""

# Save the HTML to a file
with open("verification_results.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Results saved in 'verification_results.html'.")
