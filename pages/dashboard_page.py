from pages.locators import ResourceManagerLocators
from .base_page import BasePage

class DashboardPage(BasePage):
    def user_see_dashboard_content_text(self):
        dashboard_content_text = self.driver.find_element(*ResourceManagerLocators.RESOURCE_MNG_DASHBOARD_TEXT).text
        assert dashboard_content_text == "Select the options you want.", f"Select the options you want. is expected, but {dashboard_content_text} is displayed"