#coding:utf-8
import csv

#ファイルが無ければ作る、の'a'を指定
f = open('data.csv', 'ab') 

csvWriter = csv.writer(f)

val = 0
for num in range(1, 5):
   listData = []
   val = num
   
   #listにデータの追加
   listData.append(val)                      
   for loop in range(0, 5):
      val = val * 10 + num
      listData.append(val)
      
   #1行書き込み
   csvWriter.writerow(listData)          

f.close()
