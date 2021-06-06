from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def y(x):
    return math.log(abs(12*math.sin(x)))

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

# Нажимаем на конопку
button = browser.find_element_by_tag_name("button")
button.click()

x=browser.find_element_by_id('input_value').text
textar=browser.find_element_by_id('answer')
textar.send_keys(str(y(int(x))))


button = browser.find_element_by_id("solve")
button.click()
time.sleep(25)
browser.quit()