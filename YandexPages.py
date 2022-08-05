from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SUGGEST_POPUP = (By.XPATH, "//*[@id='suggest-list-12esx44vj9ni']")
    LOCATOR_TENSOR_LINK = (By.ID, "")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def press_enter(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.send_keys(Keys.RETURN)
        return search_field

    def check_popup(self):
        self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST_POPUP)
        return True

    def check_link(self):
        self.get_text_element(YandexSearchLocators.LOCATOR_TENSOR_LINK, 'tensor.ru')
        return True
