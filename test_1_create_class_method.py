import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_1(): #создаем класс Test_1
    def test_select_product(self): #создаем метод
        driver = webdriver.Chrome(
            executable_path='C:\\Users\\user\\Desktop\\PycharmProjects\\resource\\chromedriver.exe')  # Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
        base_url = 'https://www.saucedemo.com/'  # совершенствуем код в переменную пихаем юрл который используем, удобно для ооп и для списков юрл
        driver.get(base_url)  # указываем url на который мы хотим заходить
        driver.maximize_window()  # открывается браузер на максимальный экран
        time.sleep(5)

        print("Start Test")

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))  # обращение к элемену через id
        user_name.send_keys(login_standard_user)
        print("Input Login")

        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(password_all)
        print("Input Password")

        button_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print("Click Login Button")

        select_product = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click Select Product")

        enter_shopping_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
        enter_shopping_cart.click()
        print("Click Enter Shopping Cart")

        succes_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_succes_test = succes_test.text
        assert value_succes_test == "YOUR CART"
        print("Test Succes!!!!")

        time.sleep(5)

test = Test_1() # объявляем экземпляр класса Test_1
test.test_select_product()
