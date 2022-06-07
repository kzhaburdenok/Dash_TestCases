import pytest
import random

from pages.home_page import HomePage
from pages.login_page import LoginPage

base_url = "http://10.94.6.100:50000"

class TestUserCanSwitchAmongTabs():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.link = base_url + "/Login"
        self.page = LoginPage(driver, self.link)
        self.page.open()
        self.page.login_user()
 

    def test_user_logged_in(self,driver):
        self.page = HomePage(driver, driver.current_url)
        self.page.user_is_logged_in()
        self.page.remove_banner() 