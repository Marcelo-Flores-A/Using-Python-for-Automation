# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# define url
url = "https://www.amazon.com.mx/"

# instantiate webdriver and open a chrome browser 
# Creates a Chrome WebDriver instance using ChromeDriverManager to automatically download and manage the ChromeDriver executable
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage 
driver.get(url)

# find the category option for narrowing down the search space 
category_option = driver.find_element(By.XPATH, '//*[@id="searchDropdownBox"]/option[15]')
# click on the category option
category_option.click()

# find the search bar 
first_name = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
# fill out the search bar field
first_name.send_keys("Buro para recamara")

# find the search button
search_button = driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
# click on the search button
search_button.click()

# scroll down by 200 units to view the lower part of the page
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

# pause the program for 5 seconds to view the results
sleep(5)

# close the driver
driver.quit()
