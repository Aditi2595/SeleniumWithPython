import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="\\Users\\adititewari\\Downloads\\chromedriver", options=chrome_options)
driver.get("https://chercher.tech/practice/implicit-wait-example")
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//div[@id='q']/input[1]").click()
driver.find_element(By.XPATH, "//div[@id='q']/input[3]").click()


# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)