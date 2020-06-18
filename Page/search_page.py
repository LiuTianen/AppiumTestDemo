from selenium.webdriver.common.by import By
from common.base_page import BasePage

class SearchPage(BasePage):

    _input_locator=(By.ID, "com.xueqiu.android:id/search_input_text")
    _name_locator=(By.ID, "com.xueqiu.android:id/name")
    _close = (By.ID, "com.xueqiu.android:id/action_close")
    _current_price =(By.ID ,"com.xueqiu.android:id/current_price")

    def search(self, keyword):
        self.find_element(self._input_locator).send_keys(keyword)
        self.find_elements(self._name_locator)[0].click()
        return self

    def get_current_price(self):
        return str(self.find_elements(self._current_price)[0].text)

    def close(self):
        self.find_element_and_click(self._close)
        return self
