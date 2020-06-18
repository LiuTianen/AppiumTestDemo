from app import App
import time
class TestSearch:

    def setup(self):
        self.search_page=App.start().to_search()

    def test_search_po(self):
        self.search_page.search("alibaba")
        assert self.search_page.get_current_price() > "10"
        self.search_page.close()
        time.sleep(10)


    def teardown(self):
        App.quit()







