from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_form(url, form_data):
    # Set the path to your WebDriver (e.g., chromedriver.exe for Chrome)
    driver_path = 'C:\Users\Siddhanth\Downloads\chromedriver_win32\\chromedriver.exe'
    
    
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(executable_path=driver_path)

    # Open the website
    driver.get(url)

    # Fill the form
    for field, value in form_data.items():
        element = driver.find_element(By.NAME, field)
        element.send_keys(value)

    # Wait for the "I'm not a robot" captcha
    try:
        # Replace 'CAPTCHA_SELECTOR' with the actual selector of the captcha element
        captcha_element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'CAPTCHA_SELECTOR'))
        )
        input("Please solve the captcha and press Enter to continue...")
    except Exception as e:
        print(f"Exception: {e}")
    
    # Continue with form submission
    submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    # Example form data (replace with your actual form fields and values)
    form_data = {
        'username': 'your_username',
        'password': 'your_password',
        'email': 'your_email@example.com'
        # Add more fields as needed
    }

    # URL of the website's form
    target_url = 'https://example.com/form'

    # Call the function to fill the form
    fill_form(target_url, form_data)
