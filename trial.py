from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 800))
# display.start()
browser = webdriver.Chrome('/home/marlabs/Downloads/chromedriver')

def call_search_engine_google(browser):
      browser.get("http://www.google.com")
      linkList = []
      # driver.get(url)


      input_element = browser.find_element_by_name("q")
      input_element.send_keys("abcd")
      input_element.submit()
      i = 0
      while i<1:
          nxt_page = browser.find_elements_by_class_name('pn')
          if len(nxt_page) != 0:
              if len(nxt_page) == 1:
                  browser.execute_script('arguments[0].scrollIntoView()', nxt_page[0])
                  nxt_page[0].click()
                  # self.get_page_source(browser.page_source)
              else:
                  browser.execute_script('arguments[0].scrollIntoView()', nxt_page[1])
                  nxt_page[1].click()
                  # self.get_page_source(browser.page_source)
              # time.sleep(10)
          i+=1
      # while True:
      #     elm = browser.find_elements_by_class_name('pn')
      #     # if 'inactive' in elm.get_attribute('class'):
      #     #     break;
      #     elm.click()

      # RESULTS_LOCATOR = "//h3[@class='r']/a[@href]"
      #
      # WebDriverWait(browser, 10).until( EC.presence_of_element_located((By.ID, "resultStats")))
      #
      # page_results = browser.find_elements(By.XPATH, RESULTS_LOCATOR)
      #
      # for item in page_results:
      #     print item.get_attribute("href")
      #     print item.text
      # # browser.quit()
      import sys
      sys.exit()

call_search_engine_google(browser)
