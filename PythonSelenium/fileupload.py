import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="\\Users\\adititewari\\Downloads\\chromedriver", options=chrome_options)
driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("/Users/adititewari/Downloads/selenium_tutorial.pdf")
sleep(3)
driver.find_element(By.XPATH, "//input[@id='file-submit']").click()

# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)