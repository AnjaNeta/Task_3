import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from locators import PersonalAccountPageLocators
from locators import OrderModalLocators


@allure.feature('Личный Кабинет')
class TestPersonalAccount:

    @allure.title('Переход по клику на "Личный Кабинет" для неавторизованного пользователя')
    def test_go_to_personal_account_unauthorized(self, driver):
        main_page = MainPage(driver)
        main_page.close_modal_if_exists(OrderModalLocators.CLOSE_BUTTON)
        main_page.click_personal_account_button()
        assert main_page.is_url_contains("login"), "Не выполнен переход на страницу логина"

    @allure.title('Переход в личный кабинет для авторизованного пользователя')
    def test_go_to_personal_account_authorized(self, driver, logged_in_user):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        assert main_page.is_url_contains("account"), "Не выполнен переход в личный кабинет"

    @allure.title('Переход в раздел "История заказов из личного кабинета"')
    def test_go_to_order_history(self, driver, logged_in_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        
        main_page.click_personal_account_button()
        personal_account_page.click_order_history_link()
        assert main_page.is_url_contains("order-history"), "Не выполнен переход в историю заказов"
    
    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self, driver, logged_in_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        
        main_page.click_personal_account_button()
        personal_account_page.click_logout_button()
        assert main_page.is_url_contains("login"), "Не выполнен переход на страницу логина после выхода"

        

