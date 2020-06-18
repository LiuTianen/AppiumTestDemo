from selenium.webdriver.common.by import By
from common.base_page import BasePage

class all_stock_page(BasePage):
    _item_name = (By.ID,"com.xueqiu.android:id/item_name")
    _back = (By.ID,"com.xueqiu.android:id/back")
    _current_price  =(By.ID,"com.xueqiu.android:id/stock_current_price")

    def chek_one(self):
        self.find_elements(self._item_name)[0].click()


    def get_current_price(self):
        return str(self.driver.find_elements("com.xueqiu.android:id/current_price")[0].text)

    def back(self):
        self.find_element(self._back).click()
        return self