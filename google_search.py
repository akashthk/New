import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class GoogleEveryFirstLink(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/marlabs/Downloads/chromedriver')
        self.driver.get("http://www.google.com")

    def test_Hover_Facebook(self):
        driver = self.driver
        self.assertIn("Google",driver.title)
        elem=driver.find_element_by_id("lst-ib")
        elem.clear()
        elem.send_keys("India")
        elem.send_keys(Keys.RETURN)
        page_counter=2
        links_counter=1
        wait = WebDriverWait(driver,20)
        wait.until(EC.element_to_be_clickable((By.XPATH,"(//h3[@class='r']/a)[" + str(links_counter) + "]")))
        pages=driver.find_elements_by_xpath("//*[@id='nav']/tbody/tr/td/a")
        elem1=driver.find_elements_by_xpath("//h3[@class='r']/a")
        print len(elem1)
        print len(pages)
        driver.maximize_window()
        for page in pages:
            for e in elem1:
                my_link = driver.find_element_by_xpath("(//h3[@class='r']/a)[" + str(links_counter) + "]")
                print my_link.text
                my_link.click()
                driver.back()
                links_counter+=1
            my_page = driver.find_element_by_xpath("//a[text() = '" + str(page_counter) + "']")
            my_page.click()
            page_counter+=1

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
