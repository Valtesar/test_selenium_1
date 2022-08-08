from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def change_window_browser(self):
        window_after = self.driver.window_handles[1]
        return self.driver.switch_to.window(window_after)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def find_text_element(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, text),
                                                      message=f"Can't find text {text} in element")

    def find_text_attribute_element(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element_attribute(locator, "value", text),
                                                      message=f"Element has no text {text}")

    def compare_url_with_current(self, url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_contains(url),
                                                      message=f"Link {url} invalid")

    def check_url_contains(self, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_contains(text),
                                                      message=f"Url not contained this text {text}")

    def get_current_url(self):
        return self.driver.current_url

    def go_to_site(self):
        return self.driver.get(self.base_url)
