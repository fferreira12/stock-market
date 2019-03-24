import unittest

from bovespa_data_source import BovespaDataSource


class TestBovespaDataSource(unittest.TestCase):

    def setUp(self):
        self.file_location = r"C:\Users\fferr\PycharmProjects\StockMarket\data\COTAHIST_A2019.TXT"
        self.bds = None

    def test_bovespa_dataource_creation(self):
        self.bds = BovespaDataSource(self.file_location)

    def test_open_file(self):
        self.bds = BovespaDataSource(self.file_location)
        self.bds._open_file()
        self.assertIsNotNone(self.bds._file)

    def test_read_line(self):
        self.bds = BovespaDataSource(self.file_location)
        self.bds._open_file()
        line_got = self.bds._read_line()
        line_real = "00COTAHIST.2019BOVESPA 20190322                                                                                                                                                                                                                      \n"
        self.assertEqual(line_got, line_real)

    def test_close_file(self):
        self.bds = BovespaDataSource(self.file_location)
        self.bds._open_file()
        self.bds._close_file()

    def test_get_code(self):
        self.bds = BovespaDataSource(self.file_location, "APPLE")
        code = self.bds._get_code()
        self.assertEqual(code, "AALR3")

    def test_get_price(self):
        self.bds = BovespaDataSource(self.file_location, "AALR3")
        price = self.bds._get_price()
        self.assertEqual(price, 13.25)

    def test_get_many_prices(self):
        self.bds = BovespaDataSource(self.file_location, "AALR3")
        price = 0
        for _ in range(50):
            price = self.bds._get_price()
        self.assertIsNot(price, 0)

    def tearDown(self):
        if self.bds._file:
            self.bds._close_file()
