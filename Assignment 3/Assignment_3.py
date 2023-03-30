from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the browser driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.conestogac.on.ca/")

# Wait for page to load
time.sleep(6)

# Maximizing the window
driver.maximize_window()

# Find Programs & Courses link and click it
programs_link = driver.find_element("xpath", "/html/body/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/a[1]")
programs_link.click()

# Wait for page to load
time.sleep(6)

# Find Full-time link and click it
full_time_link = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[2]/div/div[1]/a")
full_time_link.click()

# Wait for page to load
time.sleep(6)

# Find International Students checkbox and click it
intl_students_checkbox = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[2]/div/div/div[3]/div/div[2]/div/form/div[4]/div/div/div[1]/div/label[2]/span")
intl_students_checkbox.click()

# Wait for page to load
time.sleep(6)

# Find the start date dropdown and select it
start_date_dropdown = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[2]/div/div/div[3]/div/div[2]/div/form/div[4]/div/div/div[2]/a/span/span")
start_date_dropdown.click()

# Wait for page to load
time.sleep(6)

# Find the May 2023 dropdown and select it
may_2023_dropdown = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[2]/div/div/div[3]/div/div[2]/div/form/div[4]/div/div/div[2]/div/label[3]/span")
may_2023_dropdown.click()

# Wait for page to load
time.sleep(6)

# Find the Apply Filter button and click it
apply_filter_button = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[2]/div/div/div[3]/div/div[2]/div/form/div[5]/div[1]/button/span/span[1]")
apply_filter_button.click()

# Wait for page to load
time.sleep(6)

# Find the Applied Energy Management program and click it
aem_link = driver.find_element("xpath", "/html/body/div[3]/div[3]/div[2]/div/div/div[3]/div/div[1]/div[1]/div/div/ul/li[4]/a/span/span[1]")
# Click the link
aem_link.click()

# Wait for page to load
time.sleep(6)

# Close the browser
driver.quit()
