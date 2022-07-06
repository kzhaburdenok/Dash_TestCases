from .locators import CreateShowInputsLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from datetime import date, timedelta
from operator import contains

code = "ATest" + str(random.randint(0,1000))
amount_of_asserts = "2"
amount_of_shots = "5"
show_color = '#' + format(random.randint(0,16777215), 'x')
start_date = date.today()
end_date = start_date + timedelta(days=10)
artist_split_value = random.randint(1,50)
key_artist_value = random.randint(1,50)
lead_value = 100 - artist_split_value - key_artist_value
dl_value = random.randint(1,100)
awards_est_value = random.randint(1,99999)
colour_senior = random.randint(1,2000)
print(dl_value)


class CreateShowPage(BasePage):

    def check_default_tab_manage_show(self):
        default_tab_name = self.driver.find_element(*CreateShowInputsLocators.MANAGE_ACTIVE_TAB).get_attribute('innerText')
        assert default_tab_name == "Show Stats", f"tab {default_tab_name} is active instead"
    
    def create_show_page_title_displaying(self):
        edit_show_header = self.driver.find_element(*CreateShowInputsLocators.EDIT_SHOW_TITLE).get_attribute('innerText')
        assert contains(edit_show_header,"Create Show"), "Wrong page is displayed"

    def check_bid_weeks_in_edit_mode(self):
        self.driver.find_element(*CreateShowInputsLocators.BID_WEEKS_TAB).click()
        time.sleep(2)
        uploader_selector = self.driver.find_element(*CreateShowInputsLocators.UPLOADER_SELECTOR_BID_WEEKS_TAB)
        assert uploader_selector.is_displayed, "Uploader selector is missed for Edit Mode"

    def check_bid_weeks_in_create_mode(self):
        self.driver.find_element(*CreateShowInputsLocators.BID_WEEKS_TAB).click()
        time.sleep(2)
        empty_tab = self.driver.find_element(*CreateShowInputsLocators.BID_WEEKS_EMPTY_TAB)
        assert empty_tab.is_displayed, "Tab is not empty for Create Mode"

    def enter_show_code(self):
        self.driver.find_element(*CreateShowInputsLocators.CODE_FIELD).click()
        self.driver.find_element(*CreateShowInputsLocators.CODE_FIELD_INPUT).send_keys(code)
        time.sleep(2)

    def save_show_button_click(self):
        self.driver.find_element(*CreateShowInputsLocators.CREATE_SHOW_SAVE_BUTTON).click()
        time.sleep(3)

    def select_show_type(self):
        self.driver.find_element(*CreateShowInputsLocators.TYPE_DROPDOWN).click()
        self.driver.find_element(*CreateShowInputsLocators.TYPE_DROPDOWN_SELECTION).click()
        time.sleep(2)

    def select_show_category(self):
        self.driver.find_element(*CreateShowInputsLocators.CATEGORY_DROPDOWN).click()
        self.driver.find_element(*CreateShowInputsLocators.CATEGORY_DROPDOWN_SELECTION).click()
        time.sleep(2)

    def enter_amount_of_assets(self):
        self.driver.find_element(*CreateShowInputsLocators.AMOUNT_OF_ASSERTS_FIELD).click()
        self.driver.find_element(*CreateShowInputsLocators.AMOUNT_OF_ASSERTS_FIELD_INPUT).send_keys(amount_of_asserts)
        time.sleep(2)

    def select_show_status(self):
        self.driver.find_element(*CreateShowInputsLocators.STATUS_DROPDOWN).click()
        self.driver.find_element(*CreateShowInputsLocators.STATUS_DROPDOWN_SELECTION).click()
        time.sleep(2)

    def enter_amount_of_shots(self):
        self.driver.find_element(*CreateShowInputsLocators.AMOUNT_OF_SHOTS_FIELD).click()
        self.driver.find_element(*CreateShowInputsLocators.AMOUNT_OF_SHOTS_FIELD_INPUT).send_keys(amount_of_shots)
        time.sleep(2)

    def enter_show_color(self):
        self.driver.find_element(*CreateShowInputsLocators.COLOR_PICKER).click()
        hex_color_input_field = self.driver.find_element(*CreateShowInputsLocators.HEX_COLOR_INPUT)
        hex_color_input_field.clear()
        hex_color_input_field.send_keys(show_color)
        self.driver.find_element(*CreateShowInputsLocators.CONFIRM_COLOR_BUTTON).click()
        time.sleep(2)

    def select_show_start_date(self):
        start_date_field = self.driver.find_element(*CreateShowInputsLocators.START_DATE_CALENDAR_FIELD)
        start_date_field.click()
        all_dates_available = self.driver.find_elements(*CreateShowInputsLocators.LIST_OF_DATES)
        for date in all_dates_available:
            if date.get_attribute('title') == str(start_date):
                date.click()
                self.driver.find_element(*CreateShowInputsLocators.CONFIRM_CALENDAR).click()
                break
        time.sleep(3)

    def select_show_end_date(self):
        end_date_field = self.driver.find_element(*CreateShowInputsLocators.END_DATE_CALENDAR_FIELD)
        end_date_field.click()
        all_dates_available = self.driver.find_elements(*CreateShowInputsLocators.LIST_OF_DATES)
        for date in all_dates_available:
            if date.get_attribute('title') == str(end_date):
                date.click()
                self.driver.find_element(*CreateShowInputsLocators.CONFIRM_CALENDAR).click()
                break
        time.sleep(3)

    def set_seniority_splits(self):
        self.driver.find_element(*CreateShowInputsLocators.ARTIST_FIELD).click()
        self.driver.find_element(*CreateShowInputsLocators.ARTIST_FIELD_INPUT).send_keys(artist_split_value)
        time.sleep(2)

        self.driver.find_element(*CreateShowInputsLocators.KEY_ARTIST_FIELD).click()
        self.driver.find_element(*CreateShowInputsLocators.KEY_ARTIST_FIELD_INPUT).send_keys(key_artist_value)
        time.sleep(2)

        self.driver.find_element(*CreateShowInputsLocators.LEAD_FIELD).click()
        self.driver.find_element(*CreateShowInputsLocators.LEAD_FIELD_INPUT).send_keys(lead_value)
        time.sleep(2)
        
        self.driver.find_element(*CreateShowInputsLocators.DL_FIELD).click()
        self.driver.find_element(*CreateShowInputsLocators.DL_FIELD_INPUT).send_keys(str(dl_value))
        time.sleep(2)

    def select_show_financial(self):
        self.driver.find_element(*CreateShowInputsLocators.SHOW_CURRENCY_DROPDOWN).click()
        self.driver.find_element(*CreateShowInputsLocators.SHOW_CURRENCY_DROPDOWN_SELECTION).click()
        time.sleep(2)

    def enter_show_awards_est(self):
        self.driver.find_element(*CreateShowInputsLocators.AWARDS_EST_FIELD).click()
        self.driver.find_element(*CreateShowInputsLocators.AWARDS_EST_INPUT).send_keys(str(awards_est_value))

    def select_show_location(self):
        global selected_location
        self.driver.find_element(*CreateShowInputsLocators.LOCATION_DROPDOWN).click()
        self.driver.find_element(*CreateShowInputsLocators.LOCATION_DROPDOWN_SELECTION).click()
        time.sleep(2)
        selected_location = self.driver.find_element(*CreateShowInputsLocators.LOCATION_DROPDOWN).text

    def switch_to_show_inputs_tab(self):
        self.driver.find_element(*CreateShowInputsLocators.SHOW_INPUTS_TAB).click()
        show_inputs_ui = self.driver.find_element(*CreateShowInputsLocators.SHOW_INPUTS_UI)
        time.sleep(2)
        assert show_inputs_ui.is_displayed, "Tab is not opened"

    def select_show_primary_producer(self):
        self.driver.find_element(*CreateShowInputsLocators.PRIMARY_PRODUCER_DROPDOWN).click()
        self.driver.find_element(*CreateShowInputsLocators.PRIMARY_PRODUCER_DROPDOWN_SELECTION).click()
        time.sleep(2)
    
    def select_show_executive_producer(self):
        self.driver.find_element(*CreateShowInputsLocators.EXECUTIVE_PRODUCER_DROPDOWN).click()
        self.driver.find_element(*CreateShowInputsLocators.EXECUTIVE_PRODUCER_DROPDOWN_SELECTION).click()
        time.sleep(2)

    def set_other_mandatory_fields(self):      
        if "London" in selected_location:
            self.driver.find_element(By.XPATH, "//div[contains(text(), 'London')]/following-sibling::div[contains(@class, 'input-group__input_date-picker')]").click()
            all_dates_available = self.driver.find_elements(*CreateShowInputsLocators.LIST_OF_PERIOD_START_DATES)
            for date in all_dates_available:
                date.click()
                self.driver.find_element(*CreateShowInputsLocators.CONFIRM_CALENDAR).click()
                break
            time.sleep(3)
        if "Berlin" in selected_location:
            self.driver.find_element(By.XPATH, "//div[contains(text(), 'Berlin')]/following-sibling::div[contains(@class, 'input-group__input_date-picker')]").click()
            all_dates_available = self.driver.find_elements(*CreateShowInputsLocators.LIST_OF_DATES)
            for date in all_dates_available:
                date.click()
                self.driver.find_element(*CreateShowInputsLocators.CONFIRM_CALENDAR).click()
                break
            time.sleep(3)
        if "Montreal" in selected_location:
            self.driver.find_element(By.XPATH, "//div[contains(text(), 'Montreal')]/following-sibling::div[contains(@class, 'input-group__input_date-picker')]").click()
            all_dates_available = self.driver.find_elements(*CreateShowInputsLocators.LIST_OF_DATES)
            for date in all_dates_available:
                date.click()
                self.driver.find_element(*CreateShowInputsLocators.CONFIRM_CALENDAR).click()
                break
            time.sleep(3)   

    def confirm_pop_ups_appearance_when_empty_show_saved(self):
        notifications = []

        with open("E:\\Automation\\Dash_smoke\\notifications_list.txt") as file:
            notifications = file.read().splitlines()

        list_of_notifications = len(self.driver.find_elements(*CreateShowInputsLocators.LIST_OF_NOTIFICATIONS))
        notifications_list = []
        for i in range(1, list_of_notifications+1):
            notification = self.driver.find_element(By.XPATH, "(//div[@class='toast toast-warning'])["+str(i)+"]").get_attribute('innerText')
            notifications_list.append(notification)

        assert notifications.sort() == notifications_list.sort(), "Displayed notifications are different from expected"

    def check_show_ui_displaying(self):
        edit_show_body = self.driver.find_element(*CreateShowInputsLocators.EDIT_SHOW_BODY)
        assert edit_show_body.is_displayed, "Create/Edit Show UI is not displayed on the page"

    def check_tabs_list(self):
        list_of_tabs = ['Show Stats', 'Show Inputs', 'Avg Artist Day Rates', 'Outsource Rates', 'Bid Weeks', 'Contract Value', 'Indirect Costs', 'Internal Bid']
        qty_tabs_1 = len(self.driver.find_elements(*CreateShowInputsLocators.MANAGE_SHOW_TAB_TITLE_1))
        qty_tabs_2 = len(self.driver.find_elements(*CreateShowInputsLocators.MANAGE_SHOW_TAB_TITLE_2))
        current_tabs_list = []
        for i in range(1, qty_tabs_1+1):
            tab_name = self.driver.find_element(By.XPATH, "(//div[@class='tabTitle'])["+str(i)+"]").get_attribute('innerText')
            current_tabs_list.append(tab_name)

        for i in range(1, qty_tabs_2+1):
            tab_name = self.driver.find_element(By.XPATH, "(//span[@class='tab-title'])["+str(i)+"]").get_attribute('innerText')
            current_tabs_list.append(tab_name)

        assert list_of_tabs.sort() == current_tabs_list.sort(), "Displayed List of tabs is different from expected list of tabs"

        


            

