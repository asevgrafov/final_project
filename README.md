[![Build Status](https://travis-ci.com/asevgrafov/final_project.svg?branch=main)](https://travis-ci.com/asevgrafov/final_project)

# Swag Labs

Цель - автоматизация тестирования web-приложения с помощью PyTest + Selenium + Python

https://www.saucedemo.com/



### How to start
1. Использовать python 3.6 +
2. Создать виртуальное окружение https://docs.python.org/3/library/venv.html
3. Выполнить команду в терминале
    ```buildoutcfg
    pip install -r requirements.txt
    ```
4. Запустить тесты при помощи команды
    ```buildoutcfg
    pytest -m smoke
      ```
5. Для отчётов используется Allure http://allure.qatools.ru/

   Запуск

    ```buildoutcfg
    pytest --alluredir <dir_name>
    ```

    Просмотр отчёта

    > Запустить команду в powershell в той папке, где лежит <dir_name>

    ```buildoutcfg
    allure serve <dir_name>
    ```

6. Для хранения документации используется Testrail https://finalproject2021.testrail.io/index.php?/projects/overview/1

    Запуск

    ```buildoutcfg
    pytest --testrail --tr-config=testrail.cfg
    ```

7. Контроль качества кода реализован с помощью pre-commit hook. Хук запускается автоматически перед коммитом.

   Установка

    ```buildoutcfg
    pip install pre-commit
    pre-commit install
    ```

    Принудительный запуск:

    ```buildoutcfg
    pre-commit run --all-files
    ```
