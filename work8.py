import urllib.request as r

f = open('taobao_data_haerbin.txt','w',encoding='utf-8')

for i in range(0,100):
   url='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&loc=%E5%93%88%E5%B0%94%E6%BB%A8&s='+str(i*44)+'&ajax=true'
   data=r.urlopen(url).read().decode('utf-8','ignore')
   #data写进文件中
   f.write(data+'\n')
   print("第"+str(i+1)+"条")
f.close()
print('finish')
