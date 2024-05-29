
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Selenium and the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (without opening a browser window)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Open the Amazon page
url = 'https://www.amazon.de/s?k=PS4&rh=p_36%3A27500-65000&ref=nb_sb_noss'
driver.get(url)

# Allow the page to load
time.sleep(5)

# Locate all elements with the specified attributes
elements = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

# Extract and print the href attribute from each element
hrefs = [element.get_attribute('href') for element in elements]
for href in hrefs:
    print(href)

# Close the driver
driver.quit()
