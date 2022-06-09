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