#必要なもの
#txtからlistにする
#正しくひらがなのみで構成された言葉か判定する
#ある文字で始まる言葉をリストから抽出
#txtにその単語が含まれるか
#txtの末尾に単語を追加
#すでに使われた単語か判定
#欲しいひらがなを決める
#指定した文字で終わる言葉を抽出
#log 今まで使われた単語
#memo まだ使っていない単語
#head 次の頭文字

import random
import time

def delmini(self):#小文字や伸ばし棒を消す:
    ls = ["ぁ","ぃ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ","ゕ","ゖ","っ","ゎ","ー"]
    out = ""
    for i in self:
        if not(i in ls):
            out += i
    return out

def readtxt(path):#txtからlistに
    out = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            out.append(line.strip())
    n = 0
    while "" in out:
        if out[n] == "":
            out.pop(n)
        else:
            n += 1
    return out

def isjphira(self):#ひらがなかどうか
    if self == "":
        return False
    for i in self:
        n = ord(i)
        if not(ord('ぁ') <= n and n <= ord('ゖ')) and i!="ー":
            return False
    return True

def piclist(head,ls):#listから指定した頭文字の単語を抽出
    if ls == [] or head == "":
        return []
    out = []
    for i in ls:
        if i[0] == head:
            out.append(i)
    return out

def writetxt(value,path):#txtに追記
    with open(path, 'a') as f:
        print(value, file=f,end = "")

log = []
memo = []
head = ""
def hand(word):#単語を使用
    global log
    global memo
    global head
    
    if not(word in log or word in memo):
        writetxt(word+"\n","words.txt")
    log.append(word)
    if word in memo:
        memo.remove(word)
    head = delmini(word)[-1]

def avehead(ls):#欲しい頭文字を決める
    keys = []
    dic = {}
    for i in ls:
        if not(delmini(i)[0] in keys):
            keys.append(delmini(i)[0])
        if not(delmini(i)[-1] in keys):
            keys.append(delmini(i)[-1])
    for i in keys:
        n = 0
        for j in ls:
            if delmini(j)[0] == i:
                n += 1
        dic[i] = n
    chara = []
    while not(dic == {}):
        chara.append([])
        mini = min(list(dic.values()))
        for i in list(dic.keys()):
            if dic[i] == mini:
                chara[-1].append(i)
                dic.pop(i)
    out = []
    while out == [] and chara != []:
        for i in ls:
            if delmini(i)[-1] in chara[0]:
                out.append(i)
        chara.pop(0)
    return out

def piclist2(head,ls):#listからほしい文字を考慮して指定した頭文字の単語を抽出
    keys = []
    dic = {}
    for i in ls:
        if not(delmini(i)[0] in keys):
            keys.append(delmini(i)[0])
        if not(delmini(i)[-1] in keys):
            keys.append(delmini(i)[-1])
    for i in keys:
        n = 0
        for j in ls:
            if delmini(j)[0] == i:
                n += 1
        dic[i] = n
    chara = []
    while not(dic == {}):
        chara.append([])
        mini = min(list(dic.values()))
        for i in list(dic.keys()):
            if dic[i] == mini:
                chara[-1].append(i)
                dic.pop(i)
    out = []
    while out == [] and chara != []:
        for i in ls:
            if delmini(i)[-1] in chara[0]:
                if delmini(i)[0] == head:
                    out.append(i)
        chara.pop(0)
    return out

#"""
timelimit = 60
log = []
outchara = ["ん","ぢ","づ","ゑ","ゐ","を","ゔ"]
writetxt("","words.txt")
memo = readtxt("words.txt")
if memo == []:
    memo = ["しりとり"]
    writetxt("しりとり\n","words.txt")
    word = "しりとり"
else:
    word = random.choice(avehead(memo))
while not(memo == [] or timelimit <= 0):
    hand(word)
    print("cp:"+ word)
    mine = ""
    start = time.time()
    while mine == "":
        mine = input(head + str(int(timelimit//1)) + "? ")
        if isjphira(mine):
            if mine in log:
                mine = ""
                print("既に使われている")
            elif delmini(mine)[0] != head:
                print("字違う",mine[0],hand)
                mine = ""
            elif delmini(mine)[-1] in outchara:
                print("「"+delmini(mine)[-1]+"」で終わってる")
                mine = ""
        else:
            mine = ""
            print("ひらがなじゃない")
    timelimit -= time.time() - start
    hand(mine)
    if piclist2(delmini(mine)[-1],memo) != []:
        word = random.choice(piclist2(delmini(mine)[-1],memo))
    else:
        memo = []
    timelimit += 5
if timelimit <= 0:
    print("time over")
else:
    print("you win")
#"""