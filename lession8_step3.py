from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    #browser.get("http://suninjuly.github.io/selects1.html")
    browser.get("http://suninjuly.github.io/selects2.html")


    # Считаем сумму чисел
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    summa = int(num1) + int(num2)

    # Находим сумму в выпадающем списке
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector('[value="'+str(summa)+'"]').click()

    # Нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
