from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    # Wait to let results load (optional)
    driver.implicitly_wait(5)

    # Print the title of the page
    print(f"Page title is: {driver.title}")

    # Take a screenshot of the current page
    screenshot_path = "google_search_results.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")
