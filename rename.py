import lxml.etree as ET
import sys
import os
xml_path = '/home/satishkumaar/Documents/CSE549/project/test/text/articles_xml'
xml_files = []
for root, dirs, files in os.walk(xml_path):
    for xml_file in files:    
        xml_files.append(os.path.join(root, xml_file))

for xml_file in xml_files:
    #xml_file = sys.argv[1]
    dom = ET.parse(xml_file)
    root = dom.getroot()
    for pub in root.iter('pub'):
	    date = pub.find('date')
	    year = date.find('year')
	    pub_year = year.text
	    break

    # rename the corresponding text file with the published year
    text_filename = xml_file.replace('.xml', '.txt').replace('/articles_xml/', '/articles_text/')
    new_filename = text_filename.replace('/articles_text/', '/articles_text/' + pub_year + '_')
    os.rename(text_filename, new_filename)

