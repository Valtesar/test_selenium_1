from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator{locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator{locator}")

    def get_text_element(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, text),
                                                      message=f"Element has no text{text}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
