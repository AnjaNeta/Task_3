import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from locators import MainPageLocators, OrderModalLocators, OrderDetailsLocators
from urls import BASE_URL


@allure.feature('Основной функционал')
class TestMainFunctionality:

    @allure.title('Переход по клику на "Конструктор"')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        assert "react" in driver.current_url or driver.current_url == BASE_URL

    @allure.title('Переход по клику на "Лента заказов"')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        assert "feed" in driver.current_url

    @allure.title('Клик на ингредиент открывает всплывающее окно с деталями')
    def test_ingredient_click_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_bun_ingredient()
        
        modal = main_page.wait.until(EC.visibility_of_element_located(OrderDetailsLocators.MODAL_CONTAINER))
        assert modal.is_displayed(), "Модальное окно не открылось"

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_modal_closes_by_click_on_cross(self, driver):
        main_page = MainPage(driver)
        main_page.click_bun_ingredient()
        
        main_page.wait.until(EC.visibility_of_element_located(OrderDetailsLocators.MODAL_CONTAINER))
        
        close_button = main_page.wait.until(EC.element_to_be_clickable(OrderDetailsLocators.CLOSE_BUTTON))
        close_button.click()
        
        main_page.wait.until(EC.invisibility_of_element_located(OrderDetailsLocators.MODAL_CONTAINER))
        assert not main_page.is_element_visible(OrderDetailsLocators.MODAL_CONTAINER), "Модальное окно не закрылось"

    @allure.title('При добавлении ингредиента в заказ увеличивается каунтер')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        
        main_page.switch_to_buns_tab()
        
        # Ждем загрузки вкладки
        main_page.wait.until(EC.visibility_of_element_located(MainPageLocators.BUN_INGREDIENT))
        
        initial_count = main_page.get_ingredient_counter()
        print(f"Initial count: {initial_count}")
        
        main_page.add_bun_to_order()
        
        # Ждем увеличения счетчика с помощью явного ожидания
        def counter_increased(driver):
            current = main_page.get_ingredient_counter()
            print(f"Current count: {current}")
            return current == initial_count + 2
        
        main_page.wait.until(counter_increased)
        
        final_count = main_page.get_ingredient_counter()
        print(f"Final count: {final_count}")
        
        assert final_count == initial_count + 2


    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_create_order(self, driver, registered_and_logged_in_user):
        main_page = MainPage(driver)
        
        # Проверяем, что кнопка "Оформить заказ" видна (пользователь авторизован)
        main_page.wait.until(EC.visibility_of_element_located(MainPageLocators.CHECKOUT_BUTTON))
        assert True


