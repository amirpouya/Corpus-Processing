__author__ = 'AmirPouya'
import xml.etree.ElementTree as ET
import sys

source_file=sys.argv[1]
target_file=sys.argv[2]

try:
    source_tree=ET.parse(source_file)
except:
    source_file=open(source_file,'r')
    source_file.read(source_file)
    source_file='<corpus>'+source_file+'</corpus>'
    source_tree=ET.fromstring(source_file)
try:
    target_tree=ET.parse(target_file)
except:
    target_file=open(target_file,'r')
    target_file.read(target_file)
    target_file='<corpus>'+target_file+'</corpus>'
    target_tree=ET.fromstring(target_file)

source_root=source_tree.getroot()
target_root=target_tree.getroot()


