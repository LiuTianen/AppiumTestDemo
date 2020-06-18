from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
from common.base_page import BasePage
from Page.search_page import SearchPage
from Page.all_stock_page import all_stock_page


class MainPage(BasePage):
    _search_locator = (By.ID, "com.xueqiu.android:id/home_search")
    _all_stock = (By.ID, "com.xueqiu.android:id/all_stock_tv")
    def to_search(self):
        #todo: too slow
        self.find_element_and_click(self._search_locator)
        return SearchPage(self.driver)

    def all_stock(self):
        self.find_element_and_click(self._all_stock)
        time.sleep(3)
        return all_stock_page(self.driver)
