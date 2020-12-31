import pandas as pd 

import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    # create element tree object 
    tree = ET.parse(xmlfile) 
    root=tree.getroot()
    print(root.tag)
    for i in root.findall('note'):
        print(i.attrib)
        print(i.find('to').text, i.find('from').text, i.find('heading').text, i.find('body').text)
   
parseXML('demo.xml')
  
            
   