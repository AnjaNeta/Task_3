import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from urls import BASE_URL, API_REGISTER_URL, API_LOGIN_URL
from helpers import generate_random_user, delete_user
from pages.main_page import MainPage
from pages.login_page import LoginPage


class WebDriverFactory:
    """Фабрика для создания драйверов браузеров."""
    
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-search-engine-choice-screen')
            driver = webdriver.Chrome(options=options)
            driver.set_page_load_timeout(15)
            return driver
        
        elif browser_name == "firefox":
            options = FirefoxOptions()
            options.binary_location = "/Applications/Firefox-ESR.app/Contents/MacOS/firefox"
            options.add_argument('--width=1920')
            options.add_argument('--height=1080')
            
            options.set_preference("app.update.enabled", False)
            options.set_preference("dom.webnotifications.enabled", False)
            options.set_preference("dom.event.contextmenu.enabled", True)
            options.set_preference("ui.dragThresholdX", 0)
            options.set_preference("ui.dragThresholdY", 0)
            
            driver = webdriver.Firefox(options=options)
            driver.set_page_load_timeout(15)
            return driver
        
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests: chrome or firefox"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    
    allure.dynamic.parameter("Browser", browser)
    allure.dynamic.label("browser", browser)
    allure.dynamic.tag(browser)
    
    
    driver = WebDriverFactory.get_driver(browser)
    driver.get(BASE_URL)
    driver.delete_all_cookies()

    yield driver
    
    driver.quit()


@pytest.fixture
def wait(driver):
    """Фикстура для явного ожидания."""
    return WebDriverWait(driver, 10)


@pytest.fixture
def registered_user():
    """Фикстура: создаёт пользователя через API и возвращает его данные."""
    user_data = generate_random_user()
    response = requests.post(API_REGISTER_URL, json=user_data)
    
    if response.status_code != 200:
        raise Exception(f"Не удалось создать пользователя через API: {response.text}")
    
    yield user_data
    
    login_response = requests.post(API_LOGIN_URL, json={"email": user_data["email"], "password": user_data["password"]})
    if login_response.status_code == 200:
        access_token = login_response.json().get('accessToken')
        if access_token:
            delete_user(access_token)
            


@pytest.fixture
def logged_in_user(driver, registered_user):
    """Фикстура: выполняет вход через UI для созданного пользователя."""
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    
    main_page.click_personal_account_button()
    main_page.wait_for_url_contains("login")
    login_page.login(registered_user["email"], registered_user["password"])
    main_page.wait_for_url_contains(BASE_URL)
    
    
    return registered_user

