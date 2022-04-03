""" Without id
 Try pytest for all the test data"""
from drivers.drivers import WebdriverFactory
import page_objects


class checkElement:

    def __init__(self):
        self.driver = WebdriverFactory.getWebDriverInstance(self)

    def get_data(self):
        """Get table data.

        :return:
        """
        elem = self.driver.find_element_by_css_selector(
            page_objects.page_element
        )
        print(elem.text)
        assert elem, "Element not found in the page!"
        self.driver.close()


obj = checkElement()
obj.get_data()
