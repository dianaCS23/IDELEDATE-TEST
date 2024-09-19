# Login Automation Script

This script automates the login process for a web application by checking for specific UI elements and entering user credentials.

## Overview

The script performs the following actions:
1. Checks for the presence of a banner on the screen.
2. Enters the username and password into their respective fields.
3. Clicks the login button to submit the credentials.

## Requirements

- Python environment 
- The images of the UI elements (banner, login field, password field, login button) must be placed in an `images` directory relative to the script's path.

## Directory Structure

```
test2.sikuli/
│
├── test2.py          # The main script for login automation
└── images/            # Directory containing images for UI elements
    ├── 1.png         # Banner image
    ├── 2.png         # Login field image
    ├── 3.png         # Password field image
    └── 4.png         # Login button image
```

## User Credentials

The script uses the following credentials to log in:

- **Username:** `dianasalguero`
- **Password:** `Nosequeponer23#`

## Usage

1. Make sure the required images are in the `images` folder.
2. Run the script 
3. The script will check for the presence of the banner and interact with the login form.


