from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# функция вычисляющая ответ по формуле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    question = browser.find_element(By.ID, 'input_value')
    sub = question.text
    y = calc(sub)

    # Вставка ответа
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    # скрипт скролит то указанного объекта
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    chekbox = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    chekbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "input[value='robots']")
    radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()