from operator import contains
from selenium.webdriver import Remote as RemoteWebDriver # импортим ремоут вебдрайвер
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
from .locators import BasePageLocators

class BasePage():
    def __init__(self, driver: RemoteWebDriver, base_url, timeout = 5):
        self.driver = driver
        self.url = base_url
        self.driver.implicitly_wait(timeout)

    def open(self, timeout = 10):
        self.driver.get(self.url)
        self.driver.implicitly_wait(timeout)

    def remove_banner(self):
        time.sleep(6)
        self.driver.find_element(*BasePageLocators.BANNER_CLOSE_ICON).click()    

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout = 5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def user_opens_the_page(self, how, what, timeout = 20):
        global name_text, words_in_name
        page_name_loaded = EC.element_to_be_clickable((how, what))
        WebDriverWait(self.driver, timeout).until(page_name_loaded)
        page_name = self.driver.find_element(how, what)
        name_text = page_name.text
        words_in_name = name_text.split(" ")
        page_name.click()
        time.sleep(2)

    def user_see_the_title(self, how, what, timeout = 45):
        title_element = EC.visibility_of_element_located((how,what))
        WebDriverWait(self.driver, timeout).until(title_element)
        time.sleep(10)
        title = self.driver.find_element(how, what).text
        assert contains(title,words_in_name[0]), f"'{name_text}' is expected, but '{title}' is displayed"
