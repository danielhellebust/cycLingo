import time
from bs4 import BeautifulSoup
import requests

article_text = []

with open('../wiki_url_list.txt', 'r') as f:
    url_list = f.read().splitlines()

def get_wiki_article(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        text = soup.findAll('div', {'class': 'mw-parser-output'})
        sentence_list = []
        #print(text)
        for i in text:
            body = i.findAll('p')
            for j in body:

                # filter out sentences that are too short

                body_text = j.text.encode('ascii', 'ignore').decode('ascii').replace('\n', '').strip()
                #print(body_text)
                if len(body_text) > 60:
                    sentence_list.append(body_text)


        return sentence_list
    except:
        pass

for i in range(33000, len(url_list)):
    print(i)
    try:
        #print(get_wiki_article(url_list[i]))
        article_text.extend(get_wiki_article(url_list[i]))
    except:
        pass
    time.sleep(1)

with open('../wiki_article_text.txt', 'a', encoding='utf-8') as f:
    for url in article_text:
        try:
            f.write("%s \r  " % url)
        except:
            pass

# write json to text file:
with open('../wiki_article_text.txt', 'w') as f:
    json.dump(article_text, f)

