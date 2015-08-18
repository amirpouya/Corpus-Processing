__author__ = 'AmirPouya'
import io
import filters
import sys

arabic_file=''
farsi_file=''

if len(sys.argv)!=3:
    print 'Usagae: python remove_english.py arabice_file_path  farsi_file_path'
    exit(-1)

arabic_file=sys.argv[1]
farsi_file=sys.argv[2]

ar_file=io.open(arabic_file,'r',encoding='utf-8')
fa_file=io.open(farsi_file,'r',encoding='utf-8')


print 'Reading Files started..'
ar_lines=ar_file.readlines()
fa_lines=fa_file.readlines()
print 'Reading Files ended..'

if len(ar_lines) !=  len(fa_lines):
    print 'Not Equal lines,is this corpus parallel?'
    exit(-1)

farsi_out_file=farsi_file+'.filtered'
arabic_out_file=arabic_file+'.filtered'

fa_out_file=io.open(farsi_out_file,'w',encoding='utf-8')
ar_out_file=io.open(arabic_out_file,'w',encoding='utf-8')

remove_line_counter=0
print 'Filtering process starts...'
for i,line in enumerate(ar_lines):
    if filters.isArabic(line) and filters.isFarsi(fa_lines[i]):
        fa_out_file.write(fa_lines[i])
        ar_out_file.write(ar_lines[i])
    else:
        remove_line_counter+=1
fa_out_file.close()
ar_out_file.close()

print 'Number of removed line:',remove_line_counter
print 'DONE!'
