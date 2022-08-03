import json
import pytest
from selenium.webdriver import Chrome, Firefox
CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture(scope='session')
def config():
    # Чтение конфиг-файла JSON, возвращение в виде словаря
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    # Валидация и возвращение выбранного браузера из конфигурационных данных
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Валидация и возвращение времени ожидания из конфиг-файла
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    # Неявное ожидание готовности элементов до попытки взаимодействия
    driver.implicitly_wait(config_wait_time)
    # Возвращение объекта драйвера в конце настройки
    yield driver
    # Для очистки покиньте драйвер
    driver.quit()
