import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OmnivoxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.implicitly_wait(10)

   
    def test_Open_and_check_title_on_omnivox_site(self):
        driver = self.driver
        driver.get("https://montrealcollege.omnivox.ca/Login/Account/Login?L=ANG")
        self.assertIn("Omnivox - Montreal College of Information Technology", driver.title)
       
    def test_home_page_title_on_omnivox_site(self):
        driver = self.driver
        driver.get("https://montrealcollege.omnivox.ca/Login/Account/Login?L=ANG") 
        self.assertIn("Montreal College of Information Technology", driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/a').text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()