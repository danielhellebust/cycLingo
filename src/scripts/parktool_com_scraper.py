import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import requests

article_text = []
url_list = get_parktool_article_url()

def get_parktool_article_url():
    sentence_list = []
    for i in range(0, 18):
        try:
            req = requests.get(f'https://www.parktool.com/en-int/blog/repair-help/p{i}')
            soup = BeautifulSoup(req.text, "html.parser")
            text = soup.findAll('div', {'class': 'pure-u-2-3 repair-help-results-container-column'})

            #print(text)
            for i in text:
                url = i.findAll('a')
                for j in url:

                    if j['href'][36:49] == '/repair-help/' and len(j['href']) > 53:
                        sentence_list.append(j['href'])
        except:
            pass
    return sentence_list

def get_parktool_article(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.findAll('div', {'class': 'pure-u-2-3'})
        sentence_list = []
        #print(text)
        for i in text:
            body = i.findAll('p')
            for j in body:
                # filter out sentences that are too short
                body_text = j.text.encode('ascii', 'ignore').decode('ascii').replace('\n', ' ').strip()
                #print(body_text)
                if len(body_text) > 60:
                    sentence_list.append(body_text+' ')
        print(len(sentence_list))
        return sentence_list

    except:
        pass



for i in url_list:
    print(i)
    try:
        article_text.extend(get_parktool_article(i))
        sleep(1)
    except:
        pass




with open('../parktool_article_text.txt', 'a', encoding='utf-8') as f:
    for url in article_text:
        try:
            f.write("%s \r  " % url)
        except:
            pass

