# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 22:32:37 2016

@author: Jose Ailton

Remove equals place in file wifi collector for gEarth

COMAND LINE:

$ removedup file.kml


"""

from xml.dom import minidom
import codecs
import sys

if len(sys.argv) != 2:
    print "invalid input!"
    exit()

doc = minidom.parse(sys.argv[1])

sty = doc.getElementsByTagName("Style")
pms = doc.getElementsByTagName("Placemark")

tan = len(pms)
i=0
while i < tan:
    print("Porcentagem: %s %%" % (float(i)/tan*100))
    pm = pms[i]
    n = pm.getElementsByTagName("name")[0].firstChild.data
    c = pm.getElementsByTagName("coordinates")[0].firstChild.data
    d = pm.getElementsByTagName("description")[0].toxml().encode('utf8')
    j=i+1    
    while j < tan:
        dup = pms[j]
        dn = dup.getElementsByTagName("name")[0].firstChild.data
        dc = dup.getElementsByTagName("coordinates")[0].firstChild.data
        dd = dup.getElementsByTagName("description")[0].toxml().encode('utf8')
        if((n == dn) and (c == dc) and (d == dd)):
            pms.pop(j)
            tan = len(pms)
            j=j-1
        j=j+1
    i=i+1

docNodes = doc.getElementsByTagName("Folder")[0]
docRoot = docNodes.parentNode
docRoot.removeChild(docNodes)
fd = doc.createElement("Folder")
fd.childNodes = sty
fd.childNodes += pms
docRoot.appendChild(fd)

with codecs.open("R"+sys.argv[1],"w","utf-8") as out:
    doc.writexml(out)

print("Porcentagem: 100.0 %")
print("Arquivo gerado em " + "R"+sys.argv[1])