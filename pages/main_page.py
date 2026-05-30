import allure
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators import MainPageLocators, OrderDetailsLocators, OrderModalLocators
import pyautogui


class MainPage(BasePage):
    """Класс для главной страницы."""

    # --- Методы навигации ---
    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        # Закрываем модальное окно, если оно открыто
        try:
            from locators import OrderModalLocators
            close_button = self.driver.find_element(*OrderModalLocators.CLOSE_BUTTON)
            if close_button.is_displayed():
                self.driver.execute_script("arguments[0].click();", close_button)
                print("Модальное окно закрыто через JavaScript")
                self.wait.until(EC.invisibility_of_element_located(OrderModalLocators.CLOSE_BUTTON))
        except:
            pass

        button = self.wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_FEED_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)
        print("Клик по 'Лента заказов' выполнен через JavaScript")

    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликнуть на кнопку 'Войти в аккаунт'")
    def click_login_account_button(self):
        self.click_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON)

    @allure.step("Кликнуть на кнопку оформления заказа")
    def click_checkout_button(self):
        button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.CHECKOUT_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()

    @allure.step("Кликнуть на логотип Stellar Burgers")
    def click_stellar_burgers_logo(self):
        self.click_element(MainPageLocators.STELLAR_BURGERS_LOGO)

    # --- Метод для переключения вкладок ---
    @allure.step("Переключиться на вкладку 'Булки'")
    def switch_to_buns_tab(self):
        buns_tab = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)
        )
        self.driver.execute_script("arguments[0].click();", buns_tab)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.BUN_INGREDIENT))
        print("Переключено на вкладку 'Булки'")

    # --- Методы для работы с ингредиентами ---
    @allure.step("Кликнуть на булку")
    def click_bun_ingredient(self):
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.BUN_INGREDIENT))
        if self.driver.capabilities['browserName'].lower() == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step("Кликнуть на соус")
    def click_sauce_ingredient(self):
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCE_INGREDIENT))
        if self.driver.capabilities['browserName'].lower() == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step("Кликнуть на начинку")
    def click_filling_ingredient(self):
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.FILLING_INGREDIENT))
        if self.driver.capabilities['browserName'].lower() == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    # --- Методы для drag-and-drop ---
    @allure.step("Добавить булку в заказ")
    def add_bun_to_order(self):
        self.drag_and_drop_ingredient(MainPageLocators.BUN_INGREDIENT)

    def drag_and_drop_ingredient(self, ingredient_locator):
        ingredient = self.wait.until(EC.presence_of_element_located(ingredient_locator))
        constructor_area = self.wait.until(EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_AREA))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ingredient)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", constructor_area)

        browser_name = self.driver.capabilities['browserName'].lower()

        # Логика для двух браузеров
        if browser_name == 'chrome':
            actions = ActionChains(self.driver)
            actions.drag_and_drop(ingredient, constructor_area).perform()
        else:
            # Для Firefox используем pyautogui, учитывая положение окна браузера
            window_pos = self.driver.get_window_position()
            ingredient_location = ingredient.location
            ingredient_size = ingredient.size
            target_location = constructor_area.location
            target_size = constructor_area.size

            start_x = window_pos['x'] + ingredient_location['x'] + ingredient_size['width'] // 2
            start_y = window_pos['y'] + ingredient_location['y'] + ingredient_size['height'] // 2
            end_x = window_pos['x'] + target_location['x'] + target_size['width'] // 2
            end_y = window_pos['y'] + target_location['y'] + target_size['height'] // 2

            pyautogui.moveTo(start_x, start_y)
            pyautogui.dragTo(end_x, end_y, duration=0.5, button='left')

        self.wait.until(lambda d: self.get_ingredient_counter() > 0)
        print(f"✅ Ингредиент добавлен")

    # --- Методы для работы с модальными окнами ---
    @allure.step("Закрыть модальное окно деталей ингредиента")
    def close_modal(self):
        self.wait.until(EC.visibility_of_element_located(OrderDetailsLocators.MODAL_CONTAINER))
        close_button = self.wait.until(EC.presence_of_element_located(OrderDetailsLocators.CLOSE_BUTTON))
        self.driver.execute_script("arguments[0].click();", close_button)
        self.wait.until(EC.invisibility_of_element_located(OrderDetailsLocators.MODAL_CONTAINER))

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        close_button = self.wait.until(EC.presence_of_element_located(OrderModalLocators.CLOSE_BUTTON))
        self.driver.execute_script("arguments[0].click();", close_button)
        self.wait.until(EC.invisibility_of_element_located(OrderModalLocators.CLOSE_BUTTON))
        print("Модальное окно заказа закрыто через JavaScript")

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        def get_clean_order_number():
            element = self.driver.find_element(*OrderModalLocators.ORDER_NUMBER)
            text = element.text
            numbers = re.findall(r'\d+', text)
            if numbers:
                return numbers[0]
            return text.replace('#', '').strip()

        def order_number_is_real(driver):
            order_num = get_clean_order_number()
            print(f"Проверка номера: {order_num}")
            return order_num != "9999" and order_num != ""

        self.wait.until(EC.visibility_of_element_located(OrderModalLocators.ORDER_NUMBER))
        self.wait.until(order_number_is_real)

        order_number = get_clean_order_number()
        print(f"Номер заказа из модального окна (очищенный): {order_number}")
        return order_number

    @allure.step("Получить количество ингредиента")
    def get_ingredient_counter(self):
        self.wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENT_COUNTER))
        counters = self.driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        for counter in counters:
            if counter.text.isdigit() and int(counter.text) > 0:
                print(f"Найден активный счетчик: {counter.text}")
                return int(counter.text)
        return 0

