import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LoginPageLocators
from urls import BASE_URL


class LoginPage(BasePage):
    """Класс для страницы логина."""
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        element = self.wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        print(f"Поле email найдено: {element.get_attribute('name')}")
        element.clear()
        element.send_keys(email)
        print(f"Email введён: {email}")

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT))
        print(f"Поле пароля найдено: {element.get_attribute('name')}")
        element.clear()
        element.send_keys(password)
        print(f"Пароль введён: {password}") 
        
    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_login_button(self):
        button = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)
        print("Клик по кнопке 'Войти' выполнен через JavaScript")
    
    @allure.step("Кликнуть на ссылку 'Зарегистрироваться'")
    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)
    
    @allure.step("Кликнуть на ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
    
    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        
        print("🔹 Кликаем на кнопку 'Войти'...")
        login_button = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        self.driver.execute_script("arguments[0].click();", login_button)
        
        # Ожидаем перехода на главную страницу
        self.wait.until(EC.url_to_be(BASE_URL))
        print(f"URL после клика: {self.driver.current_url}")
        
        # Проверяем наличие ошибки (если страница не изменилась, возможно ошибка)
        if "login" in self.driver.current_url:
            page_source = self.driver.page_source
            if "неверный" in page_source.lower() or "incorrect" in page_source.lower():
                raise AssertionError("Найдено сообщение об ошибке на странице логина")

