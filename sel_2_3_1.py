from selenium import webdriver
import os
import time
import math

def y(x):
    return math.log(abs(12*math.sin(x)))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
# Нажимаем на конопку
button = browser.find_element_by_tag_name("button")
button.click()

# Нажимаем ОК в модалке
alert = browser.switch_to.alert
alert.accept()

x=browser.find_element_by_id('input_value').text
textar=browser.find_element_by_id('answer')
textar.send_keys(str(y(int(x))))


button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(25)
browser.quit()