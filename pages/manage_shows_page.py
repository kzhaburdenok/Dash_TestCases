from operator import contains
import random

from .locators import ManageShowsLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class ShowsPage(BasePage):
    def find_max_qty_of_lines_in_focus_top(self):
        global max_qty_of_lines_in_focus
        lines_in_focus = self.driver.find_element(*ManageShowsLocators.SHOWS_LINES_ON_THE_TOP)
        max_qty_of_lines_in_focus = int(lines_in_focus.get_attribute('childElementCount'))

    def scroll_list_of_shows(self):
        time.sleep(5)
        self.driver.find_element(*ManageShowsLocators.MANAGE_SHOW_HEADER).click()
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)

    def count_lines_qty(self):
        global lines_qty, lines_height
        time.sleep(3)
        lines = self.driver.find_element(*ManageShowsLocators.SHOWS_MIN_HEIGHT)
        lines_height_attribute = lines.get_attribute("style")
        lines_height_values = lines_height_attribute.split(" ")
        lines_height_px = lines_height_values[1]
        lines_height = lines_height_px[:-3]
        lines_qty = int(lines_height)/300

    def count_cards_qty_first_line(self):
        global cards_qty_first_line
        shows_line = self.driver.find_element(By.XPATH, "(//div[@class='shows'])[1]")
        cards_qty_first_line = shows_line.get_attribute('childElementCount')

    def count_cards_qty_last_line(self):
        global cards_qty_in_last_line
        shows_line = self.driver.find_element(By.XPATH, "(//div[@class='shows'])[last()]")
        cards_qty_in_last_line = shows_line.get_attribute('childElementCount')

    def count_shows_qty(self):
        global shows_qty
        shows_qty = ((int(lines_qty))-1) * int(cards_qty_first_line) + int(cards_qty_in_last_line)

    def select_show(self):    
        global i
        time.sleep(3)
        max_pg_dn = int(lines_qty)/4
        page_down_qty = random.randint(0, int(max_pg_dn))
        self.driver.find_element(*ManageShowsLocators.MANAGE_SHOW_HEADER).click()
        for press_pg_dn in range(0, page_down_qty+1):
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        if press_pg_dn == 0:
            max_to_be_found = int(max_qty_of_lines_in_focus-1) * int(cards_qty_first_line)
            i = str(random.randrange(1, max_to_be_found))
        elif press_pg_dn > 0 and press_pg_dn < 4:
            max_to_be_found = int(max_qty_of_lines_in_focus+2) * int(cards_qty_first_line)
            i = str(random.randrange(5, max_to_be_found))
        else:
            max_to_be_found = int(max_qty_of_lines_in_focus+4) * int(cards_qty_first_line)
            i = str(random.randrange(12, max_to_be_found))
        
        time.sleep(6)

    def show_title_displaying(self,timeout = 5):   
        global show_code, show_name
        self.driver.implicitly_wait(timeout)
        show_title = self.driver.find_element(By.XPATH, f"(//div[@class='show shows__item'])["+i+"]/descendant::div[@class='info__title']").text
        title = show_title.split(" | ")
        if len(title) == 2:
            show_code = title[0]
            show_name = title[1]
            assert show_code, "show code is not displayed"
            assert show_name, "show name is not displayed"
        else:
            show_code = title[0]
            assert show_code, "show code is not displayed"

    def show_status_displaying(self,timeout = 5):
        self.driver.implicitly_wait(timeout)
        show_status = self.driver.find_element(By.XPATH, f"(//div[@class='show shows__item'])["+i+"]/descendant::div[@class='info__status status']").get_attribute('innerText')
        assert show_status == "Active" or show_status == "Inactive" or show_status == "Delivered", f"Wrong status is displayed. Current value is {show_status}"

    def show_type_displaying(self,timeout = 5):
        self.driver.implicitly_wait(timeout)
        show_type = self.driver.find_element(By.XPATH, f"(//div[@class='show shows__item'])["+i+"]/descendant::div[@class='info__type type']").get_attribute('innerText')
        type = show_type.split("\n")
        type_name = type[1]
        assert type_name == "Awarded" or type_name == "Blocked Potential" or type_name == "Blocked Speculative", f"Wrong type is displayed. Current value is {type_name}"

    def show_primary_producer_displaying(self,timeout = 5):
        self.driver.implicitly_wait(timeout)
        show_primary_producer = self.driver.find_element(By.XPATH, "(//span[contains(text(), 'Primary Producer')]/parent::div)["+i+"]").get_attribute('innerText')
        primary_producer = show_primary_producer.split("\n")
        if len(primary_producer) == 2:
            primary_producer_name = primary_producer[1]
            assert primary_producer_name, "Primary Producer name is not displayed"

    def show_executive_producer_displaying(self,timeout = 5):
        self.driver.implicitly_wait(timeout)
        show_executive_producer = self.driver.find_element(By.XPATH, "(//span[contains(text(), 'Executive Producer')]/parent::div)["+i+"]").get_attribute('innerText')
        lines = show_executive_producer.split("\n")
        if len(lines) == 2:
            executive_producer_name = lines[1]
            assert executive_producer_name, "there is no name"

    def show_start_date_displaying(self,timeout = 5):
        self.driver.implicitly_wait(timeout)
        show_start_date = self.driver.find_element(By.XPATH, "(//span[contains(text(), 'Start Date')]/parent::div)["+i+"]").get_attribute('textContent')
        lines = show_start_date.split("\n")
        start_date = lines[1]
        assert start_date, "Start date is missed"

    def show_end_date_displaying(self,timeout = 5):
        self.driver.implicitly_wait(timeout)
        show_end_date = self.driver.find_element(By.XPATH, "(//span[contains(text(), 'End Date')]/parent::div)["+i+"]").get_attribute('textContent')
        lines = show_end_date.split("\n")
        end_date = lines[1]
        assert end_date, "End date is missed"

    def show_release_date_displaying(self,timeout = 5):
        self.driver.implicitly_wait(timeout)
        show_release_date = self.driver.find_element(By.XPATH, "(//span[contains(text(), 'Release Date')]/parent::div)["+i+"]").get_attribute('innerText')
        lines = show_release_date.split("\n")
        if len(lines) == 2:
            release_date = lines[1]
            assert release_date, "Release date is not displayed"

    def show_seniority_split_displaying(self,timeout = 5):
        self.driver.implicitly_wait(timeout)
        seniority_split_line = self.driver.find_element(By.XPATH, "(//div[@class='show__seniority seniority'])["+i+"]").get_attribute('innerText')
        lines = seniority_split_line.split("\n")
        artist = lines[0]
        key_artist = lines[1]
        lead = lines[2]
        assert artist and key_artist and lead, "seniority split is missed"  

    def show_right_menu_displaying(self,timeout = 5):
        self.driver.implicitly_wait(timeout)
        right_menu_list = self.driver.find_element(By.XPATH, "(//div[@class='show__actions actions'])["+i+"]").text
        lines = right_menu_list.split("\n")
        manage_link = lines[0]
        show_planner_link = lines[1]
        ones_link = lines[2]
        financials_link = lines[3]
        public_archive = lines[4]
        assert manage_link and show_planner_link and ones_link and financials_link and public_archive, "Something is missed"

    def filter_show_by_status(self, filter):
        time.sleep(5)
        self.driver.find_element(*ManageShowsLocators.FILTER_BUTTON).click()
        time.sleep(2)
        self.driver.find_element(*ManageShowsLocators.SELECT_ALL).click()
        self.driver.find_element(By.XPATH, f"//input[@value='{filter}']/parent::div[contains(@class, 'ui-checkbox')]").click()
        self.driver.find_element(*ManageShowsLocators.APPLY_BUTTON).click()

    def only_shows_of_filtered_status_displaying(self,filter):
        last_line_y = int(lines_height) - 300
        for i in range (0, last_line_y):
            line = self.driver.find_element(By.XPATH, "//div[@style='transform: translateY("+str(i)+"px);']/child::div")
            cards_qty_first_line = line.get_attribute('childElementCount')
            for show in range(1, int(cards_qty_first_line)+1):
                show_status_code = self.driver.find_element(By.XPATH, f"(//div[@class='status__label'])["+str(show)+"]").text
                time.sleep(2)
                assert show_status_code == filter, f"Statuses are not filtered. '{filter}' is expected, but '{show_status_code}' is displayed"
            i+=300


    def header_counters_calculation(self, filter):
        header_counter_of_selected_filter = self.driver.find_element(By.XPATH, f"//div[@class='header__counters']/descendant::div[contains(text(), '{filter}')]").text
        header = header_counter_of_selected_filter.split(" ")
        shows_of_selected_filter_qty = header[1]
        assert int(shows_of_selected_filter_qty) == int(shows_qty), "Qty of cards is different with qty displayed in header"

    def open_manage_show_page(self):
        self.driver.find_element(By.XPATH, "(//a[contains(text(),'Manage')])["+i+"]").click()
        time.sleep(20)
    
    def manage_show_page_title(self):
        time.sleep(15)
        edit_show_header = self.driver.find_element(*ManageShowsLocators.EDIT_SHOW_TITLE).get_attribute('innerText')
        assert contains(edit_show_header,"Edit Show"), "Wrong page is displayed"

    def name_of_open_show(self):
        show_title_in_manage_menu = self.driver.find_element(*ManageShowsLocators.SHOW_TITLE_MANAGE).get_attribute('innerText')
        assert show_title_in_manage_menu == show_code, f"another show was opened to manage, expected '{show_title_in_manage_menu}', but '{show_code}' is opened"

    def open_show_ones_page_from_show_card(self):
        self.driver.find_element(By.XPATH, "(//a[contains(text(),'Ones')])["+i+"]").click()
        time.sleep(15)
    
    def check_show_quota_ui_displaying(self):
        show_quota = self.driver.find_element(*ManageShowsLocators.SHOW_ONES_QUOTA_PAGE)
        assert show_quota.is_displayed, "Show Quota UI os not displayed on the page"

    def check_show_code_preselected(self):
        show_code_preselected = self.driver.find_element(*ManageShowsLocators.PRESELECTED_SHOW_CODE).get_attribute('innerText')
        assert show_code_preselected == show_code, f"another show was selected for ones. '{show_code_preselected}' is expected, but '{show_code}' is opened"

    def open_financials_page_from_show_card(self):
        self.driver.find_element(By.XPATH, "(//a[contains(text(),'Financials')])["+i+"]").click()
        time.sleep(15)

    def check_show_code_in_url(self):
        current_page = self.driver.current_url
        assert show_code in current_page, f"Financial of wrong show is opened. '{current_page}' doesn't contain '{show_code}'"

    def open_create_show_page(self):
        time.sleep(5)
        self.driver.find_element(*ManageShowsLocators.CREATE_SHOW_BUTTON).click()
        time.sleep(20)



    




