
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


response  = session.get('http://www.adab.com/modules.php?name=Sh3er&doWhat=shqas&qid=9504&r=&rc=0')
response.encoding='windows-1256'
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find_all(class_="poem") 
title = soup.find('title')

print(title.string)
