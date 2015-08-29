__author__ = 'AmirPouya'
__author__ = 'AmirPouya'
import sys
import standard_xml
import io

def writer(file,dic):
    for key in sorted(int(dic.keys())):
        file.writle(dic[key].strip()+"\n")
    file.close()

try:
    input_file=sys.argv[1]
except:
    print "python XML2RAW.py input_file "
    exit(-1)
data=standard_xml.read_standard(input_file)

title=data[0]
source_lang=data[1]
target_lang=data[2]
source_dic=data[3]
target_dic=data[4]
data=""

source_file=io.open(input_file+'.'+source_lang,'w',encoding='utf-8')
target_file=io.open(input_file+'.'+target_lang,'w',encoding='utf-8')

writer(source_file,source_dic)
writer(target_file,target_dic)