import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="\\Users\\adititewari\\Downloads\\chromedriver", options=chrome_options)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//a[text()='Top']")).click().perform()

