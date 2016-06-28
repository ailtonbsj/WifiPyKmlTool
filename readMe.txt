#####################################################
#
#  Using Python(X,Y) 2.7.5.1
#  Windows 7 Ultimate
#
#  By Jose Ailton BS
#
#####################################################

#go to folder with soft and files
cd "..\yourFolderWithSoftPython"

#join the files
joinkml sample1.kml sample2.kml > out.kml

#remove duplicates
remdupkml out.kml

#export the datas to html
kml2html Rout.kml > out.html