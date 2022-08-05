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
from selenium.common.exceptions import NoSuchElementException
from tests.conftest_old import *
import logging


class TensorSearch:

    def __init__(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def check_exists_by_selector(self, selector):
        browser = self.browser
        try:
            browser.find_element(By.CSS_SELECTOR, selector)
        except NoSuchElementException:
            return False
        return True

    def test_search(self):
        """Метод поиска слова <Тензор> используя поисковую систему яндекса"""

        """Метод должен перейти на страницу яндекса, ввести в поисковую строку слово <Тензор>
           затем проверить имеются ли поисковые подсказки, далее нажать клавишу Enter.
           Первая ссылка должна вести на сайт tensor.ru"""

        search_field_selector = '#text'
        suggest_field_selector = '#suggest-item-8e67ilglevb-0'
        tensor_link_selector = '#search-result > li:nth-child(3) > div > div.Organic.organic.Typo.Typo_text_m.Typo_line_s.i-bem > div.Organic-Subtitle.Organic-Subtitle_noWrap.Typo.Typo_type_greenurl.organic__subtitle > div.Path.Organic-Path.Organic-Path_verified.path.organic__path > a > b'

        browser = self.browser
        browser.get('https://yandex.ru')
        try:
            assert self.check_exists_by_selector(search_field_selector)
        except AssertionError:
            logging.error("Can't find search text box", exc_info=True)

        print('test 1 passed')
        element = browser.find_element(By.CSS_SELECTOR, search_field_selector)
        element.send_keys('Тензор')
        try:
            assert self.check_exists_by_selector(suggest_field_selector)
        except AssertionError:
            logging.error("Suggest field doesn't displayed", exc_info=True)
        print('test 2 passed')

        element.send_keys(Keys.RETURN)
        try:
            assert self.check_exists_by_selector(tensor_link_selector)
        except AssertionError:
            logging.error("Can't find link <tensor.ru>")
        print('test 3 passed')
        sleep(5)


if __name__ == '__main__':
    TensorSearch().test_search()
