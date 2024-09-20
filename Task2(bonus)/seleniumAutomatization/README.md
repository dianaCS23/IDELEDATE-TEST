# Python Scripts for Page Performance, Error Detection, and Data Automation

## Prerequisites
- **Python 3.x**
- **Selenium WebDriver**
- **ChromeDriver**

To run these scripts, you need to have the following installed:

### Installing Python Dependencies

```bash
pip install selenium
```

## Overview
This repository contains three Python scripts designed to:
1. **Evaluate the performance of a web page**.
2. **Detect errors** in key functionalities.
3. **Automate data processing** and streamline the interaction with the webpage for testing purposes.

The scripts utilize **Selenium WebDriver** for automating browser interactions and verifying the presence and correctness of web elements.

---

## Files

### 1. `performance.py`
This script measures the performance of a target web page by loading it through a browser and recording its load time. It captures:
- **Page Load Time**
- **DOM Content Load Time**

#### Key Features:
- Opens the web page using Selenium WebDriver.
- Logs performance metrics into a file.
- Can be integrated into a larger pipeline for automated performance monitoring.

### 2. `error_detection.py`
Focuses on verifying that the banner element is available.

#### Key Features:

- Handles **exceptions** (e.g., missing elements) and logs detailed error information.


### 3. `data_automation.py`
The **data automation** script fills in a registration form with predefined data and submits it automatically.

#### Key Features:
- Automatically fills form fields such as username, first name, last name, and password.
- Validates successful registration through the presence of a success message.
- Generates an HTML report with the results of the test, highlighting both successes and failures.

---


