import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators import OrderFeedPageLocators, OrderModalLocators


@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('Если кликнуть на заказ, откроется страница с деталями заказа')
    def test_click_on_order_opens_details(self, driver, registered_and_logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed_button()
        main_page.wait.until(EC.presence_of_element_located(OrderFeedPageLocators.ORDER_NUMBER_IN_FEED))
        
        current_url = driver.current_url
        order_feed_page.click_first_order()
        
        main_page.wait.until(lambda driver: driver.current_url != current_url)
        
        assert "feed" in driver.current_url and len(driver.current_url) > len(current_url)

    @allure.title('Заказы пользователя из истории отображаются в ленте заказов')
    def test_user_orders_appear_in_feed(self, driver, registered_and_logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.add_bun_to_order()
        main_page.click_checkout_button()
        
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()
        
        main_page.click_order_feed_button()
        main_page.wait.until(EC.presence_of_element_located(OrderFeedPageLocators.ORDER_NUMBER_IN_FEED))
        
        # Явное ожидание: ждём, что в ленте появится хотя бы один элемент
        main_page.wait.until(lambda driver: len(driver.find_elements(*OrderFeedPageLocators.ORDER_NUMBER_IN_FEED)) > 0)
        
        # Прокручиваем страницу вниз
        driver.execute_script("window.scrollBy(0, 500);")
        main_page.wait.until(lambda driver: driver.execute_script("return window.pageYOffset") > 0)
        
        assert order_feed_page.is_order_present_in_feed(order_number)

    @allure.title('При создании заказа счётчик "Выполнено за всё время" увеличивается')
    def test_all_time_counter_increases(self, driver, registered_and_logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed_button()
        initial_counter = order_feed_page.get_all_time_counter()
        
        main_page.click_constructor_button()
        main_page.add_bun_to_order()
        main_page.click_checkout_button()
        
        main_page.wait.until(EC.visibility_of_element_located(OrderModalLocators.ORDER_NUMBER))
        main_page.close_order_modal()
        
        main_page.click_order_feed_button()
        main_page.wait.until(EC.presence_of_element_located(OrderFeedPageLocators.ALL_TIME_COUNTER))
        
        assert order_feed_page.get_all_time_counter() > initial_counter

    @allure.title('При создании заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_counter_increases(self, driver, registered_and_logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed_button()
        initial_counter = order_feed_page.get_today_counter()
        
        main_page.click_constructor_button()
        main_page.add_bun_to_order()
        main_page.click_checkout_button()
        
        main_page.wait.until(EC.visibility_of_element_located(OrderModalLocators.ORDER_NUMBER))
        main_page.close_order_modal()
        
        main_page.click_order_feed_button()
        main_page.wait.until(EC.presence_of_element_located(OrderFeedPageLocators.TODAY_COUNTER))
        
        assert order_feed_page.get_today_counter() > initial_counter

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_number_appears_in_progress(self, driver, registered_and_logged_in_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.add_bun_to_order()
        main_page.click_checkout_button()
        
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()
        
        main_page.click_order_feed_button()
        main_page.wait.until(EC.presence_of_element_located(OrderFeedPageLocators.ORDERS_IN_PROGRESS))
        
        assert order_feed_page.is_order_in_progress(order_number)

