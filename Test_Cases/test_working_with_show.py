import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.manage_shows_page import ShowsPage
from pages.create_show_page import CreateShowPage

base_url = "http://10.94.6.100"

class TestCreationEditingDeletingShow():
    @pytest.fixture(scope="module", autouse=True)
    def setup(self, driver):
        self.link = base_url + "/Login"
        page = LoginPage(driver, self.link)
        page.open()
        page.login_user()
        page = HomePage(driver, driver.current_url)
        page.user_is_logged_in()
        page.remove_banner()

    def test_user_creates_show_with_simple_data_Dash_MS_0029(self,driver):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.open_create_show_page() 
        page = CreateShowPage(driver, driver.current_url)
        page.enter_show_code()
        page.select_show_type()
        page.select_show_category()
        page.enter_amount_of_assets()
        page.select_show_status()
        page.enter_amount_of_shots()
        page.enter_show_color()
        page.select_show_start_date()
        page.select_show_end_date()
        page.set_seniority_splits()
        page.select_show_financial()
        page.enter_show_awards_est()
        page.select_show_location()
        page.switch_to_show_inputs_tab()
        page.select_show_primary_producer()
        page.select_show_executive_producer()
        page.set_other_mandatory_fields()
        page.save_show_button_click()