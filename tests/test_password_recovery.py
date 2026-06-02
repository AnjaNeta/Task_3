import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from helpers import generate_random_user, create_user


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_go_to_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.click_personal_account_button()
        login_page.click_forgot_password_link()
        
        assert main_page.is_url_contains("forgot-password"), "Не выполнен переход на страницу восстановления пароля"

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_restore_password_with_email(self, driver):
        user_data = generate_random_user()
        create_user(user_data)
        
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        
        main_page.click_personal_account_button()
        login_page.click_forgot_password_link()
        forgot_password_page.enter_email(user_data["email"])
        forgot_password_page.click_restore_button()
        
        assert main_page.is_url_contains("reset-password"), "Не выполнен переход на страницу сброса пароля"

    @allure.title('Клик по кнопке показа/скрытия пароля делает поле активным')
    def test_show_password_button_activates_field(self, driver):
        user_data = generate_random_user()
        create_user(user_data)
        
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        
        main_page.click_personal_account_button()
        login_page.click_forgot_password_link()
        forgot_password_page.enter_email(user_data["email"])
        forgot_password_page.click_restore_button()
        
        assert main_page.is_url_contains("reset-password"), "Не выполнен переход на страницу сброса пароля"
        
        # Проверяем, что кнопка показа пароля работает
        forgot_password_page.click_show_password_button()
        
        # Проверяем, что поле пароля стало активным (можно вводить)
        assert forgot_password_page.is_password_field_active(), "Поле пароля не стало активным после клика по кнопке показа"

