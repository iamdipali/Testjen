from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (ensure the correct driver is installed and in PATH)
driver = webdriver.Chrome()  # or webdriver.Edge(), webdriver.Firefox(), etc.
driver.maximize_window()

try:
    # Open the browser and navigate to Google
    driver.get("https://www.google.com")
    print("Opened Google successfully.")

    # Find the search bar using its name attribute
    search_box = driver.find_element(By.NAME, "q")

    # Enter the search term and hit Enter
    search_term = "Selenium Python"
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    print(f"Searching for: {search_term}")

    # Wait to let results load (adjust time if needed)
    driver.implicitly_wait(5)

    # Find the desired search result using its XPath
    result_xpath = "//div[@id='rso']//a[@href='https://selenium-python.readthedocs.io/']/h3[.='Selenium with Python — Selenium Python Bindings 2 ...']"
    result = driver.find_element(By.XPATH, result_xpath)

    # Click on the search result
    result.click()
    print("Clicked on the search result.")

    # Wait for the page to load
    time.sleep(5)

    # Take a screenshot of the current page
    screenshot_path = "selenium_python_page.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")
