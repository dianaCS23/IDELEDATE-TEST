import requests
import pytest

# Define the API base URL
BASE_URL = "https://fakestoreapi.com/products"

# Test to verify that the API returns status code 200
def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"Código de estado esperado 200, pero se obtuvo {response.status_code}"

# Test to validate that the response time is acceptable (<500ms)
def test_response_time():
    response = requests.get(BASE_URL)
    response_time = response.elapsed.total_seconds()
    assert response_time < 1.0, f"Tiempo de respuesta demasiado lento: {response_time} segundos"

#  Test to ensure that there are products in the "men's clothing" category
def test_category_mens_clothing():
    response = requests.get(BASE_URL)
    data = response.json()
    mens_clothing = [item for item in data if item["category"] == "men's clothing"]
    assert len(mens_clothing) > 0, "No se encontraron productos en la categoría 'men's clothing'"


# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
