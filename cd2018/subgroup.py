import re
with open("2a.txt") as ml:
    #將2a.txt檔案開啟, 命名為ml的"列表".
    mushroom = ml.readlines()
    #逐行讀入ml的"列表",將其命名為mushroom
    mushroom = [(re.findall('405\d\d\d\d\d', mushroom[i])) for i in range(len(mushroom))]
    #使用re的"套件"(findall)在mushroom"列表"中找出開頭為405xxxxx的"字串".
    #使用len找出mushroom的"長度""範圍",使用for"迴圈"排出mushroom的"列表"並命名為代數"i".

num = 0
#將num從零開始
for a in range(len(mushroom)):
#使用len找出mushroom的"長度""範圍",使用for"迴圈"排出mushroom的"列表"並命名為代數"a".
    row = mushroom[a]
    #將mushroom[a]命名為row
    for b in range(len(row)):
    #使用for"迴圈"排出row的"列表"並命名為代數"b".
        if b%3 == 0:
        #假設代數"b"(row的長度)能被三整除.
            num += 1
            #滿足以上條件時, num加一.
            print('第' + str(num) +'組:' + str(row[b:b+3]))
            #"顯示"出結果為('第' + "字串"num + '組:' + "字串"row的"長度"從b開始至b+3.