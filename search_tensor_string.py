import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class TensorSearch:

    def __init__(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search(self):
        """Метод поиска слова <Тензор> используя поисковую систему яндекса"""

        """Метод должен перейти на страницу яндекса, ввести в поисковую строку слово <Тензор>
           затем проверить имеются ли поисковые подсказки, далее нажать клавишу Enter.
           Первая ссылка должна вести на сайт tensor.ru"""

        browser = self.browser
        browser.get('https://yandex.ru')
        element = browser.find_element(By.XPATH, '//input[@id="text"]')
        element.send_keys('Тензор')
        element.send_keys(Keys.RETURN)

        sleep(5)


if __name__ == '__main__':
    TensorSearch().test_search()
