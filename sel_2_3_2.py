from selenium import webdriver
import os
import time
import math

def y(x):
    return math.log(abs(12*math.sin(x)))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
# Нажимаем на конопку
button = browser.find_element_by_tag_name("button")
button.click()

# Переходим на другую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x=browser.find_element_by_id('input_value').text
textar=browser.find_element_by_id('answer')
textar.send_keys(str(y(int(x))))


button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(25)
browser.quit()