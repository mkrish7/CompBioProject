import lxml.etree as ET
import sys
import os

xml_files = []
with open('article_list', 'r') as f:
    lines = f.readlines()
    for line in lines:
        xml_files.append(line.strip())
    
dic = {}
for xml_file in xml_files:
    dom = ET.parse(xml_file)
    root = dom.getroot()
    for insg in root.iter('insg'):
	    ins = insg.find('ins')
	    p = ins.find('p')
	    value = p.text
	    break
    #dic[xml_file.split('/')[-1]] = value.encode('utf-8')
    location = value.encode('utf-8')    
    if location in dic:
        dic[location] += 1
    else:
        dic[location] = 1
    
for key in dic:
    print key + ' : ' + str(dic[key])
    
