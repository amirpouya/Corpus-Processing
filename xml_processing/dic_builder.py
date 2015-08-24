__author__ = 'AmirPouya'



def extract_dic(source_root):
    source_doc = {}
    for doc in source_root.getchildren():
        try:
            key = doc.attrib['docid']
            if source_doc.has_key(key):
                print 'Dublicate doc', key
                exit(-1)
            else:
                p_doc = {}
                for child in doc.getchildren():
                    for seg in child.findall('seg'):
                        seg_key = seg.attrib['id']
                        if p_doc.has_key(key):
                            print 'Dublicate seg', seg_key
                            exit(-1)
                        else:
                            p_doc[int(seg_key)] = seg.text
                source_doc[key] = p_doc
        except KeyError:
            print 'Error: Bad formed XML'
            exit(-1)
        except UnicodeDecodeError:
            print seg.text
            exit(-1)
    return  source_doc

