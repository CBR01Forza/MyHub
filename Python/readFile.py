# -*- coding: utf-8 -*-
#ファイル読み込み

f = open('data.csv', 'r')

for row in f:
    print (row)
    
f.close()
