# Unit Tests for Fake Store API

This repository contains unit tests for the Fake Store API, implemented using `unittest`. The tests verify the functionality and reliability of the API.


## Dependencies

To run these tests, you need to have the following installed:

- **Python 3.x**: The programming language used for the tests.

- **requests**: The library used to make HTTP requests.

  You can install the `requests` library using pip:

  ```bash
  pip install requests
  ```

## Running the Tests

To run the unit tests, navigate to the `UnitTests` directory and execute the following command:

```bash
python -m unittest test_fake_store_api.py
```

This command will discover and run all the tests defined in the `test_fake_store_api.py` file.

## Test Cases

The following tests are included in `test_fake_store_api.py`:

1. **Test Status Code**: Verifies that the API returns a 200 status code when a request is made.

2. **Test Response Time**: Ensures that the response time for the API is less than 2 seconds.

3. **Test Category - Men's Clothing**: Confirms that products exist in the "men's clothing" category.

4. **Test Men's Clothing Item Properties**: Validates that each item in the men's clothing category contains required properties (`id`, `title`, `price`, `category`, `description`, `image`).

5. **Test Men's Clothing Item Prices**: Ensures that the prices of men's clothing products are greater than 0.

