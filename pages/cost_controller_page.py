from .base_page import BasePage
from pages.locators import IdlCostLocators

class CostPage(BasePage):
    def user_see_idl_cost_title(self):
        return True