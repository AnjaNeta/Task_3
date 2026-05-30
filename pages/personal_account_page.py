import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):
    """Класс для страницы личного кабинета."""
    
    @allure.step("Кликнуть на ссылку 'Профиль'")
    def click_profile_link(self):
        self.click_element(PersonalAccountPageLocators.PROFILE_LINK)
    
    @allure.step("Кликнуть на ссылку 'История заказов'")
    def click_order_history_link(self):
        self.click_element(PersonalAccountPageLocators.ORDER_HISTORY_LINK)
    
    @allure.step("Кликнуть на кнопку 'Выход'")
    def click_logout_button(self):
    # Ждём, пока кнопка станет кликабельной
        logout_button = self.wait.until(EC.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON))
    
    # Скроллим к кнопке
        self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_button)
    
    # Кликаем через JavaScript
        self.driver.execute_script("arguments[0].click();", logout_button)



