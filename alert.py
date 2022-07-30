from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# функция вычисляющая ответ по формуле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
# переход на окно алерта
alert = browser.switch_to.alert
alert.accept()

x_elem = browser.find_element(By.ID, 'input_value')
num = x_elem.text
y = calc(num)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)

button1 = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

time.sleep(5)
browser.quit()