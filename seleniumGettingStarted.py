from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


def random_delay(short=2, long=5):
    """Generate a random delay to mimic human behavior."""
    time.sleep(random.uniform(short, long))


# Set up the driver (assuming Firefox in this case)
driver = webdriver.Firefox()

# Navigate to Ticketmaster
driver.get("https://www.ticketmaster.com/")
random_delay()

# Locate the "Sign In" button using the aria-label attribute
wait = WebDriverWait(driver, 10)
sign_in_button = wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Sign In']"))
)
random_delay()
sign_in_button.click()
random_delay()

# Locate the email input field using the name attribute and simulate typing
email_input = driver.find_element(By.NAME, "email")
for char in "dyland601@gmail.com":
    email_input.send_keys(char)
    random_delay(0.1, 0.3)  # Short delay between key presses

# Locate the password input field using the name attribute and simulate typing
password_input = driver.find_element(By.NAME, "password")
for char in "610Crown!541":
    password_input.send_keys(char)
    random_delay(0.1, 0.3)  # Short delay between key presses

random_delay()

# Locate the "Sign in" button using the data-bdd attribute and click it
sign_in_submit_button = driver.find_element(
    By.XPATH, "//button[@data-bdd='sign-in-button']"
)
random_delay()
sign_in_submit_button.click()
# Close the browser after some time (or continue with other tasks)
# time.sleep(10)
# driver.quit()
