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
        element.clear()
        element.send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)
    
    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_login_button(self):
        button = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        self.click_js(button)

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
        self.click_login_button()
        
        # Ожидаем перехода на главную страницу
        self.wait_for_url(BASE_URL)
    
    @allure.step("Проверить наличие ошибки на странице логина")
    def has_login_error(self):
        """Проверяет, есть ли сообщение об ошибке на странице логина."""
        return self.is_text_present("неверный") or self.is_text_present("incorrect")
    
    @allure.step("Проверить, что пользователь не авторизован и остался на странице логина")
    def is_on_login_page(self):
        """Проверяет, что текущая страница - страница логина."""
        return self.is_url_contains("login")

        