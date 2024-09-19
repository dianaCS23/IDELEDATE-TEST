import unittest
import requests

# Define the base URL of the API
BASE_URL = "https://fakestoreapi.com/products"

class TestFakeStoreAPI(unittest.TestCase):
    
    def setUp(self):
        """Set up the initial state for the tests."""
        # Make a GET request to the API and store the response
        self.response = requests.get(BASE_URL)
        # Convert the response to JSON format for use in tests
        self.data = self.response.json()

    def test_status_code(self):
        """Verify that the API returns a 200 status code."""
        self.assertEqual(self.response.status_code, 200, 
                         f"Expected status code 200, but got {self.response.status_code}")

    def test_response_time(self):
        """Verify that the response time is less than 2 seconds."""
        response_time = self.response.elapsed.total_seconds()
        self.assertLess(response_time, 2.0, 
                        f"Response time too slow: {response_time} seconds")

    def test_category_mens_clothing(self):
        """Verify that there are products in the 'men's clothing' category."""
        # Filter products to find those in the 'men's clothing' category
        mens_clothing = [item for item in self.data if item["category"] == "men's clothing"]
        self.assertGreater(len(mens_clothing), 0, 
                           "No products found in the 'men's clothing' category")

    def test_mens_clothing_item_properties(self):
        """Verify that men's clothing items have required properties."""
        mens_clothing = [item for item in self.data if item["category"] == "men's clothing"]

        for item in mens_clothing:
            # Check that each product contains the required properties
            self.assertIn('id', item, "Missing property 'id'")
            self.assertIn('title', item, "Missing property 'title'")
            self.assertIn('price', item, "Missing property 'price'")
            self.assertIn('category', item, "Missing property 'category'")
            self.assertIn('description', item, "Missing property 'description'")
            self.assertIn('image', item, "Missing property 'image'")

    def test_mens_clothing_item_prices(self):
        """Verify that the prices of men's clothing products are valid."""
        mens_clothing = [item for item in self.data if item["category"] == "men's clothing"]

        for item in mens_clothing:
            # Ensure that the price of each product is greater than 0
            self.assertGreater(item["price"], 0, 
                               f"Product with ID {item['id']} has an invalid price: {item['price']}")

if __name__ == "__main__":
    # Run all tests when the script is executed directly
    unittest.main()
