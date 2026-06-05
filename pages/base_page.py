import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def click_element(self, locator):
        """Клик на элемент с прокруткой."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        """Ввод текста в поле."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Получение текста элемента."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def is_element_visible(self, locator, timeout=10):
        """Проверка видимости элемента с ожиданием."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False
    
    def scroll_to_element(self, element, block='center'):
        """Прокручивает страницу до указанного элемента."""
        self.driver.execute_script(f"arguments[0].scrollIntoView({{block: '{block}'}});", element)
    
    def scroll_to_locator(self, locator, block='center'):
        """Прокручивает страницу до элемента по локатору."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.scroll_to_element(element, block)
        return element
    
    def wait_for_url_contains(self, text, timeout=10):
        """Ожидает, что URL содержит указанный текст."""
        WebDriverWait(self.driver, timeout).until(lambda driver: text in driver.current_url)
    
    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url
    
    def is_url_contains(self, text, timeout=10):
        """Проверяет, содержит ли текущий URL указанную строку (с ожиданием)."""
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: text in driver.current_url)
            return True
        except:
            return False
    
    def is_url_changed(self, old_url, timeout=10):
        """Проверяет, изменился ли URL по сравнению с переданным."""
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.current_url != old_url)
            return True
        except:
            return False
    
    def get_page_source(self):
        """Возвращает HTML-код текущей страницы."""
        return self.driver.page_source
    
    def is_text_present(self, text):
        """Проверяет, содержится ли указанный текст в HTML-коде страницы."""
        return text.lower() in self.driver.page_source.lower()
    
    def click_js(self, element):
        """Кликает на элемент через JavaScript с прокруткой."""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
    
    def execute_script(self, script, *args):
        """Выполняет JavaScript код."""
        return self.driver.execute_script(script, *args)
    
    def find_element(self, locator):
        """Находит элемент по локатору."""
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """Находит все элементы по локатору."""
        return self.driver.find_elements(*locator)
    
    def get_browser_name(self):
        """Возвращает имя браузера."""
        return self.driver.capabilities['browserName'].lower()
    
    def get_window_position(self):
        """Возвращает позицию окна браузера."""
        return self.driver.get_window_position()
    
    def close_modal_if_exists(self, close_button_locator):
        """Закрывает модальное окно, если оно открыто."""
        try:
            close_button = self.driver.find_element(*close_button_locator)
            if close_button.is_displayed():
                self.click_js(close_button)
                self.wait.until(EC.invisibility_of_element_located(close_button_locator))
                return True
        except:
            pass
        return False
    
    def wait_for_url(self, expected_url, timeout=10):
        """Ожидает, что текущий URL станет равен ожидаемому."""
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

        