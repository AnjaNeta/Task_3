# Task_3

├── .gitignore
├── requirements.txt
├── conftest.py – фикстуры для браузеров (Chrome/Firefox), создание/удаление пользователя 
├── helpers.py – генерация случайного пользователя, API-функции (создание, логин, удаление)
├── urls.py – URL-адреса приложения и API
├── locators.py – все локаторы элементов для всех страниц

├── pages/
│   ├── base_page.py - базовые методы (клики, ожидания, работа с URL)
│   ├── main_page.py - главная страница (конструктор, ингредиенты, заказы)
│   ├── login_page.py - страница входа (ввод email/пароля, кнопка "Войти")
    └── register_page.py - страница регистрации нового пользователя
│   ├── forgot_password_page.py - восстановление пароля
│   ├── personal_account_page.py - личный кабинет (профиль, история, выход)
│   ├── order_feed_page.py - лента заказов (счётчики, заказы в работе)

├── tests/
│   
│   ├── test_password_recovery.py # Восстановление пароля
│   ├── test_personal_account.py # Личный кабинет 
│   ├── test_main_functionality.py # Проверка основного функционала
│   └── test_order_feed.py # Раздел «Лента заказов»

└── allure-results/

## Tests

# 1. test_personal_account.py:
- test_go_to_personal_account_unauthorized ✅ переход по клику на «Личный кабинет»
- test_go_to_order_history ✅ переход в раздел «История заказов» под зарегистрированным пользователем
- test_logout_from_account ✅  выход из аккаунта


# 2. test_password_recovery.py:
- test_go_to_forgot_password_page ✅  переход на страницу восстановления пароля по кнопке «Восстановить пароль»
- test_restore_password_with_email ✅  ввод почты и клик по кнопке «Восстановить»,
- test_show_password_button_activates_field ✅  клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.
  

# 3. test_main_functionality.py:
- test_go_to_constructor  ✅ переход по клику на «Конструктор»,                            
- test_go_to_order_feed ✅ переход по клику на «Лента заказов»,
- test_ingredient_click_opens_modal ✅ если кликнуть на ингредиент, появится всплывающее окно с деталями 
- test_modal_closes_by_click_on_cross ✅ всплывающее окно закрывается кликом по крестику
- test_ingredient_counter_increases ✅ при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
- test_authorized_user_can_create_order ✅ залогиненный пользователь может оформить заказ

# 4. test_order_feed.py:
- test_click_on_order_opens_details ✅ если кликнуть на заказ, откроется всплывающее окно с деталями
- test_user_orders_appear_in_feed ✅ заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
- test_order_number_appears_in_progress ✅ после оформления заказа его номер появляется в разделе В работе
- test_all_time_counter_increases ✅  при создании нового заказа счётчик Выполнено за всё время увеличивается
- test_today_counter_increases ✅ при создании нового заказа счётчик Выполнено за сегодня увеличивается


## Ручная отладка теста test_personal_account
Открывается страница https://stellarburgers.education-services.ru/
2. Кликаем на Личный Кабинет
3. Скроллом вниз и кликаем на Зарегистрироваться открывается страница https://stellarburgers.education-services.ru/ 
нам нужны уникальные значения для полей:
- Имя: 
- Email
- пароль 
4. Нажимаем на кнопку Зарегистрироваться
Происходит переход на https://stellarburgers.education-services.ru/
5. Вводим Email и пароль уже зарегистрированного пользователя, нажимаем на Войти
6. Открывается страница https://stellarburgers.education-services.ru/
6. Снова кликаем на Личный кабинет - https://stellarburgers.education-services.ru/account/profile - и оказываемся в профиле зарегистрированного пользователя
7. Нажимаем на кнопку История заказов - https://stellarburgers.education-services.ru/account/order-history
8. Дальше нажимаем на кнопку Выход - происходит разлогин (переиспользовать данные авторизованного юзера через фикстуру)


## Ручная отладка теста test_order_feed
1. Пользователь регистрируется и сразу же авторизуется через фикстуру (было решено сделать так, чтобы решить проблему с авторизацией)
2. Открыть ленту заказов
3. Кликнуть на заказ
4. Проверить, что URL изменился (открылась страница с деталями)
5. Проверить, что модальное окно открылось
6. для теста test_order_number_appears_in_progress (После оформления заказа его номер появляется в разделе "В работе") было замечено, что номер заказа галлюционирует после создания заказа: сначала отображается 9999, а потом якобы актуальный номер заказа, это создало определенные сложности для прогона

## Запуск тестов и генерация отчёта

# Запуск по отдельности для проверок успешности прохождения firefox
pytest tests/test_main_functionality.py -v --browser firefox
pytest tests/test_order_feed.py -v --browser firefox
pytest tests/test_password_recovery.py -v --browser firefox
pytest tests/test_personal_account.py -v --browser firefox

## Запуск по отдельности для проверок успешности прохождения chrome
pytest tests/test_main_functionality.py -v --browser chrome
pytest tests/test_order_feed.py -v --browser chrome
pytest tests/test_password_recovery.py -v --browser chrome
pytest tests/test_personal_account.py -v --browser chrome

#  Общий прогон тестов без allure для отладки
pytest tests/ -v --browser firefox
pytest tests/ -v --browser chrome

# Запускаем тесты в Chrome, результаты сохраняются в папку allure_results
pytest tests/ -v --browser chrome --alluredir=allure_results
# Запускаем тесты в Firefox, результаты добавляются к результатам Chrome
pytest tests/ -v --browser firefox --alluredir=allure_results

# Сгенерировать и открыть Allure-отчёт
# Генерируем отчёт из всех результатов (Chrome + Firefox)
allure generate allure_results -o allure-report --clean
# Открываем отчёт в браузере
allure open allure-report
