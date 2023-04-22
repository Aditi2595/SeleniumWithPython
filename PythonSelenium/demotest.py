from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="\\Users\\adititewari\\Downloads\\chromedriver", options=chrome_options)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
#driver.find_element(By.ID, "name").send_keys("Aditi")
#driver.find_element(By.ID,"alertbtn").click()
###TODO: To find an element by a tag text
#driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

## TODO: To find an element by css selector tag and attribute
driver.find_element(By.CSS_SELECTOR, "input[value='radio1']").click()
## TODO: to find an element by using css selector id, we can use name as well
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Aditi")

## TODO: find element using xpath
a = driver.find_element(By.XPATH, "//div[@class='tableFixHead']/table/tbody/tr[5]/td[2]").text
print(a)

## TODO: finding xpath using ancestor method
# b = driver.find_element(By.XPATH, "//option[@value='option3']/ancestor::div[@class='block large-row-spacer']").text
# print(b)

## TODO: Selecting multiple checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox == checkboxes[1]:
        pass
    else:
        checkbox.click()
sleep(2)

##TODO : Selecting from static dropdown
static_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
static_dropdown.select_by_visible_text('Option3')
sleep(2)
static_dropdown.select_by_index((2))
sleep(2)
static_dropdown.select_by_value("option1")



#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)