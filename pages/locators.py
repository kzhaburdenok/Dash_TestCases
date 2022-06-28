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
    EDIT_SHOW_TITLE = (By.XPATH, "//div[@class='edit-show__header header']")
    SHOW_TITLE_MANAGE = (By.XPATH, "//div[contains(text(), 'Code')]/following-sibling::div[contains(@class, '')]")
    MANAGE_ACTIVE_TAB = (By.XPATH, "//li[contains(@class, 'VTab__btn_active')]")
    PRESELECTED_SHOW_CODE = (By.XPATH, "//div[@class ='Vheader__show']")
    CREATE_SHOW_BUTTON = (By.XPATH, "//div[contains(@class, 'header__btn_create')]")
    MANAGE_SHOW_TABS_LIST = (By.XPATH, "//ul[@class='VTab__controls']")
    MANAGE_SHOW_TAB_TITLE_1 = (By.XPATH, "//div[@class='tabTitle']")
    MANAGE_SHOW_TAB_TITLE_2 = (By.XPATH, "//span[@class='tab-title']")
    BID_WEEKS_TAB = (By.XPATH, "//li[contains(@class, 'VTab__btn_bidWeeks')]")
    BID_WEEKS_EMPTY_TAB = (By.XPATH, "//div[@class='empty-tab']")
    UPLOADER_SELECTOR_BID_WEEKS_TAB = (By.XPATH, "//div[@class='uploader__selector']")
    CREATE_SHOW_SAVE_BUTTON = (By.XPATH, "//div[contains(@class, 'footer__btn_save')]")
    LIST_OF_NOTIFICATIONS = (By.XPATH, "//div[@class='toast toast-warning']")

    

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