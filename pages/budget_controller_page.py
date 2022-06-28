from .base_page import BasePage
from .locators import BudgetsLocators

class BudgetPage(BasePage):
    def user_see_budged_title(self):
        return True