import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators import OrderFeedPageLocators, OrderModalLocators


@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('Если кликнуть на заказ, откроется страница с деталями заказа')
    def test_click_on_order_opens_details(self, driver, logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed_button()
        current_url = main_page.get_current_url()
        order_feed_page.click_first_order()
        
        assert main_page.is_url_changed(current_url), "URL не изменился после клика на заказ"

    @allure.title('Заказы пользователя из истории отображаются в ленте заказов')
    def test_user_orders_appear_in_feed(self, driver, logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.add_bun_to_order()
        main_page.click_checkout_button()
        
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()
        
        main_page.click_order_feed_button()
        
        assert order_feed_page.is_order_present_in_feed(order_number), f"Заказ {order_number} не найден в ленте"

    @allure.title('При создании заказа счётчик "Выполнено за всё время" увеличивается')
    def test_all_time_counter_increases(self, driver, logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed_button()
        initial_counter = order_feed_page.get_all_time_counter()
        
        main_page.click_constructor_button()
        main_page.add_bun_to_order()
        main_page.click_checkout_button()
        
        main_page.wait.until(EC.visibility_of_element_located(OrderModalLocators.ORDER_NUMBER))
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()
        
        main_page.click_order_feed_button()
        assert order_feed_page.is_all_time_counter_increased(initial_counter), "Счётчик 'Выполнено за всё время' не увеличился"
    

    @allure.title('При создании заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_counter_increases(self, driver, logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed_button()
        initial_counter = order_feed_page.get_today_counter()
        
        main_page.click_constructor_button()
        main_page.add_bun_to_order()
        main_page.click_checkout_button()
        
        main_page.wait.until(EC.visibility_of_element_located(OrderModalLocators.ORDER_NUMBER))
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()
        
        main_page.click_order_feed_button()
        assert order_feed_page.is_today_counter_increased(initial_counter), "Счётчик 'Выполнено за сегодня' не увеличился"

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_number_appears_in_progress(self, driver, logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.add_bun_to_order()
        main_page.click_checkout_button()
        
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()
        
        main_page.click_order_feed_button()
        assert order_feed_page.is_order_in_progress(order_number), f"Заказ {order_number} не появился в разделе 'В работе'"

