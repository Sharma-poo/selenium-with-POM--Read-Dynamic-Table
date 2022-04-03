""" Drivers!"""
from selenium import webdriver


class WebdriverFactory:
    """Get the Chrome browser.

    """

    def getWebDriverInstance(self):
        # baseURL = 'https://demo.guru99.com/test/web-table-element.php'
        baseURL = "https://phptravels.com/demo/"
        driver = webdriver.Chrome(executable_path=r"/usr/bin/chromedriver")

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver
