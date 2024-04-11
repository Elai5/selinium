from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# webdriver is an automation tool to controll googlechrome
# in this part, we demonstarte how to use web browser to find an element

service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")
# from google website we get to search for element
# can be by id,classname and so on, by inputing send key, we specify what we want it to search without us having to type it

# after time(5) program doesnt exixt, it crashes
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)


input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear() 
input_element.send_keys("jamie oliver" + Keys.ENTER)
# be able to type other element using arrow key

# after time(5) program doesnt exixt, it crashes
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)


link = driver.find_element(By.PARTIAL_LINK_TEXT, "Jamie Oliver")
link.click()

# after time(5) program doesnt exixt, it crashes
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)



time.sleep(10)

driver.quit()