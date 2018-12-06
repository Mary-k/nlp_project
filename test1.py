import xml.etree.ElementTree as ET

# create the file structure
data = ET.Element('opems')  
items = ET.SubElement(data, 'poem')  
item1 = ET.SubElement(items, 'verse')  
item1.text = 'item1abc'  

# create a new XML file with the results
mydata = ET.tostring(data)  
print(mydata)
#mydata=str(data)
myfile = open("items2.xml", "wb")  
myfile.write(mydata) 