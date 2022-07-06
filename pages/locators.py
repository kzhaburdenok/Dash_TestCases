from selenium.webdriver.common.by import By

class BasePageLocators():
    BANNER_CLOSE_ICON = (By.XPATH, "//span[@class='header-banner__close-button']")

class LoginPageLocators():
    USERNAME = (By.NAME, "UserName")
    PASSWORD = (By.NAME, "Password")
    REMEMBER_ME = (By.NAME, "RememberMe")
    LOG_IN_BTN = (By.XPATH, "//button[@type = 'submit']")

class HomePageLocators():
    RESOURCE_MANAGER = (By.XPATH, "//div[contains(text(), 'Resource Manager')]")
    FILES_UPLOAD = (By.XPATH, "//div[contains(text(), 'Upload')]")
    FILES_DOWNLOAD = (By.XPATH, "//div[contains(text(), 'Download')]")
    REPORTS_PACKS = (By.XPATH, "//div[contains(text(), 'P&L Packs')]")
    IDL_COST_CONTROLLER = (By.XPATH, "//div[contains(text(), 'IDL Cost')]")
    BUDGETS_CONTROLLER = (By.XPATH, "//div[contains(text(), 'Budgets & KPI')]")
    IDL_DEPT_ONES = (By.XPATH, "//div[contains(text(), 'IDL Dept. Ones')]")
    DL_DEPT_ONES = (By.XPATH, "(//div[contains(text(), 'DL Dept. Ones')])[2]") 
    SHOW_ONES = (By.XPATH, "//div[contains(text(), 'Show Ones')]")
    MANAGE_SHOWS = (By.XPATH, "//div[contains(text(), 'Manage Shows')]")
    CREATE_SHOW = (By.XPATH, "//div[contains(text(), 'Create New Show')]")
    MANAGE_PROJECT = (By.XPATH, "//div[contains(text(), 'Manage Project')]")
    CREATE_NEW_PROJECT = (By.XPATH, "//div[contains(text(), 'Create New Project')]")
    NOTIFICATION_CENTER = (By.XPATH, "//div[contains(text(), 'Notification Center')]")
    MANAGE_SITES_PERMISSIONS = (By.XPATH, "//div[contains(text(), 'Manage Sites Permissions')]")
    USERS = (By.XPATH, "//div[contains(text(), 'Users')]")
    CREATE_NEW_USER = (By.XPATH, "//div[contains(text(), 'Create New User')]")
    CONTACT_ADMIN = (By.XPATH, "//div[contains(text(), 'Contract Admin')]")
    LOGS = (By.XPATH, "//div[contains(text(), 'Logs')]")

 
class ResourceManagerLocators():    
    RESOURCE_MNG_DASHBOARD_TITLE = (By.XPATH, "//div[@class='main-title']")
    RESOURCE_MNG_DASHBOARD_TEXT = (By.XPATH, "//div[@class='dummy']")

class UploadDataLocators():
    UPLOAD_TITLE = (By.XPATH, "//div[@class='active']")

class DownloaddataLocators():
    DOWNLOAD_TITLE = (By.XPATH, "//div[@class='active']")

class ReportsLocators():
    PACKS_TITLE = (By.XPATH, "//div[@class='main-title']")

class IdlCostLocators():
    COST_TITLE = (By.XPATH, "//div[@class='main-title']")

class BudgetsLocators():
    BUDGETS_TITLE = (By.XPATH, "//div[@class='main-title']")

class IdlDeptOnesLocators():
    IDL_DEPT_ONES_TITLE = (By.XPATH, "//div[@class='main-title']") 

class DlDeptOnesLocators():
    DL_DEPT_INES_TITLE = (By.XPATH, "//div[@class='main-title']")  

class ShowOnesLocators():
    SHOW_ONES_TITLE = (By.XPATH, "//div[@class='main-title']")

class ManageShowsLocators():
    MANAGE_SHOWS_TITLE = (By.XPATH, "//div[@class='header__title']")
    SHOW_CARD = (By.XPATH, "//div[@class='show shows__item']")
    MANAGE_SHOW_HEADER = (By.XPATH, "//div[@class='header__title']")
    MANAGE_SHOWS_DATA_PAGE = (By.XPATH, "//div[@class='VDataTable page-mode full-page scrollable']")
    FILTER_BUTTON = (By.XPATH, "//button[contains(@class, 'v-filter__toggle')]")
    SELECT_ALL = (By.XPATH, "//li[contains(@class, 'select-all')]")
    APPLY_BUTTON = (By.XPATH, "//div[contains(@class, 'header__btn_apply')]/child::div[contains(@class, 'VButton-block')]")
    SHOWS_MIN_HEIGHT = (By.XPATH, "//div[contains(@style, 'min-height')]")
    SHOWS_LINES_ON_THE_TOP = (By.XPATH, "//div[@class='vue-recycle-scroller__item-wrapper']")


    SHOW_TITLE_MANAGE = (By.XPATH, "//div[contains(text(), 'Code')]/following-sibling::div[contains(@class, '')]")

    PRESELECTED_SHOW_CODE = (By.XPATH, "//div[@class ='Vheader__show']")
    CREATE_SHOW_BUTTON = (By.XPATH, "//div[contains(@class, 'header__btn_create')]")
    MANAGE_SHOW_TABS_LIST = (By.XPATH, "//ul[@class='VTab__controls']")
    SHOW_ONES_QUOTA_PAGE = (By.XPATH, "//div[@class='show-ones-quota']")

type = "Awarded"
category = "Episodic"
status = "Active"
show_currency = "GBP"
location = "London (MPC-EPI)"
primary_producer = "tobias-wi"
executive_producer = "peter-jo"
class CreateShowInputsLocators():
    MANAGE_ACTIVE_TAB = (By.XPATH, "//li[contains(@class, 'VTab__btn_active')]")
    BID_WEEKS_EMPTY_TAB = (By.XPATH, "//div[@class='empty-tab']")
    UPLOADER_SELECTOR_BID_WEEKS_TAB = (By.XPATH, "//div[@class='uploader__selector']")
    BID_WEEKS_TAB = (By.XPATH, "//li[contains(@class, 'VTab__btn_bidWeeks')]")
    EDIT_SHOW_TITLE = (By.XPATH, "//div[@class='edit-show__header header']")
    EDIT_SHOW_BODY = (By.XPATH, "//div[@class='edit-show__body']")
    CODE_FIELD = (By.XPATH, "//div[contains(text(), 'Code')]/following-sibling::div/descendant::span[@class='VInputFake__label']")
    CODE_FIELD_INPUT = (By.XPATH, "//div[contains(text(), 'Code')]/following-sibling::div/descendant::input")
    TYPE_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Type')]/following-sibling::div/descendant::span[@class='input-group__input__content']")
    TYPE_DROPDOWN_SELECTION = (By.XPATH, "//li/a[contains(text(), '" + type + "')]")
    CATEGORY_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Category')]/following-sibling::div")
    CATEGORY_DROPDOWN_SELECTION = (By.XPATH, "//li/a[contains(text(), '"+category+"')]")
    AMOUNT_OF_ASSERTS_FIELD = (By.XPATH, "//div[contains(text(), 'Amount of Assets')]/following-sibling::div/descendant::span[@class='VInputFake__label']")
    AMOUNT_OF_ASSERTS_FIELD_INPUT = (By.XPATH, "//div[contains(text(), 'Amount of Assets')]/following-sibling::div/descendant::input")
    STATUS_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Status')]/following-sibling::div")
    STATUS_DROPDOWN_SELECTION = (By.XPATH, "//li/a[contains(text(), '"+ status +"')]")
    AMOUNT_OF_SHOTS_FIELD = (By.XPATH, "//div[contains(text(), 'Amount of Shots')]/following-sibling::div/descendant::span[@class='VInputFake__label']")
    AMOUNT_OF_SHOTS_FIELD_INPUT = (By.XPATH, "//div[contains(text(), 'Amount of Shots')]/following-sibling::div/descendant::input")
    COLOR_PICKER = (By.XPATH, "//div[@class='VColorPicker__toggle toggle']")
    HEX_COLOR_INPUT = (By.XPATH, "//div[@class='cp-chrome__tab tab tab_hex']/descendant::input[@class='cp-input__input']")
    CONFIRM_COLOR_BUTTON = (By.XPATH, "//div[contains(@class, 'picker__btn_confirm')]")
    START_DATE_CALENDAR_FIELD = (By.XPATH, "//div[contains(text(), 'Start Date')]/following-sibling::div[contains(@class, 'input-group__input_date-picker')]")
    END_DATE_CALENDAR_FIELD = (By.XPATH, "//div[contains(text(), 'End Date')]/following-sibling::div[contains(@class, 'input-group__input_date-picker')]")
    LIST_OF_DATES = (By.XPATH, "//table[@class='mx-table mx-table-date']/tbody//td[@class!='cell not-current-month']")
    LIST_OF_PERIOD_START_DATES = (By.XPATH, "//table[@class='mx-table mx-table-date']/tbody//td[@class!='cell not-current-month disabled' and @class !='cell disabled' and @class !='cell today disabled']")
    CONFIRM_CALENDAR = (By.XPATH, "//button[@class='mx-btn mx-datepicker-btn-confirm']")
    ARTIST_FIELD = (By.XPATH, "//div[contains(text(), 'Artist') and not(contains(text(), 'Key'))]/following-sibling::div/descendant::span[@class='VInputFake__label']")
    ARTIST_FIELD_INPUT = (By.XPATH, "//div[contains(text(), 'Artist') and not(contains(text(), 'Key'))]/following-sibling::div/descendant::input")
    KEY_ARTIST_FIELD = (By.XPATH, "//div[contains(text(), 'Key Artist')]/following-sibling::div/descendant::span[@class='VInputFake__label']")
    KEY_ARTIST_FIELD_INPUT = (By.XPATH, "//div[contains(text(), 'Key Artist')]/following-sibling::div/descendant::input")
    LEAD_FIELD = (By.XPATH, "//div[contains(text(), 'Lead')]/following-sibling::div/descendant::span[@class='VInputFake__label']")
    LEAD_FIELD_INPUT = (By.XPATH, "//div[contains(text(), 'Lead')]/following-sibling::div/descendant::input")
    DL_FIELD = (By.XPATH, "//div[contains(text(), 'DL')]/following-sibling::div/descendant::span[@class='VInputFake__label']")
    DL_FIELD_INPUT = (By.XPATH, "//div[contains(text(), 'DL')]/following-sibling::div/descendant::input")
    SHOW_CURRENCY_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Show Currency')]/following-sibling::div")
    SHOW_CURRENCY_DROPDOWN_SELECTION = (By.XPATH, "//li/a[contains(text(), '"+ show_currency +"')]")
    AWARDS_EST_FIELD = (By.XPATH, "//div[contains(text(), 'Awards Est')]/following-sibling::div/descendant::span[@class='VInputFake__label']")
    AWARDS_EST_INPUT = (By.XPATH, "//div[contains(text(), 'Awards Est')]/following-sibling::div/descendant::input")
    LOCATION_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Primary')]/following-sibling::div")
    LOCATION_DROPDOWN_SELECTION = (By.XPATH, "//li/a[contains(text(), '"+ location +"')]")
    SHOW_INPUTS_TAB = (By.XPATH, "//span[contains(text(),'Show Inputs')]/ancestor::div[@class='tabTitle']")
    AVG_ARTIST_DAY_RATES_TAB = (By.XPATH, "//span[contains(text(),'Avg Artist')]/ancestor::div[@class='tabTitle']")
    SHOW_INPUTS_UI = (By.XPATH, "//div[contains(@class,'show-tab_show-inputs')]")
    PRIMARY_PRODUCER_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Primary Producer')]/following-sibling::div")
    PRIMARY_PRODUCER_DROPDOWN_SELECTION = (By.XPATH, "//li/a[contains(text(), '"+ primary_producer +"')]")
    EXECUTIVE_PRODUCER_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Executive Producer')]/following-sibling::div")
    EXECUTIVE_PRODUCER_DROPDOWN_SELECTION = (By.XPATH, "//li/a[contains(text(), '"+ executive_producer +"')]")
    COLOUR_AVG_ARTIST = (By.XPATH, "//div[contains(text(), 'Colour')]")
    COLOUR_SENIOR_FIELD = (By.XPATH, "(//div[contains(text(), 'Colour')]/following-sibling::div/descendant::span[@class='VInputFake__label'])[2]")
    COLOUR_SENIOR_FIELD_INPUT = (By.XPATH, "//div[contains(text(), 'Colour')]/following-sibling::div/descendant::input")
    CREATE_SHOW_SAVE_BUTTON = (By.XPATH, "//div[contains(@class, 'footer__btn_save')]")
    LIST_OF_NOTIFICATIONS = (By.XPATH, "//div[@class='toast toast-warning']")
    MANAGE_SHOW_TAB_TITLE_1 = (By.XPATH, "//div[@class='tabTitle']")
    MANAGE_SHOW_TAB_TITLE_2 = (By.XPATH, "//span[@class='tab-title']")
    



class CreateNewShowLocators():
    CREATE_NEW_SHOW_TITLE = (By.XPATH, "//div[@class='header__title']")

class ManageProjectsLocators():
    MANAGE_PROJECT_TITLE = (By.XPATH, "//div[@class='header__title']")

class CreateNewProjectLocators():
    CREATE_PROJECT_TITLE = (By.XPATH, "//div[@class='main-title']")

class NotificationCenterLocators():
    NOTIFICATION_CENTER_TITLE = (By.XPATH, "//div[@class='main-title']")

class ManageSitePermissionsLocators():
    MANAGE_SITE_PERMISSIONS_TITLE = (By.XPATH, "//div[@class='main-title']")

class UserLocators():
    USERS_TITLE = (By.XPATH, "//div[@class='main-title']")

class CreateNewUserLocators():
    CREATE_NEW_USER_TITLE = (By.XPATH, "//div[@class='main-title']")

class ContactAdminLocators():
    CONTACT_ADMIN_TITLE = (By.XPATH, "//div[@class='main-title']")
    CONTENT_MESSAGE = (By.XPATH, "//div[@class='ContractAdmin__content__message']")

class LogsLocators():
    LOGS_TITLE = (By.XPATH, "//div[@class='main-title']")