[![Build Status](https://travis-ci.com/asevgrafov/final_project.svg?branch=main)](https://travis-ci.com/asevgrafov/final_project)

# Swag Labs

UI python tests with selenium https://www.saucedemo.com/

This is a test project for training. PyTest + Selenium + Python


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
6. Для хранения документации используется Testrail https://www.gurock.com/testrail/



# Контроль качества кода

Реализован с помощью pre-commit hook, который проверяет и форматирует код перед коммитом.

## Установка

    pip install pre-commit
    pre-commit install

## Использование

Хук запускается автоматически перед коммитом. Принудительный запуск:

    pre-commit run --all-files


# Отчёты

Для удобного анализа результатов тестирования, добавлен функционал построения очётов

## Отчёты в Allure

### Установка

**Scoop**

В powershell выполнить две команды для установки scoop:

    Set-ExecutionPolicy RemoteSigned -scope CurrentUser

    Invoke-Expression (New-Object System.Net.WebClient).DownloadString('[https://get.scoop.sh]')

**Allure**

C помощью scoop установить Allure:

       scoop install allure

>Необходимо проверить, установлена ли Java. Для этого ввести allure и нажать enter. Если не установлена, то необходимо установить и добавить в переменные окружения.

### Запуск

    pytest --alluredir <dir_name>

### Просмотр отчёта

> Запустить команду в powershell в той папке, где лежит <dir_name>

    allure serve <dir_name>

## Testrail


https://finalproject2021.testrail.io/index.php?/projects/overview/1

## Запуск

    pytest --testrail --tr-config=testrail.cfg
