__author__ = 'AmirPouya'
from lxml import etree as ET
import time


def write(source_dic,target_dic,output_file,config):
    root=ET.Element('corpus')
    root.attrib['title']=config['corpus_name']
    root.attrib['source_lang']=config['source_lang']
    root.attrib['target_lang']=config['target_lang']
    root.attrib['create_date']=time.strftime("%d/%m/%Y")
    root.attrib['corpus_desc']=config['corpus_desc']
    par_id = 1
    for key in sorted(source_dic.keys()):
        if target_dic.has_key(key):
            for seg_key in sorted(source_dic[key].keys()):
                if target_dic[key].has_key(seg_key):
                    par = ET.SubElement(root, 'p')
                    par.attrib['id'] = str(par_id)
                    par_id += 1
                    src = ET.SubElement(par, 'source').text = source_dic[key][seg_key].strip()
                    trg = ET.SubElement(par, 'target').text = target_dic[key][seg_key].strip()

        else:
            print "Doc not found", key
    tree = ET.ElementTree(root)
    tree.write(output_file, pretty_print=True, encoding='utf-8', xml_declaration=True)