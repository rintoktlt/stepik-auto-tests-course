from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    # Считываем значение х
    x_element = browser.find_element_by_id('input_value').text

    # Считаем математическую функцию
    y = calc(x_element)

    # Поднимаем поле для ввода наверх
    input1 = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)

    # Вводим ответ в поле ответа
    input1.send_keys(y)

    # Выбираем необходимые опции
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
