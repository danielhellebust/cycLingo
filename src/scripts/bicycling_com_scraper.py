import time
from bs4 import BeautifulSoup

import requests

article_text = []


def get_bicycling_article_url():
    try:
        req = requests.get('https://www.bicycling.com/repair/')
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.findAll('a')
        sentence_list = []
        #print(text)
        for i in text:
            if i['href'][:8] == '/repair/' and len(i['href']) > 10:
                sentence_list.append(i['href'])

        return sentence_list

    except:
        pass

url_list = get_bicycling_article_url()

def get_bicycling_article(url):
    try:
        req = requests.get('https://www.bicycling.com' + url)
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.findAll('div')
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
        article_text.extend(get_bicycling_article(i))
        sleep(1)
    except:
        pass




with open('../bicycling_article_text.txt', 'a', encoding='utf-8') as f:
    for url in article_text:
        try:
            f.write("%s \r  " % url)
        except:
            pass

