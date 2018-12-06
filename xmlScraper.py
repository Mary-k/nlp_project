
from lxml import etree
from xml.etree import  ElementTree
url = 'http://www.adab.com/modules.php?name=Sh3er&doWhat=shqas&qid=14324&r=&rc=0'


html = urllib2.urlopen(url)

root = etree.parse(html) 

res = requests.get(url)
doc = lxml.html.parse(res.content)
doc = lxml.html.fromstring(root.content)


root = etree.fromstring(xml, base_url='http://www.adab.com/modules.php?name=Sh3er&doWhat=shqas&qid=14324&r=&rc=0')

from lxml import etree

root = etree.Element("root")
root.set("interesting", "somewhat")
child1 = etree.SubElement(root, "test")

et = etree.ElementTree(root)
et.write(sys.stdout, pretty_print=True)


