
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:30:47 2019
@author: harsh
"""

# try :
from googlesearch import search
import pandas as pd
import os
import time
from word_cloud_ import main as wc
import urllib
import re
from urllib2 import urlparse
    #import tldextract
# except ImportError:
#     print ("Library not found")

values_websites = []
queries = []
def Downloading_data():
    a = 0
    global queries
    values_web = []
    while a != 'exit':
        query = str(raw_input("Enter the query to be searched \n"))
        if len(query) is 0:
            print ("Please enter the query to search\n")
        else:
            values_websites = validinputs(query)
            search_query = query.split("\"")
            search_query = [x for x in search_query if x is not None]
            for j in search_query:
                queries.append(j)
        if type(values_websites) == str:
            values_web.append(values_websites)
            break
        else:
            values_web.append(values_websites)

        a = str(raw_input('\nExit / For staying press enter.')).lower()
        if values_web == None:
            print("Exit without output")
    return values_web[0],queries

def validinputs(query):
    domain = str(raw_input("Enter the Domain to be searched \n1.USA\n2.UK\n3.Canada\n4.Austraila\n If search all domain leave null\n")).lower()
    if len(domain) == 0:
        values_websites = stringcheck(query,domain=0)
        return values_websites
    else :
        if isIntorString(domain):
            if int(domain)<5 and 0<int(domain):
                values_websites = stringcheck(query,domain)
                return values_websites
            elif 4<int(domain):
                print( "\nEnter a valid input")
                validinputs(query)
        else:
            values_websites = stringcheck(query,domain)
            return values_websites

def isIntorString(domain):
    for i in range(len(domain)):
        if domain[i].isdigit() != True:
            return False
    return True

def stringcheck(query,domain):

    dict_domain = {1:"com",'usa':"com",2:"co.uk",'uk':"co.uk",3:"ca",'canada':"ca",4:"com.au",'austraila':"com.au"}
    list_domain =["co.uk","com","ca","com.au"]
    i = 1
    global values_websites
    if domain != 0:
        if isIntorString(domain):
            domain = int(domain)
            domain = dict_domain[domain]
            values_websites = query_return(domain,query)
            return values_websites
        else:
            if domain in dict_domain.keys():
                domain = dict_domain[domain]
                values_websites = query_return(domain,query)
                return values_websites
            else:
                print( "\nEnter a valid Input")
                validinputs(query)
    else:
        try:
            for j in range( len(list_domain)):
                for result in search(query,tld = list_domain[j],num =100,stop=1,pause =7):
                    print (str(i) + "-->" + result)
                    i=i+1
                    values_websites.append(result)

            return values_websites
        except urllib.error.HTTPError as e:
            print("Service Unavailable")
            print(e)
            return "Service Unavailable"

def query_return(domain,query):
    try :
        global values_websites
        i = 1
        for result in search(query,tld = domain,num =100,stop=1,pause =7):
                    print (str(i) + "-->" + result)
                    i=i+1
                    if len(values_websites)==0:
                        values_websites.append(result)
                    else:
                        values_websites.append(result)


        return values_websites
    except urllib.error.HTTPError as e:
        print("Service Unavailable")
        print(e)
        return "Service Unavailable"

def second_data(values_websites,queries):
    second_final_list = []
    for link in values_websites:
        review = link.lower()
        review = review.split("://")
        review = re.split(r"[^a-zA-Z0-9\s]",review[1])
        review = list(set(review))
        x = 0
        for i in review:
            for word in queries:
                if x <4:
                    if i == word:
                        second_final_list.append(link)
            x = x+1
    return second_final_list



def cleaing_data(values_websites):
    new_data =[]
    a = len(values_websites)
    if a>0:
        for j in range(0, a):
            if returned_list[j] != None:
                url = values_websites[j]
                # review = urlparse(url)
                new_data.append(url)
    return new_data

def finding_string(new_data,queries):
    websitelistfinal = []
    a = len(new_data)
    for i in range(len(queries)):
        for j in range(a):
            if queries[i] in new_data[j]:
                websitelistfinal.append(new_data[j])
    print("\n\n\n\nThe Website which contains the queries as domain name.")
    if len(websitelistfinal) > 0:
        for i in range(len(websitelistfinal)):
            print (websitelistfinal[i])
        websitelistfinal = list(set(websitelistfinal))
    else :
        print ( "No values Found")
    return websitelistfinal


def output_saving(websitelistfinal,values_websites):
    df = pd.DataFrame(websitelistfinal)
    df.columns = ['Website Address']
    if os.path.exists("xls_file_data"):
        if os.path.exists("xls_file_data/output_website.xls"):
            df.to_excel("xls_file_data/output_website{}.xls".format(int(time.time())),index =False)
        else:
            df.to_excel("xls_file_data/output_website.xls",index =False)
    else:
        os.mkdir("xls_file_data")
        if os.path.exists("xls_file_data/output_website.xls"):
            df.to_excel("xls_file_data/output_website{}.xls".format(int(time.time())),index =False)
        else:
            df.to_excel("xls_file_data/output_website.xls",index =False)

    if os.path.exists("website_data"):
        if os.path.exists("website_data/website_data.txt"):
            with open('website_data/website_data{}.txt'.format(int(time.time())),'w') as f:
                f.write("Queries \n\n")
                for item in queries:
                    f.write("%s\n" %item)
                f.write("\n \n \nWebsite_final_list \n\n")
                for item in websitelistfinal:
                    f.write("%s\n" %item)
                f.write("\n \n \nValues_Websites \n\n")
                for item in values_websites:
                    f.write("%s\n" %item)
        else:
            with open('website_data/website_data.txt','w') as f:
                f.write("Queries \n\n")
                for item in queries:
                    f.write("%s\n" %item)
                f.write("\n \n \nWebsite_final_list \n\n")
                for item in websitelistfinal:
                    f.write("%s\n" %item)
                f.write("\n \n \nValues_Websites \n\n")
                for item in values_websites:
                    f.write("%s\n" %item)
    else:
        os.mkdir("website_data")
        if os.path.exists("website_data/website_data.txt"):
            with open('website_data/website_data{}.txt'.format(int(time.time())),'w') as f:

                f.write("Queries \n\n")
                for item in queries:
                    f.write("%s\n" %item)
                f.write("\n \n \nWebsite_final_list \n\n")
                for item in websitelistfinal:
                    f.write("%s\n" %item)
                f.write("\n \n \nValues_Websites \n\n")
                for item in values_websites:
                    f.write("%s\n" %item)
        else:
            with open('website_data/website_data.txt','w') as f:

                f.write("Queries \n\n")
                for item in queries:
                    f.write("%s\n" %item)
                f.write("\n \n \nWebsite_final_list \n\n")
                for item in websitelistfinal:
                    f.write("%s\n" %item)
                f.write("\n \n \nValues_Websites \n\n")
                for item in values_websites:
                    f.write("%s\n" %item)
def sending_url(websitelistfinal):
    lst = []
    for i in websitelistfinal:
        lst.append(wc(i))
    return lst
if __name__ == "__main__":
    returned_list,queries = Downloading_data()

    if "Service Unavailable" in returned_list:
        print("No values found")
    else:
        returned_list2 = cleaing_data(returned_list)
        returned_list3 = finding_string(returned_list2,queries)
        returned_list4 = second_data(returned_list,queries)
        returned_list5 = list(set(cleaing_data(returned_list4)))
        # lst = sending_url(returned_list5)
        # returned_list5 = [x for x in lst if x is not None]
        output_saving(returned_list3,returned_list)
