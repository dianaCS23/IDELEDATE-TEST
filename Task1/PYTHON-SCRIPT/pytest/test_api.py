import requests
import pytest

# Base URL for the API
BASE_URL = "http://localhost:3000/products"

def test_update_invalid_data():
    url = f"{BASE_URL}/1"
    payload = {"price": -20}
    response = requests.put(url, json=payload)
    
    # Check status code
    assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"
    
    # Check error message
    json_data = response.json()
    assert json_data.get("message") == "Invalid price. Price cannot be negative.", \
        f"Expected error message 'Invalid price. Price cannot be negative.' but got {json_data.get('message')}"
    
    # Check response time
    assert response.elapsed.total_seconds() < 0.5, f"Response time is too slow: {response.elapsed.total_seconds()} seconds"

def test_create_product_with_missing_data():
    url = BASE_URL
    payload = {
        "title": "",
        "price": ""
    }
    response = requests.post(url, json=payload)
    
    # Check status code
    assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"
    
    # Check error message
    json_data = response.json()
    assert json_data.get("message") == "Title and price are required.", \
        f"Expected error message 'Title and price are required.' but got {json_data.get('message')}"
    
    # Check response contains error message
    assert "message" in json_data, "Response JSON does not contain 'message' key"
    
    # Check response time
    assert response.elapsed.total_seconds() < 0.5, f"Response time is too slow: {response.elapsed.total_seconds()} seconds"
