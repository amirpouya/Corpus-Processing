import argparse
import standard_xml

parser=argparse.ArgumentParser('python RAW2XML.py')
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
print 'Start Building Dics:'
dics=standard_xml.read_rawtext(source_file,target_file)
print 'Start Writing XML'
standard_xml.write(dics[0],dics[1],out_file,config)


