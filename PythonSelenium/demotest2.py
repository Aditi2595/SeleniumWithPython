import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="\\Users\\adititewari\\Downloads\\chromedriver", options=chrome_options)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.NAME, "from").send_keys("del")
time.sleep(3)
from_airport = driver.find_elements(By.XPATH, "//ul[@id='xyz']/li/div")
for airport in from_airport:
    if airport.text == "New Delhi":
        airport.click()
    else:
        pass

    




#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)