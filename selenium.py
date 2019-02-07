from selenium import webdriver
import re
browser = webdriver.Chrome('/home/marlabs/Downloads/chromedriver')
# driver.get('https://duckduckgo.com/html?q=python&t=h_&ia=web')

results_url = "https://duckduckgo.com/html?q=paralegal&t=h_&ia=web"
browser.get(results_url)
results = browser.find_elements_by_id('links')
num_page_items = len(results)
for i in range(num_page_items):
    print(results[i].text)
    # print(len(results))
while True:
    nxt_page = browser.find_element_by_class_name('btn--alt')
    if nxt_page:
        browser.execute_script('arguments[0].scrollIntoView();', nxt_page)
        nxt_page.click()
