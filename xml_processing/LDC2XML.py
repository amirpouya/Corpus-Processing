__author__ = 'AmirPouya'
from lxml import etree as ET
import dic_builder
import standard_xml_writer
import sys

source_file=sys.argv[1]
target_file=sys.argv[2]

#source_file='source_p1.xml'
#target_file='target_p1.xml'
out_file='test.xml'
config={}
config['corpus_name']='test'
config['source_lang']='ar'
config['target_lang']='en'
config['corpus_desc']=''

parser = ET.XMLParser(recover=True,encoding='utf-8' )
source_tree=ET.parse(source_file,parser)
target_tree=ET.parse(target_file,parser)


source_root=source_tree.getroot()
target_root=target_tree.getroot()
source_dic=dic_builder.extract_dic(source_root)
target_dic=dic_builder.extract_dic(target_root)
standard_xml_writer.write(source_dic,target_dic,out_file,config)




