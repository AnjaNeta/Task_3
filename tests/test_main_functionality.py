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
        assert main_page.is_url_contains("react") or main_page.get_current_url() == BASE_URL

    @allure.title('Переход по клику на "Лента заказов"')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        assert main_page.is_url_contains("feed")

    @allure.title('Клик на ингредиент открывает всплывающее окно с деталями')
    def test_ingredient_click_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_bun_ingredient()
        assert main_page.is_element_visible(OrderDetailsLocators.MODAL_CONTAINER), "Модальное окно не открылось"

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_modal_closes_by_click_on_cross(self, driver):
        main_page = MainPage(driver)
        main_page.click_bun_ingredient()
        assert main_page.is_element_visible(OrderDetailsLocators.MODAL_CONTAINER), "Модальное окно не открылось"
        
        main_page.close_modal()
        assert not main_page.is_element_visible(OrderDetailsLocators.MODAL_CONTAINER), "Модальное окно не закрылось"

    @allure.title('При добавлении ингредиента в заказ увеличивается каунтер')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.switch_to_buns_tab()
        
        initial_count = main_page.get_ingredient_counter()
        main_page.add_bun_to_order()
        final_count = main_page.get_ingredient_counter()
        
        assert final_count == initial_count + 2, f"Счётчик увеличился не на 2: {initial_count} -> {final_count}"

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_create_order(self, driver, logged_in_user):
        main_page = MainPage(driver)
        assert main_page.is_element_visible(MainPageLocators.CHECKOUT_BUTTON), "Кнопка 'Оформить заказ' не отображается"

        