from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
import urllib2
from bs4 import BeautifulSoup
browser = webdriver.Chrome('/home/marlabs/Downloads/chromedriver')
from selenium.webdriver.support import expected_conditions as EC

# driver.get('https://duckduckgo.com/html?q=python&t=h_&ia=web')

class seleniumfile:
    def __init__(self,ip):
        self._ip = ip
        self.list_of_website = []


    def get_page_source(self, html_source):
        soup = BeautifulSoup(html_source)
        web_data = soup.prettify()
        name = soup.findAll("a", {"class": "result__url"})
        for n in name:
            self.list_of_website.append(self.iterator_f(n))


    def iterator_f(self,mydivs):
            reg = 'href="\s*.*\s*"'
            x =  re.findall(reg,str(mydivs))
            x = x[0].replace('href=', "")
            x = x.replace('"',"")
            x = x.strip()
            return x

    def call_search_engine(self):
        results_url = "https://duckduckgo.com/html?q="+self._ip+"l&t=h_&ia=web"
        browser.get(results_url)
        html_source = browser.page_source
        i = 0
        while i<10:
            nxt_page = browser.find_elements_by_class_name('btn--alt')
            if len(nxt_page) != 0:
                if len(nxt_page) == 1:
                    browser.execute_script('arguments[0].scrollIntoView()', nxt_page[0])
                    nxt_page[0].click()
                    self.get_page_source(browser.page_source)
                else:
                    browser.execute_script('arguments[0].scrollIntoView()', nxt_page[1])
                    nxt_page[1].click()
                    self.get_page_source(browser.page_source)
                # time.sleep(10)
            i+=1

        return self.list_of_website

    def call_search_engine_google(self):
        def get_website(browser):
            # print browser.page_source
            soup = BeautifulSoup(browser.page_source)
            links = soup.findAll("a")
            for link in links:
                self.list_of_website.append(link.get('href'))
            # RESULTS_LOCATOR = "//*[@id='rso']//h3/a"
            #
            # WebDriverWait(browser, 10).until( EC.presence_of_element_located((By.ID, "resultStats")))
            # # print browser.page_source
            # page_results = browser.find_elements_by_xpath("(//h3)[3]/a")
            # # print page_results
            # for item in page_results:
            #     print item.get_attribute("href")

        browser.get("http://www.google.com")
        linkList = []
        # driver.get(url)


        input_element = browser.find_element_by_name("q")
        input_element.send_keys(self._ip)
        input_element.submit()
        get_website(browser)
        i = 0
        while i<50:
            nxt_page = browser.find_elements_by_class_name('pn')
            if len(nxt_page) != 0:
                if len(nxt_page) == 1:
                    browser.execute_script('arguments[0].scrollIntoView()', nxt_page[0])
                    nxt_page[0].click()
                    get_website(browser)
                    # self.get_page_source(browser.page_source)
                else:
                    browser.execute_script('arguments[0].scrollIntoView()', nxt_page[1])
                    nxt_page[1].click()
                    get_website(browser)

                    # self.get_page_source(browser.page_source)

                time.sleep(random.uniform(0.5, 5.0))
            i+=1
        # browser.quit()
        return self.list_of_website
# // wait until the google page shows the result
        # myDynamicElement = (new WebDriverWait(browser, 10)).until(ExpectedConditions.presenceOfElementLocated(By.id("resultStats")))
        #
        # findElements = browser.findElements(By.xpath("//*[@id='rso']//h3/a"))
        #
        # # // this are all the links you like to visit
        # for (WebElement webElement : findElements)
        # {
        #     System.out.println(webElement.getAttribute("href"))
        # }
