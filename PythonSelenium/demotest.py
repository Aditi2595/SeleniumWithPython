from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="\\Users\\adititewari\\Downloads\\chromedriver", options=chrome_options)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
#driver.find_element(By.ID, "name").send_keys("Aditi")
#driver.find_element(By.ID,"alertbtn").click()
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)