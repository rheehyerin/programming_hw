#-*- coding: utf-8 -*-
import filemapper as fm
'''
from imp import reload
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
'''
cd_collect = []

with open('postcd/1.txt') as file: #thats just totally NOGADA
    q = file.read().split("\n")

for sp_draft in q:
    sp = ''.join(sp_draft).split("|")
    for index, cd in enumerate(sp):
        if index==0:
            cd_collect.append(cd)
            continue
new_file = open('extracted_cd1.txt','a')
new_file.write(','.join(cd_collect))
new_file.close()

'''
all_files = fm.load('postcd')
for f_l in all_files:
    for sp in fm.read(f_l):
        splited = ''.join(sp).split("|")
        for index, cd in enumerate(splited):
            if index == 0:
                cd_collect.append(cd)
                continue

new_file = open('extracted_cd.txt', 'w')
new_file.write(','.join(cd_collect))
new_file.close()
'''
