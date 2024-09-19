# Unit Tests Documentation

This repository contains unit tests for the Fake Store API, implemented using `pytest`. The tests are designed to verify the functionality and performance of the API.



## Dependencies

To run these tests, you need to have the following installed:

- **Python 3.x**: The programming language used for the tests.
  
- **pytest**: The testing framework used for running the tests.

  You can install `pytest` using pip:

  ```bash
  pip install pytest
  ```

## Running the Tests

To run the unit tests, navigate to the `UnitTests` directory and execute the following command:

```bash
pytest
```

This will discover and run all the test files in the directory.

## Test Cases

### test_fake_store.py

This file contains tests for the Fake Store API. The following tests are included:

1. **Test Status Code**: Verifies that the API returns a 200 status code.
2. **Test Response Time**: Ensures that the response time is less than 2 seconds.
3. **Test Category - Men's Clothing**: Checks that products exist in the "men's clothing" category.
4. **Test Men's Clothing Item Properties**: Validates that each item has required properties (`id`, `title`, `price`, `category`, `description`, `image`).
5. **Test Men's Clothing Item Prices**: Confirms that the prices of men's clothing products are valid.

### test_api.py

This file contains additional tests for the API's functionality, ensuring robust validation and error handling.

## Generating Test Reports

To generate an HTML report of the test results, you can run:

```bash
pytest --html=report.html
```

This will create a report file named `report.html` in the current directory.



