from shiritori import *

def test_delmini():
    assert delmini("") == ""
    assert delmini("あいうえお") == "あいうえお"
    assert delmini("るーる") == "るる"
    assert delmini("るびー") == "るび"

def test_readtxt():
    assert readtxt("./tests/test1.txt") == []
    assert readtxt("./tests/test2.txt") == ["abc","defg","hijkl"]

def test_isjphira():
    assert isjphira("") == False
    assert isjphira("あ") == True
    assert isjphira("ｘ") == False
    assert isjphira("こんにちは") == True
    assert isjphira("ｋんにちは") == False
    assert isjphira("るーる") == True

def test_piclist():
    assert piclist("",[]) == []
    assert piclist("a",[]) == []
    assert piclist("",["a"]) == []
    assert piclist("あ",["あいうえお","ああ","えおあお","かああ"]) == ["あいうえお","ああ"]
    assert piclist("わ",["あいうえお","ああ","えおあお","かああ"]) == []

def test_avehead():
    assert avehead(["しりとり"]) == ["しりとり"]
    assert avehead(["しりとり","りんご"]) == ["りんご"]
    assert avehead(["しりとり","りんご","ごり"]) == ["しりとり","りんご","ごり"]
    assert avehead(["しりとり","りんご","ごり","ごま"]) == ["ごま"]
    assert avehead(["しりとり","りんご","ごり","ごま","るーる"]) == ["ごま"]
    assert avehead(["しりとり","りんご","ごり","ごま","るーる","るびー"]) == ["ごま","るびー"]
    assert avehead(["しりとり","りんご","ごり","ごま","るーる","るびー","びーる"]) == ["ごま"]

def test_piclist2():
    assert piclist2("",[]) == []
    assert piclist2("a",[]) == []
    assert piclist2("",["a"]) == []
    assert piclist2("あ",["あいうえお","ああ","えおあお","かああ"]) == ["あいうえお"]
    assert piclist2("わ",["あいうえお","ああ","えおあお","かああ"]) == []

