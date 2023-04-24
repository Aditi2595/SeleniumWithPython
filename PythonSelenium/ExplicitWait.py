import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="\\Users\\adititewari\\Downloads\\chromedriver", options=chrome_options)
driver.get("https://chercher.tech/practice/implicit-wait-example")
WebDriverWait(driver, 11).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='q']/input[1]")))
driver.find_element(By.XPATH, "//div[@id='q']/input[1]").click()

