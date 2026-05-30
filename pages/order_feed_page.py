import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import OrderFeedPageLocators, OrderDetailsLocators, OrderModalLocators


class OrderFeedPage(BasePage):
    """Класс для страницы ленты заказов."""
    
    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order(self):
        order_card = self.wait.until(EC.element_to_be_clickable(OrderFeedPageLocators.ORDER_CARD))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_card)
        order_card.click()
        print("Клик по первому заказу выполнен")
    
    @allure.step("Получить счётчик 'Выполнено за всё время'")
    def get_all_time_counter(self):
        element = self.wait.until(EC.visibility_of_element_located(OrderFeedPageLocators.ALL_TIME_COUNTER))
        return int(element.text)
    
    @allure.step("Получить счётчик 'Выполнено за сегодня'")
    def get_today_counter(self):
        element = self.wait.until(EC.visibility_of_element_located(OrderFeedPageLocators.TODAY_COUNTER))
        return int(element.text)
    
    def normalize_order_number(self, order_number):
        """Нормализует номер заказа (добавляет ведущий ноль до 6 цифр)."""
        return str(order_number).zfill(6)
    
    def is_order_present_in_feed(self, order_number):
        """Проверяет, отображается ли заказ в ленте"""
        # Ждем появления всех элементов заказов
        self.wait.until(EC.presence_of_all_elements_located(OrderFeedPageLocators.ORDER_NUMBER_IN_FEED))
        
        # Получаем все номера заказов
        order_elements = self.driver.find_elements(*OrderFeedPageLocators.ORDER_NUMBER_IN_FEED)
        
        # Проверяем, есть ли нужный номер
        for element in order_elements:
            if order_number in element.text:
                return True
        
        return False
    
    @allure.step("Проверить, что заказ находится в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        """Проверяет, находится ли заказ в разделе 'В работе'."""
        normalized_order = self.normalize_order_number(order_number)
        
        # Ждем появления элементов в разделе "В работе"
        self.wait.until(EC.presence_of_element_located(OrderFeedPageLocators.ORDERS_IN_PROGRESS))
        
        # Получаем все заказы в работе
        orders_in_progress = self.driver.find_elements(*OrderFeedPageLocators.ORDERS_IN_PROGRESS)
        
        # Проверяем, есть ли наш номер заказа
        for order in orders_in_progress:
            if normalized_order in order.text:
                return True
        
        return False
    
    @allure.step("Получить номер заказа из деталей")
    def get_order_number_from_details(self):
        return self.get_text(OrderDetailsLocators.ORDER_NUMBER)

        