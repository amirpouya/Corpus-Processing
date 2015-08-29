__author__ = 'AmirPouya'
#from lxml import etree as ET
from lxml import etree as ET
import dic_builder
import standard_xml
import sys,argparse
import codecs

#source_file=sys.argv[1]
#target_file=sys.argv[2]


parser=argparse.ArgumentParser('python LDC2XML.py')
parser.add_argument('--source','-s',required=True)
parser.add_argument('--target','-t',required=True)
parser.add_argument('--output','-o',required=True)
parser.add_argument('--cname',required=True,default='corpus')
parser.add_argument('--srclang',required=True,default='ar')
parser.add_argument('-trglang',required=True,default='en')
args=parser.parse_args()

source_file=args.source
target_file=args.target
out_file=args.output
config={}
config['corpus_name']=args.cname
config['source_lang']=args.srclang
config['target_lang']=args.trglang

xml_parser = ET.XMLParser(recover=True,encoding='utf-8',resolve_entities=True )
source_tree=ET.parse(source_file,xml_parser)
target_tree=ET.parse(target_file,xml_parser)


source_root=source_tree.getroot()
target_root=target_tree.getroot()
source_dic=dic_builder.extract_dic(source_root)
target_dic=dic_builder.extract_dic(target_root)
standard_xml.write(source_dic,target_dic,out_file,config)




