from .locators import DownloaddataLocators
from .base_page import BasePage

class DownloadFilesPage(BasePage):
    def user_see_download_file_title(self):
        return True