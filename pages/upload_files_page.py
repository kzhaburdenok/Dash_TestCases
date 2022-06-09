from pages.locators import UploadDataLocators
from .base_page import BasePage

class UploadFilesPage(BasePage):
    def user_see_upload_file_title(self):
        return True