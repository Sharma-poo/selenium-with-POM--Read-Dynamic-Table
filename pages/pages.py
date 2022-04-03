""" Pages """
from drivers.drivers import WebdriverFactory
from page_objects import page_tables


class GetTable(WebdriverFactory):
    """Get table.

    """

    def __init__(self):
        self.driver = WebdriverFactory.getWebDriverInstance(self)

    def get_table(self):
        """Get table data.

        :return:
        """
        table = self.driver.find_element_by_xpath(page_tables.dyamic_table)
        print("table", table)
        columns = self.driver.find_elements_by_xpath(page_tables.columns)
        print("Number of columns in the table: ", len(columns))
        table_rows = self.driver.find_elements_by_xpath(page_tables.table_rows)
        print("Number table rows: ", len(table_rows))
        print("Data - ")
        print([row.text for row in table_rows])
        table_columns = self.driver.find_elements_by_xpath(
            page_tables.table_colums_headers
        )
        print("Number of columns: ", len(table_columns))
        print([header.text for header in table_columns])
        self.driver.close()


obj = GetTable()
obj.get_table()
