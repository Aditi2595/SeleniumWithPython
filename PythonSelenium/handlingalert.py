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
driver.find_element(By.ID, "name").send_keys("Aditi")
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
popup = driver.switch_to.alert
time.sleep(2)
assert "Aditi" in popup.text
print(popup.text)
popup.accept()
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)