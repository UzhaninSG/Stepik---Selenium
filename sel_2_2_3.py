from selenium import webdriver
import os
import time


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

# Заполняем фамилию
fio=browser.find_element_by_css_selector('[name="firstname"]')
fio.send_keys('Южанин')

# Заполняем фамилию
fio=browser.find_element_by_css_selector('[name="lastname"]')
fio.send_keys('Станислав')

# Заполняем фамилию
fio=browser.find_element_by_css_selector('[name="email"]')
fio.send_keys('stas@stas.ru')

# Отправляем файл
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'output.txt')
ff=browser.find_element_by_css_selector('[type="file"]')
ff.send_keys(file_path)


button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(25)
browser.quit()