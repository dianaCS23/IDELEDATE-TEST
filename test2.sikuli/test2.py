
# Get the current path of the script
current_dir = getBundlePath()

# Create dynamic paths for the images
banner_image = os.path.join(current_dir, "images", "1.png")
login_field_image = os.path.join(current_dir, "images", "2.png")
password_field_image = os.path.join(current_dir, "images", "3.png")
login_button_image = os.path.join(current_dir, "images", "4.png")

# User credentials
username = "dianasalguero"
password = "Nosequeponer23#"

# Check if the banner is present on the screen
if exists(banner_image):
    print("The 'Buggy Rating' banner is present.")
    
    # Enter the username
    if exists(login_field_image):
        click(login_field_image)
        type(username)
        print("Username entered.")
    else:
        print("Login field not found.")
    
    # Enter the password
    if exists(password_field_image):
        click(password_field_image)
        type(password)
        print("Password entered.")
    else:
        print("Password field not found.")
    
    # Click on the Login button
    if exists(login_button_image):
        click(login_button_image)
        print("Clicked on the 'Login' button.")
    else:
        print("The 'Login' button is not found.")
else:
    print("The 'Buggy Rating' banner is not present.")
