import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.manage_shows_page import ShowsPage

base_url = "http://10.94.6.100"

class TestManageShowsTab():
    @pytest.fixture(scope="module", autouse=True)
    def setup(self, driver):
        self.link = base_url + "/Login"
        page = LoginPage(driver, self.link)
        page.open()
        page.login_user()
        page = HomePage(driver, driver.current_url)
        page.user_is_logged_in()
        page.remove_banner()

    def test_user_see_show_card_content_Dash_MS_0001(self, driver):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.find_max_qty_of_lines_in_focus_top()
        page.count_lines_qty()
        page.count_cards_qty_first_line()
        page.select_show()
        page.show_title_displaying()
        page.show_status_displaying()
        page.show_type_displaying()
        page.show_primary_producer_displaying()
        page.show_executive_producer_displaying()
        page.show_start_date_displaying()
        page.show_end_date_displaying()
        page.show_seniority_split_displaying()
        page.show_right_menu_displaying()

    @pytest.mark.parametrize('filter', ["Active", "Inactive", "Delivered"])
    def test_search_show_by_status_Dash_MS_0008(self, driver, filter):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.filter_show_by_status(filter)
        page.scroll_list_of_shows()
        page.count_lines_qty()
        page.count_cards_qty_first_line()
        page.count_cards_qty_last_line()
        page.count_shows_qty()
        #page.only_shows_of_filtered_status_displaying(filter)
        page.header_counters_calculation(filter)

    def test_user_opens_manage_show_page_Dash_MS_0015(self,driver):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.find_max_qty_of_lines_in_focus_top()
        page.count_lines_qty()
        page.count_cards_qty_first_line()
        page.select_show()
        page.show_title_displaying()        
        page.open_manage_show_page()
        page.manage_show_page_title()
        page.name_of_open_show()
        page.check_default_tab_manage_show()
        page.check_edit_show_ui_displaying()

    def test_user_opens_ones_page_Dash_MS_0017(self, driver):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.find_max_qty_of_lines_in_focus_top()
        page.count_lines_qty()
        page.count_cards_qty_first_line()
        page.select_show()
        page.show_title_displaying()
        page.open_show_ones_page_from_show_card()
        page.check_show_code_preselected()
        page.check_show_quota_ui_displaying()

    def test_user_opens_financial_page_Dash_MS_0018(self, driver):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.find_max_qty_of_lines_in_focus_top()
        page.count_lines_qty()
        page.count_cards_qty_first_line()
        page.select_show()
        page.show_title_displaying()
        page.open_financials_page_from_show_card()
        page.check_show_code_in_url()

    def test_user_opens_create_show_page_Dash_MS_0020(self, driver):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.open_create_show_page()
        page.create_show_page_title_displaying()
        page.check_default_tab_manage_show()

    def test_necessary_tabs_displaying_manage_show_Dash_MS_0024(self, driver):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.find_max_qty_of_lines_in_focus_top()
        page.count_lines_qty()
        page.count_cards_qty_first_line()
        page.select_show()    
        page.open_manage_show_page()    
        page.check_tabs_list()    
        page.check_bid_weeks_in_edit_mode()
        page.check_show_ui_displaying()
    
    def test_necessary_tabs_displaying_create_show_Dash_MS_0024(self, driver):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.open_create_show_page()   
        page.check_tabs_list()    
        page.check_bid_weeks_in_create_mode()

    def test_create_empty_show_notification_displaying_Dash_MS_0027(self, driver):
        self.link = base_url + "/ones/new/shows"
        page = ShowsPage(driver, self.link)
        page.open()
        page.open_create_show_page() 
        page.save_show_button_click()
        page.confirm_pop_ups_appearance_when_empty_show_saved()
        page.check_show_ui_displaying()