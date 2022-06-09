from subprocess import CREATE_NEW_CONSOLE
import py
import pytest
from pages.base_page import BasePage
from pages.contact_admin_page import ContactAdminPage
from pages.dashboard_page import DashboardPage
from pages.locators import BudgetsLocators, ContactAdminLocators, CreateNewProjectLocators, CreateNewShowLocators, CreateNewUserLocators, DlDeptOnesLocators, DownloaddataLocators, HomePageLocators, IdlCostLocators, IdlDeptOnesLocators, LogsLocators, ManageProjectsLocators, ManageShowsLocators, ManageSitePermissionsLocators, NotificationCenterLocators, ReportsLocators, ResourceManagerLocators, ShowOnesLocators, UploadDataLocators, UserLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage

base_url = "http://10.94.6.100:50000"

class TestUserCanSwitchAmongTabs():
    @pytest.fixture(scope="module", autouse=True)
    def setup(self, driver):
        self.link = base_url + "/Login"
        page = LoginPage(driver, self.link)
        page.open()
        page.login_user()
        page = HomePage(driver, driver.current_url)
        page.user_is_logged_in()
        page.remove_banner() 

    def test_user_opens_resource (self,driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.RESOURCE_MANAGER)
        page.user_see_the_title(*ResourceManagerLocators.RESOURCE_MNG_DASHBOARD_TITLE)
        page = DashboardPage(driver, driver.current_url)
        page.user_see_dashboard_content_text()

    def test_user_opens_upload_files_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.FILES_UPLOAD)
        page.user_see_the_title(*UploadDataLocators.UPLOAD_TITLE)

    def test_user_opens_download_files_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.FILES_DOWNLOAD)
        page.user_see_the_title(*DownloaddataLocators.DOWNLOAD_TITLE)

    def test_user_opens_reports_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.REPORTS_PACKS)
        page.user_see_the_title(*ReportsLocators.PACKS_TITLE)
    
    def test_user_opens_idl_cost_controller_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.IDL_COST_CONTROLLER)
        page.user_see_the_title(*IdlCostLocators.COST_TITLE)

    def test_user_opens_budget_controller_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.BUDGETS_CONTROLLER)
        page.user_see_the_title(*BudgetsLocators.BUDGETS_TITLE)

    def test_user_opens_idl_dept_ones_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.IDL_DEPT_ONES)
        page.user_see_the_title(*IdlDeptOnesLocators.IDL_DEPT_ONES_TITLE)

    def test_user_opens_dl_dept_ones_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.DL_DEPT_ONES)
        page.user_see_the_title(*DlDeptOnesLocators.DL_DEPT_INES_TITLE)

    def test_user_opens_show_ones_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.SHOW_ONES)
        page.user_see_the_title(*ShowOnesLocators.SHOW_ONES_TITLE)

    def test_user_opens_manage_shows_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.MANAGE_SHOWS)
        page.user_see_the_title(*ManageShowsLocators.MANAGE_SHOWS_TITLE)

    def test_user_opens_create_new_show_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.CREATE_SHOW)
        page.user_see_the_title(*CreateNewShowLocators.CREATE_NEW_SHOW_TITLE)

    def test_user_opens_manage_projects_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.MANAGE_PROJECT)
        page.user_see_the_title(*ManageProjectsLocators.MANAGE_PROJECT_TITLE)
    
    def test_user_opens_create_new_project_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.CREATE_NEW_PROJECT)
        page.user_see_the_title(*CreateNewProjectLocators.CREATE_PROJECT_TITLE)

    def test_user_opens_notification_center_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.NOTIFICATION_CENTER)
        page.user_see_the_title(*NotificationCenterLocators.NOTIFICATION_CENTER_TITLE)

    def test_user_opens_manage_sites_permissions_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.MANAGE_SITES_PERMISSIONS)
        page.user_see_the_title(*ManageSitePermissionsLocators.MANAGE_SITE_PERMISSIONS_TITLE)

    def test_user_opens_users_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.USERS)
        page.user_see_the_title(*UserLocators.USERS_TITLE)

    def test_user_opens_create_user_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.CREATE_NEW_USER)
        page.user_see_the_title(*CreateNewUserLocators.CREATE_NEW_USER_TITLE)

    def test_user_opens_contact_admin_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.CONTACT_ADMIN)
        page.user_see_the_title(*ContactAdminLocators.CONTACT_ADMIN_TITLE)
        page = ContactAdminPage(driver, driver.current_url)
        page.user_see_admin_content_text()

    def test_user_opens_logs_page(self, driver):
        self.link = base_url + "/Home/Homepage"
        page = HomePage(driver, self.link)
        page.user_opens_the_page(*HomePageLocators.LOGS)
        page.user_see_the_title(*LogsLocators.LOGS_TITLE)