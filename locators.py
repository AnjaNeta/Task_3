from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы."""
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Вкладки
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")

    # Ингредиенты
    BUN_INGREDIENT = (By.XPATH, "//p[text()='Краторная булка N-200i']")
    SAUCE_INGREDIENT = (By.XPATH, "//p[text()='Соус с шипами Антарианского плоскоходца']")
    FILLING_INGREDIENT = (By.XPATH, "//p[text()='Хрустящие минеральные кольца']")
    
    # Область конструктора для перетаскивания
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")
    
    # Кнопка оформления заказа
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Логотип Stellar Burgers
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__')]/a")
    
    # Счётчик ингредиентов
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter__')]//p[contains(@class, 'counter_counter__num__')]")


class LoginPageLocators:
    """Локаторы страницы логина."""
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class RegisterPageLocators:
    """Локаторы страницы регистрации."""
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")


class ForgotPasswordPageLocators:
    """Локаторы страницы восстановления пароля."""
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    NEW_PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")


class PersonalAccountPageLocators:
    """Локаторы страницы личного кабинета."""
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@href, 'order-history')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class OrderDetailsLocators:
    """Локаторы окна деталей заказа."""
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]")
    # Контейнер модального окна
    MODAL_CONTAINER = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__')]")

class OrderModalLocators:
    """Локаторы модального окна заказа."""
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__')]//h2[contains(@class, 'text_type_digits-large')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]")

class OrderFeedPageLocators:
    """Локаторы страницы ленты заказов."""
    # Карточка заказа (первая)
    ORDER_CARD = (By.XPATH, "(//a[contains(@class, 'OrderHistory_link__')])[1]")
    # Номер заказа в ленте
    ORDER_NUMBER_IN_FEED = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")
    # Счётчик "Выполнено за всё время"
    ALL_TIME_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[1]")
    # Счётчик "Выполнено за сегодня"
    TODAY_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[2]")
    # Заказы в работе
    ORDERS_IN_PROGRESS = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")



