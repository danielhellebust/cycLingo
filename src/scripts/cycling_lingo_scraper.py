import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import requests

cycling_lingo = []

# with open('wiki_url_list.txt', 'r') as f:
#     url_list = f.read().splitlines()
#
cycling_lingo_list = []
def get_cycling_lingo_greatist():
    try:
        req = requests.get('https://greatist.com/fitness/ultimate-guide-cycling-lingo')
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.findAll('h3')
        lingo_list = []
        for i in text:
            lingo_list.append(i.text)
            print(i.text)
        return lingo_list
    except:
        pass

def get_cycling_lingo_roadbikerider():
    try:
        req = requests.get('https://www.roadbikerider.com/cycling-lingo-slang-definition-list/')
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.findAll('strong')
        lingo_list = []
        for i in text:
            if len(i.text) > 1:
                lingo_list.append(i.text)
        return lingo_list
    except:
        pass

def get_cycling_lingo_cyclingtips():
    try:
        req = requests.get('https://cyclingtips.com/2017/05/cycling-lingo-101/')
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.findAll('strong')
        lingo_list = []
        for i in text:
            if len(i.text) > 1:
                lingo_list.append(i.text)
        return lingo_list
    except:
        pass

def get_cycling_lingo_wiki():
    try:
        req = requests.get('https://en.wikipedia.org/wiki/List_of_bicycle_parts')
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.findAll('div', {'class': 'mw-parser-output'})
        lingo_list = []
        for i in text:
            url = i.findAll('a')
            for j in url:
                if j.text not in lingo_list:
                    lingo_list.append(j.text)



        return lingo_list
    except:
        pass

wiki_lingo = get_cycling_lingo_wiki()

#
# greatist_lingo = get_cycling_lingo_greatist()
#
# roadbikerider_lingo = get_cycling_lingo_roadbikerider()
#
# cyclingtips_lingo = get_cycling_lingo_cyclingtips()
#
# cycling_lingo.extend(greatist_lingo)
# cycling_lingo.extend(roadbikerider_lingo)
# cycling_lingo.extend(cyclingtips_lingo)
cycling_lingo.extend(wiki_lingo)
with open('../wiki_lingo.txt', 'a', encoding='utf-8') as f:
    for url in cycling_lingo:
        try:
            f.write("%s \r  " % url)
        except:
            pass


# with open('wiki_article_text.txt', 'a', encoding='utf-8') as f:
#     for url in article_text:
#         try:
#             f.write("%s \r  " % url)
#         except:
#             pass

