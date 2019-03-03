# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:37:00 2019
@author: harsh
"""
try :
    import requests
    from bs4 import BeautifulSoup
    from wordcloud import WordCloud,STOPWORDS
    import matplotlib.pyplot as plt
    from nltk.corpus import stopwords
    import re
    import os
    import time
except ImportError:
    print ("Library not found")
def Get_html(url):
    if 'http://'in url or 'https://'in url:
        try:
            response = requests.get(url,verify=False)
            html = response.text.encode("utf-8")
            if str(html) is not None:
                return str(html)
            else:
                    pass
        except requests.exceptions.ConnectionError as e:
            print ("connection not establised")
            print(e)
            html = "connection not establised"
    else:
        try:
            url = 'http://'+url
            response = requests.get(url,verify=False)
            html = response.text.encode("utf-8")
            if str(html) is not None:
                return str(html)
            else:
                pass
        except requests.exceptions.ConnectionError as e:
            print ("connection not establised")
            print(e)
            html = "connection not establised"
def cleaning_html(html):
    if html is not None:
        text_val = BeautifulSoup(html)
        for script in text_val(["script","style"]):
            script.decompose()
        cleantext_html = ' '.join(text_val.stripped_strings)
        cachedStopWords = set(stopwords.words("english"))
        cleantext_html = cleantext_html.lower()
        cleantext_html = re.sub('\W+',' ',cleantext_html)#removing spsl character
        cleantext_html = re.sub("^\d+\s|\s\d+\s|\s\d+$"," ",cleantext_html)#removing words ending with number
        cleantext_html = re.sub(r"(^|\W)\d+","",cleantext_html)#removing words starting with number
        cleantext_html = re.sub(r'\b\d+(?:\.\d+)?\s+',' ',cleantext_html)#removing numbers
        cleantext_html = re.sub(r'^[^a-zA-Z]',r' ',cleantext_html)#non words
        cleantext_html = ' '.join(word for word in cleantext_html.split(' ') if len(word) >1)
        cleantext_html = ' '.join([word for word in cleantext_html.split() if word not in cachedStopWords])
        return cleantext_html
    else:
        pass
def word_count(cleantext_html):
    if cleantext_html is not None:
        counts = dict()
        words =cleantext_html.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        final_count = dict((key_count, value_count) for key_count, value_count in counts.items() if value_count > 1)
        return(final_count)
    else:
        pass
def word_cloud(cleantext_html):
    if cleantext_html is not None:
        stopwords = set(STOPWORDS)
        wc = WordCloud(width =800,
                       height = 800,
                       background_color = 'white',
                       max_words=20,
                       stopwords = stopwords,
                       min_font_size =10
                       ).generate(cleantext_html)
        return wc
    else:
        pass
def save_img(wc):
    if wc is not None:
        plt.figure(figsize = (8,8),facecolor =None)
        plt.imshow(wc)
        plt.axis("off")
        plt.tight_layout(pad =0)
        if os.path.exists("image_data_store"):
            if os.path.exists("image_data_store/result.png"):
                plt.savefig('image_data_store/result_{}.png'.format(int(time.time())))
            else:
                plt.savefig('image_data_store/result.png')
        else:
            os.mkdir("image_data_store")
            if os.path.exists("image_data_store/result.png"):
                plt.savefig('image_data_store/result_{}.png'.format(int(time.time())))
            else:
                plt.savefig('image_data_store/result.png')
        plt.show()
    else:
        pass
def save_file(html):
    if html is not None:
        if os.path.exists("text_data_store"):
            if os.path.exists("text_data_store/website_html_data.txt"):
                with open('text_data_store/website_html_data{}.txt'.format(int(time.time())),'w') as f:
                    f.write("%s\n" %html)
            else:
                with open('text_data_store/website_html_data.txt','w') as f:
                    f.write("%s\n" %html)
        else:
            os.mkdir("text_data_store")
            if os.path.exists("text_data_store/website_html_data.txt"):
                with open('text_data_store/website_html_data{}.txt'.format(int(time.time())),'w') as f:
                    f.write("%s\n" %html)
            else:
                with open('text_data_store/website_html_data.txt','w') as f:
                    f.write("%s\n" %html)
    else:
        pass
def main(url):
    html = Get_html(url)
    save_file(html)
    cleantext_html = cleaning_html(html)
    xyz = word_count(cleantext_html)
    wc = word_cloud(cleantext_html)
    save_img(wc)
    return xyz
