from .locators import ContactAdminLocators
from .base_page import BasePage

class ContactAdminPage(BasePage):
    def user_see_admin_content_text(self):
        content_text = self.driver.find_element(*ContactAdminLocators.CONTENT_MESSAGE).text
        assert content_text == "Please enter either Global ID or Username.", f"'Please enter either Global ID or Username.' is expected, but '{content_text}' is displayed"