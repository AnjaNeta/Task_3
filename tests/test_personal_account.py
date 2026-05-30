import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from locators import PersonalAccountPageLocators


@allure.feature('Личный Кабинет')
class TestPersonalAccount:

    @allure.title('Переход по клику на "Личный Кабинет" для неавторизованного пользователя')
    def test_go_to_personal_account_unauthorized(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        assert "login" in driver.current_url

    @allure.title('Переход в раздел "История заказов"')
    def test_go_to_order_history(self, driver, registered_and_logged_in_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        
        main_page.click_personal_account_button()
        main_page.wait_for_url_contains("account")
        
        personal_account_page.click_order_history_link()
        
        assert "order-history" in driver.current_url

    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self, driver, registered_and_logged_in_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        
        main_page.click_personal_account_button()
        main_page.wait_for_url_contains("account")
        
        main_page.wait.until(EC.visibility_of_element_located(PersonalAccountPageLocators.LOGOUT_BUTTON))
        personal_account_page.click_logout_button()
        main_page.wait_for_url_contains("login")
        assert "login" in driver.current_url

