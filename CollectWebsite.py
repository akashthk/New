# from googlesearch import search
import csv
import pandas as pd
import re
from webtreater import WebsiteTreat
from selenium import webdriver
from seleniumCode import seleniumfile

def main():
    # browser = webdriver.Chrome('/home/marlabs/Downloads/chromedriver')
    urlList, input, keyword = input_query()
    # input = input.strip()

    saveListtoCSV(urlList, 'complete_url_list', 'all_website')
    MostLikelyWebsites(urlList, input, keyword)

    # open_csv()
def input_query():
    # urlList = []
    i = 0
    ip=raw_input("What would you like to search for? ")
    keyword=raw_input("What keyword are you looking for? ")
    keyword = keyword.split(',')
    a = seleniumfile(ip)
    urlList =  a.call_search_engine_google()
    # for url in search(ip,num=50, start=0, stop=500, pause =10):
    #     i+=1
    #     print i
    #     print url
    #     urlList.append(url)
    return urlList, ip, keyword

def MostLikelyWebsites(your_list, ip,keyword):
        print "generating MostLikelyWebsites"
        core_URL_list = []
        webtreatobj = WebsiteTreat()
        for url in your_list:
            if url!=None:
                core_URL= webtreatobj.Extract_Core_URL_content(url)
                if core_URL:
                    for i in range(len(keyword)):
                        if keyword[i] in core_URL:
                            core_URL_list.append(webtreatobj.Extract_Core_URL(url))
                    core_URL_list = list(set(core_URL_list))
        saveListtoCSV(core_URL_list,'core_URL_list','Most Likely Wbesite')

def open_csv(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list


def MakeWord(word):
    return word.split()

def saveListtoCSV(list,file_name,column_header):
    df = pd.DataFrame(list, columns=[column_header])
    df.to_csv(file_name+'.csv', index=False)


if __name__ == "__main__":
    main()
