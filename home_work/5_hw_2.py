from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
# поиск элементов
icon = driver.find_element(By.CSS_SELECTOR, '#user-name')
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент поле username найден')
password = driver.find_element(By.CSS_SELECTOR, ' #password')
if password is None:
    print('Элемент не найден')
else:
    print('Элемент поле password найден')
submit = driver.find_element(By.CSS_SELECTOR, 'input#login-button.submit-button')
if submit is None:
    print('Элемент не найден')
else:
    print('Элемент кнопка submit найден')


def visit():
    return driver.get("https://www.saucedemo.com/"), icon, password, submit
