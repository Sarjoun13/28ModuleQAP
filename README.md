  Этот репозиторий — является итоговым проектом курса Тестировщик-автоматизатор на Python | SkillFactory.
Репозиторий был создан с использованием шаблона PageObject с Selenium и PyTest (Python).
Проект содержит UI тесты сайта "Ростелеком": https://b2c.passport.rt.ru

  Подготовка к запуску:

Скопируйте репозиторий на свой компьютер.
Если вы используете PyCharm, он автоматически запрашивает установку необходимых библиотек.
Если нет - установите требуемые библиотеки в файле requirements.txt.


Файлы:

в папке tests: test_rostelecom.py - все автотесты
               driver.exe - Chromedriver

в папке Pages: base.py - содержит библиотеку Smart Page Object

auth_page.py - содержит класс для страницы "Авторизация"

auth_page_with_code.py - содержит класс для страницы "Авторизация с временным кодом"

elements.py - содержит класс для определения элементов на веб-страницах

register_page.py - содержит класс для страницы "Регистрация"

Запуск тестов:

 py -m pytest -v --driver Chrome --driver-path driver.exe 
 или
 python -m pytest -v --driver Chrome --driver-path driver.exe
