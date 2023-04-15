import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import requests

article_text = []


def get_velomati_article_url():
    sentence_list = []
    for i in range(0,57):
        try:
            req = requests.get(f'https://www.velominati.com/the-archives/page/{i}/')
            soup = BeautifulSoup(req.text, "html.parser")
            text = soup.findAll('div', {'class': 'post-wrapper'})

            #print(text)
            for i in text:
                url = i.findAll('a')
                for j in url:
                    #print(j['href'])
                    if j['href'][:34] != 'https://www.velominati.com/author/' \
                            and j['href'][-9:] != '#comments'\
                            and j['href'][:36] != 'https://www.velominati.com/category/':

                        if j['href'] not in sentence_list:
                            sentence_list.append(j['href'])

        except:
            pass
    return sentence_list


url_list  = get_velomati_article_url()

# with open('velomati_article_urls.txt', 'w') as f:
#     for url in url_list:
#         f.write("%s \r  " % url)
#


def get_velomati_article(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.findAll('div', {'class': 'post-content'})
        sentence_list = []
        #print(text)
        for i in text:
            body = i.findAll('p')
            for j in body:
                # filter out sentences that are too short
                body_text = j.text.encode('ascii', 'ignore').decode('ascii').replace('\n', ' ').strip()
                print(body_text)
                if len(body_text) > 60:
                    sentence_list.append(body_text+' ')

        print(len(sentence_list))
        return sentence_list


    except:
        pass

#get_velomati_article('https://www.velominati.com/la-vie-velominatus/route-finding/')
#
for i in url_list:
    print(i)
    try:
        article_text.extend(get_velomati_article(i))
        sleep(1)
    except:
        pass
#
#
#
#
with open('../velomati_article_text.txt', 'a', encoding='utf-8') as f:
    for url in article_text:
        try:
            f.write("%s \r  " % url)
        except:
            pass

