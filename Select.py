from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

# Конструкция для входа на страницу
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, 'num1')
first_num = num1.text
num2 = browser.find_element(By.ID, 'num2')
second_num = num2.text
summa_nums = str(int(first_num) + int(second_num))

# Открыть селектор
select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
select.select_by_value(summa_nums)

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(5)
browser.quit()