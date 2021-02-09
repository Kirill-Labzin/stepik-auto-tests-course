from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
         EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button = browser.find_element_by_css_selector("button[id='book']")
button.click()

x_element = browser.find_element_by_css_selector("span[id='input_value']")
x = x_element.text
y = calc(x)
    
input1 = browser.find_element_by_id("answer")
input1.send_keys(calc(x))

button = browser.find_element_by_css_selector("button[id='solve']")
button.click()

time.sleep(10)
browser.quit()
