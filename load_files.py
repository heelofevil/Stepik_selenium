from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


inpu1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
inpu1.send_keys('Ivan')

inpu2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
inpu2.send_keys("Ivanchenko")

inpu3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
inpu3.send_keys("ffwef@fwf.com")

# loader =  os.path.abspath(os.path.dirname('C:/ff/ada.txt'))
# file_path = os.path.join(loader, 'ada.txt')
# просто вставил путь то файла
filesend = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
filesend.send_keys('C:/ff/ada.txt')

button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

time.sleep(5)
browser.quit()