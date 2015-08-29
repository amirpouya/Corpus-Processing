__author__ = 'AmirPouya'
import standard_xml
import argparse

parser=argparse.ArgumentParser('python LDC2XML.py')
parser.add_argument('--input','-i',required=True)
parser.add_argument('--output','-o',required=True)
parser.add_argument('--cname',required=True,default='corpus')
parser.add_argument('--srclang',required=True,default='ar')
parser.add_argument('-trglang',required=True,default='en')
args=parser.parse_args()

file=args.input
target_file=args.target
out_file=args.output
config={}
config['corpus_name']=args.cname
config['source_lang']=args.srclang
config['target_lang']=args.trglang


dics=standard_xml.read_cdecformat(file)
standard_xml.write(dics[0],dics[1],out_file,config)
