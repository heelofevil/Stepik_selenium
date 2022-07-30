from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# функция вычисляющая ответ по формуле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Конструкция для входа на страницу
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Этап вычисления по функции выше
    x_element = browser.find_element(By.CSS_SELECTOR, 'div.form-group #input_value')
    x = x_element.text
    y = calc(x)

    # Вставка ответа
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    # Активация чекбокса
    chekb = browser.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
    chekb.click()

    # Выбор радиобатенов
    radiob = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiob.click()

    # Ожидание
    time.sleep(3)

    # Нажатие кнопки отправить
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()