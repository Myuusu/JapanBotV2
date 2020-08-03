from selenium.common.exceptions import NoSuchElementException


class WebTable:
    def __init__(self, web_table):
        self.table = {
            "table": web_table,
            "rows": len(web_table.find_elements_by_xpath("tr")) - 1,
            "columns": len(web_table.find_elements_by_xpath("//tr[2]/td"))
        }

    def __getitem__(self, item):
        return self.table[item]

    def get_row_count(self):
        return len(self.table["table"].find_elements_by_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.table["table"].find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(), "columns": self.get_column_count()}

    def row_data(self, row_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        row_number = row_number + 1
        row = self.table["table"].find_elements_by_xpath(f'//tr[{str(row_number)}]/td')
        r_data = []
        for webElement in row:
            r_data.append(webElement.text)
        return r_data

    def column_data(self, column_number):
        col = self.table["table"].find_elements_by_xpath(f'//tr/td[{str(column_number)}]')
        r_data = []
        for webElement in col:
            r_data.append(webElement.text)
        return r_data

    def get_all_data(self, max_rows=None):
        if max_rows:
            num_rows = len(self.table["table"].find_elements_by_xpath("//tr")) - 1
            if max_rows < num_rows:
                num_rows = max_rows
        else:
            num_rows = len(self.table["table"].find_elements_by_xpath("//tr")) - 1
        header = ["Form", "Plain", "Polite"]
        all_data = [" | ".join(header)]
        for i in range(2, num_rows):
            ro = ["**(" + self.table["table"].find_element_by_xpath(f'//tr[{str(i)}]/th').text + ")**"]
            for j in range(1, len(self.table["table"].find_elements_by_xpath(f'//tr[{str(i)}]/td')) - 1):
                try:
                    ro.append(
                        self.table["table"].find_element_by_xpath(
                            f'//tr[{str(i)}]/td[{str(j)}]'
                        ).text
                    )
                except NoSuchElementException:
                    pass
            all_data.append(" | ".join(ro))
        return all_data

    def presence_of_data(self, data):
        data_size = len(self.table["table"].find_elements_by_xpath(f'//td[normalize-space(text())="{data}"]'))
        presence = False
        if data_size > 0:
            presence = True
        return presence

    def get_cell_data(self, row_number, column_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        row_number = row_number + 1
        cell_data = self.table["table"].find_element_by_xpath(f'//tr[{str(row_number)}]/td[{str(column_number)}]').text
        return cell_data
