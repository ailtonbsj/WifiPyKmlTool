# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 05:01:32 2016

@author: WindowsSeven

Join places of file gEarth of wifi collector

COMAND LINE:

joinkml file1.kml file2.kml filem.kml > out.kml

"""

from xml.dom import minidom
import sys

tang = len(sys.argv)
if tang < 3:
    print "invalid input!"
    exit()

docs = []
for i in range(1,tang):
    docs.append(minidom.parse(sys.argv[i]))

sty = docs[0].getElementsByTagName("Style")

print """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Folder>

"""

for s in sty:
    print s.toxml()
for doc in docs:
    for pl in doc.getElementsByTagName("Placemark"):
        print pl.toxml().encode('utf8') 

print """

</Folder></kml>"""

