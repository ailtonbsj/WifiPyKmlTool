# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 22:32:37 2016

@author: Jose Ailton

Remove equals place in file wifi collector for gEarth

COMAND LINE:

$ removedup file.kml


"""

from xml.dom import minidom
from xml.dom.minidom import parse, parseString
import codecs
import sys

if len(sys.argv) != 2:
    print "invalid input!"
    exit()

doc = minidom.parse(sys.argv[1])
pms = doc.getElementsByTagName("Placemark")

print """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html><head><title>Wireless Networks List</title>
<style>
td {
    text-align: center;
}
</style>
</head>
<body><h3>Wireless Networks List</h3><p>
<table border='1''>
<tr>
<th>Name
<th>Address
<th>Company
<th>Sign Level
<th>Frequency
<th>Channel
<th>Security
<th>Cipher
<th>BSS Typer
<th>WPS
<th>Time
<th>Longitude
<th>Latitude
</tr>
"""

for pm in pms:
    t = pm.getElementsByTagName("description")[0].firstChild.data
    d = parseString(t.encode('utf8'))    
    
    print "<tr>"
    for tr in d.getElementsByTagName("tr"):
        print tr.firstChild.nextSibling.toxml().encode('utf8')
    print "</tr>"
    
print """</table></body>
</html>
"""