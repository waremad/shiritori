#必要なもの
#txtからlistにする
#正しくひらがなのみで構成された言葉か判定する
#ある文字で始まる言葉をリストから抽出
#txtにその単語が含まれるか
#txtの末尾に単語を追加
#すでに使われた単語か判定
#欲しいひらがなを決める
#指定した文字で終わる言葉を抽出

def readtxt(path):
    out = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            out.append(line.strip())
    return out

