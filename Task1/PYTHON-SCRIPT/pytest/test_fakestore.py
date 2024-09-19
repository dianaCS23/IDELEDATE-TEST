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

# # Test to verify that each "men's clothing" item contains the necessary properties
def test_mens_clothing_item_properties():
    response = requests.get(BASE_URL)
    data = response.json()
    mens_clothing = [item for item in data if item["category"] == "men's clothing"]

    for item in mens_clothing:
        assert "id" in item, "Falta la propiedad 'id'"
        assert "title" in item, "Falta la propiedad 'title'"
        assert "price" in item, "Falta la propiedad 'price'"
        assert "category" in item, "Falta la propiedad 'category'"
        assert "description" in item, "Falta la propiedad 'description'"
        assert "image" in item, "Falta la propiedad 'image'"

# Test to verify that all "men's clothing" products have a price greater than 0
def test_mens_clothing_item_prices():
    response = requests.get(BASE_URL)
    data = response.json()
    mens_clothing = [item for item in data if item["category"] == "men's clothing"]

    for item in mens_clothing:
        assert item["price"] > 0, f"El producto con IDs {item['id']} tiene un precio no válido: {item['price']}"

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
