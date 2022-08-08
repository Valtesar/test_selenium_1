from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SUGGEST_POPUP = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YANDEX_LINK = (By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/div[2]/div[1]/a/b')
    LOCATOR_YANDEX_IMAGES = (By.XPATH, "//a[contains(@data-id, 'images')]")  # Локатор кнопки картинки яндекс
    LOCATOR_YANDEX_IMAGES_SEARCH_FIELD = (By.XPATH, "//input[contains(@class, 'input__control mini-suggest__input')]")
    LOCATOR_YANDEX_IMAGES_FIRST_CAT = (By.XPATH, "//div[contains(@class, 'Item_pos_0')]")  # Локатор текста категории
    LOCATOR_YANDEX_IMAGES_FIRST_IMAGE = (By.XPATH, "//div[contains(@class, 'serp-item_pos_0')]")  # Локатор первой картинки поиска
    LOCATOR_YANDEX_IMAGES_NEXT_BUTTON = (By.CLASS_NAME, "CircleButton-Icon")  # Локатор кнопки вперед
    LOCATOR_YANDEX_IMAGES_BACK_BUTTON = (By.XPATH, "//div[contains(@class, 'ButtonNext')]")  # Локатор кнопки назад


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
        self.find_text_element(YandexSearchLocators.LOCATOR_YANDEX_LINK, 'tensor.ru')
        return True

    def go_to_images(self):
        images = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES)
        images.click()
        self.change_window_browser()
        if not self.compare_url_with_current('https://yandex.ru/images/'):
            return False
        else:
            return True

    def check_images_changes(self):
        first_cat_images = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_FIRST_CAT)
        first_cat_images.click()
        name_of_category = first_cat_images.text
        self.find_text_attribute_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_SEARCH_FIELD, name_of_category)
        first_image = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_FIRST_IMAGE)[0]
        first_image.click()
        self.check_url_contains('pos=0')
        next_button = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_NEXT_BUTTON)[3]
        next_button.click()
        self.check_url_contains('pos=1')
        back_button = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_NEXT_BUTTON)[0]
        back_button.click()
        self.check_url_contains('pos=0')
        return True



