'''

browser.implicitly_wait(5) говорим WebDriver ждать все элементы в течение 5 секунд
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
тут смотреть медоты ожидания 
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


# функция вычисляющая ответ по формуле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
# говорим WebDriver ждать все элементы в течение 5 секунд
#browser.implicitly_wait(12)

#
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button1 = browser.find_element(By.ID, "book")
button1.click()

x_elem = browser.find_element(By.ID, 'input_value')
num = x_elem.text
y = calc(num)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)

button1 = browser.find_element(By.ID, 'solve').click()

time.sleep(5)
browser.quit()