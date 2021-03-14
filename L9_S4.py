from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Нажимаем в модальном окне ОК
    alert = browser.switch_to.alert
    alert.accept()

    # Считываем значение х
    x_element = browser.find_element_by_id('input_value').text

    # Считаем математическую функцию
    y = calc(x_element)

    # Вводим ответ в поле ответа
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    # Нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
