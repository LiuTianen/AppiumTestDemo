from app import App


class TestCheakAllstock:

    def setup(self):
        self.all_page = App.start().all_stock()

    def test_all(self):
        self.all_page.chek_one()
        assert self.all_page.get_current_price() > "10"
        self.all_page.back()

    def teardown(self):
        App.quit()
