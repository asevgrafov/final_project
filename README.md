# final_project
[![Build Status](https://travis-ci.com/asevgrafov/final_project.png)](https://travis-ci.com/asevgrafov/final_project)
# Автотесты

Selenium Python

# Контроль качества кода

Реализован с помощью pre-commit hook, который проверяет и форматирует код перед коммитом.

## Установка

    pip install pre-commit
    pre-commit install

## Использование

Хук запускается автоматически перед коммитом. Принудительный запуск:

    pre-commit run --all-files

## Запуск конкретной проверки

  `pre-commit run <hook_id> <options>`

`hook-id`  - идентификатор хука;
`-a, --all-files`   - запуск всех все файлов в репозитории;
`--files [FILES[FILES...]]`   - запуск для конкретных файлов.


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

## Отчёты в pytest-html

### Установка

 `pip install pytest-html`

>доступно с Python >=3.6 или PyPy3
