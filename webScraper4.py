import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from lxml import etree
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import html
import re

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

PoemUrlPart1='http://www.adab.com/modules.php?name=Sh3er&doWhat=shqas&qid='
PoemUrlPart2='&r=&rc='

pre_islamEra_poets=[14324,14505,10646,17326,19415]#increment by one to go thraugh the poems
islamAndAmaoui_era_poets=[10475,16336,15472,14065,26338]
Abbasi_era_poets=[11935,15641,57369,84838,57448]
modern_era_poets=[53148,64436,372,420,9504]

erasList=[pre_islamEra_poets,islamAndAmaoui_era_poets,Abbasi_era_poets,modern_era_poets]
ErasforldersList=['1pre_islamic_era/','2islamAndAmaoui_era/','3Abbasi_era/','4modern_era/']

corpusPath='/home/mimi/Desktop/NLP/project/corpus/'
poemTypes=('poem/','prose/')

def getAuthorName(title):
        l = title.split(":")
        print(l)
        poemName=l[1]
        
        s = l[0].split("..")
        authorName=s[1]
        return(authorName,poemName)

def webScraper(corpusPath,poemUrl):
        print(poemUrl)
        response  = session.get(poemUrl)
        response.encoding='windows-1256'
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find_all(class_="poem") 
        title = soup.find('title')
        (authorName,poemName)=getAuthorName(str(title.string))
        print(authorName,poemName)
        FileSave.write(str(authorName+' '+poemName))
        FileSave.write('\n')
FileSave=open('poemes.txt','w',encoding = "utf-8")
for target_era in range(0,4):
        #erasList[target_era]
        #ErasforldersList[target_era]
        for poetId in erasList[target_era]:
                print(poetId)
                for poemId in range(0,5):
                        corpus_path=corpusPath+ErasforldersList[target_era]+poemTypes[0]
                        url_poem=url_poem_page=PoemUrlPart1+str(poetId)+PoemUrlPart2+str(poemId)
                        webScraper(corpus_path,url_poem)
                        poetId+=1
        
                              
        