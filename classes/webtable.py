class WebTable:
    def __init__(self, web_table):
        self.table = web_table

    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr")) - 1

    def get_column_count(self):
        return len(self.table.find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(), "columns": self.get_column_count()}

    def row_data(self, row_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")

        row_number = row_number + 1
        row = self.table.find_elements_by_xpath("//tr["+str(row_number)+"]/td")
        r_data = []
        for webElement in row:
            r_data.append(webElement.text)
        return r_data

    def column_data(self, column_number):
        col = self.table.find_elements_by_xpath("//tr/td["+str(column_number)+"]")
        r_data = []
        for webElement in col:
            r_data.append(webElement.text)
        return r_data

    def get_all_data(self):
        num_rows = len(self.table.find_elements_by_xpath("//tr")) - 1
        header = ["Form", "Plain", "Polite"]
        all_data = ["    |    ".join(header)]
        for i in range(2, num_rows):
            ro = [
                "**(" + self.table.find_element_by_xpath("//tr[" + str(i) + "]/th").text + ")**"
            ]
            num_columns = len(self.table.find_elements_by_xpath(f'//tr[{i}]/td')) + 1
            for j in range(1, num_columns):
                current = self.table.find_element_by_xpath("//tr["+str(i)+"]/td["+str(j)+"]").text
                if current:
                    ro.append(current)
            all_data.append(" | ".join(ro))
        return all_data

    def presence_of_data(self, data):
        data_size = len(self.table.find_elements_by_xpath("//td[normalize-space(text())='"+data+"']"))
        presence = False
        if data_size > 0:
            presence = True
        return presence

    def get_cell_data(self, row_number, column_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")
        row_number = row_number+1
        cell_data = self.table.find_element_by_xpath("//tr["+str(row_number)+"]/td["+str(column_number)+"]").text
        return cell_data
