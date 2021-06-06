from selenium import webdriver
import math
import time

def y(x):
    return math.log(abs(12*math.sin(x)))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)
x=browser.find_element_by_id('input_value').text
print(x)

textar=browser.find_element_by_id('answer')
textar.send_keys(str(y(int(x))))

chek=browser.find_element_by_id('robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", chek)
chek.click()

opt1=browser.find_element_by_id('robotsRule')
opt1.click()


button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(25)
browser.quit()