В задании необходимо:
1) Использовать Python/Java, подключить библиотеку Selenium Webdriver;
2) С помощью Selenium открыть браузер, открыть страницу выше указанной
почты(google.com/yandex.ru) и авторизоваться;
3) С помощью Selenium определить сколько во входящих нашлось писем с
темой «Simbirsoft Тестовое задание»;
4) С помощью Selenium и интерфейса почты написать/отправить письмо на
этот же почтовый ящик, в тексте которого указать найденное в шаге 3
количество писем. Указать тему письма «Simbirsoft Тестовое задание.
<Фамилия>», где <Фамилия> - это Ваша фамилия;
5) Оформить эти действия в виде теста.

При выполнении работы необходимо использовать следующие технологии:
1) Selenium GRID (тесты запускать через GRID обязательно)
2) Использовать паттерн проектирования автотестов Page Object
3) Реализовать формирование отчетов о пройденных тестах через Allure

Данные для авторизации хранятся в файле auth_data.py
Запуск производится из терминала командой pytest test_mail_page.py
