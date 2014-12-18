import lxml.etree as ET
import sys
xsl_file = sys.argv[1]
xml_file = sys.argv[2]
dom = ET.parse(xml_file)
xslt = ET.parse(xsl_file)
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))
