import allure
from pages.base_page import BasePage
from locators import RegisterPageLocators


class RegisterPage(BasePage):
    """Класс для страницы регистрации."""
    
    @allure.step("Ввести имя")
    def enter_name(self, name):
        self.send_keys(RegisterPageLocators.NAME_INPUT, name)
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        self.send_keys(RegisterPageLocators.EMAIL_INPUT, email)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.send_keys(RegisterPageLocators.PASSWORD_INPUT, password)
    
    @allure.step("Кликнуть на кнопку 'Зарегистрироваться'")
    def click_register_button(self):
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)
    
    @allure.step("Зарегистрировать нового пользователя")
    def register(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register_button()

        