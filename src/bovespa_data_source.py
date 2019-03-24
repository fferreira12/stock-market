from data_source import DataSource


class BovespaDataSource(DataSource):

    def __init__(self, file_location, code = "PETR4"):
        self._file_location = file_location
        self._file = None
        self._current_line = None
        self._code = code

    def next(self):
        pass

    def _open_file(self):
        self._file = open(self._file_location, "r", encoding="utf-8-sig")

    def _read_line(self):
        if not self._file:
            self._open_file()
        self._current_line = self._file.readline()
        return self._current_line

    def _close_file(self):
        self._file.close()

    def _get_code(self):

        code = self._current_line[12:24].strip()
        return code

    def _get_price(self):
        while not self._current_line or self._current_line[0:2] != "01" or self._get_code() != self._code:
            self._read_line()
        price = int(self._current_line[108:121]) / 100.00
        self._read_line() #goes to next line to prevent reading same line
        return price

