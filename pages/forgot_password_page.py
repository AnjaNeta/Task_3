import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    """Класс для страницы восстановления пароля."""
    
    @allure.step("Ввести email для восстановления")
    def enter_email(self, email):
        self.send_keys(ForgotPasswordPageLocators.EMAIL_INPUT, email)
    
    @allure.step("Кликнуть на кнопку 'Восстановить'")
    def click_restore_button(self):
        self.click_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
    
    @allure.step("Кликнуть на кнопку показа/скрытия пароля")
    def click_show_password_button(self):
        # Ждём, пока кнопка станет кликабельной
        button = self.wait.until(EC.element_to_be_clickable(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON))
        button.click()
    
    @allure.step("Проверить, что поле пароля стало активным")
    def is_password_field_active(self):
        # Ждём, пока поле пароля появится на странице
        element = self.wait.until(EC.visibility_of_element_located(ForgotPasswordPageLocators.NEW_PASSWORD_FIELD))
        return element.is_enabled()

        