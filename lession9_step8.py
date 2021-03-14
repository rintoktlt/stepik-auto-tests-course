from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока значение прайса не достигнит 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    # Считываем значение х
    x_element = browser.find_element_by_id('input_value').text

    # Считаем математическую функцию
    y = calc(x_element)

    # Поднимаем поле для ввода наверх
    input1 = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)

    # Вводим ответ в поле ответа и нажимаем кнопку
    input1.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
