__author__ = 'AmirPouya'
import xml.etree.ElementTree as ET
import sys

source_file=sys.argv[1]
target_file=sys.argv[2]

source_tree=ET.parse(source_file)
target_tree=ET.parse(target_file)

source_root=source_tree.getroot()
target_root=target_tree.getroot()


