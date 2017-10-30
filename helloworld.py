# coding: utf-8

import importSample

data = [66, 59, 62, 64, 63,
        68, 65, 59, 68, 64,
        65, 51, 67, 64, 83,
        59, 61, 62, 57, 72,
        65, 64, 54, 60, 53,
        65, 67, 60, 53, 79,
        74, 53, 61, 68, 75,
        50, 57, 55, 66, 56,
        55, 61, 70, 71, 49,
        69, 70, 80, 73, 72]

class SampleHelloClass:
    def funcInstance(self, row):
        all = row + 10
        print ("クラスとインスタンスの検証です。" + str(all))
    def funcList(self, list):
        for n in list:
            yield n*2
    def isodd(self, x): return x % 2

class SampleInitClass():
    def __new__(cls):
        print("newの検証です。Hello!")
        return super().__new__(cls)
    def __init__(self):
        print("initの検証です。Hello!")

# クラスとインスタンスの検証
a = SampleHelloClass()
plus = 5
a.funcInstance(plus)

# importとドキュメントストリングの検証
im = importSample.SampleImportClass()
im.funcImportInstance(d1='D1')
print("ドキュメントストリング(注約)の検証です。" + importSample.__doc__)

# ファイルの検証
print("ファイルの検証です。" + __file__)

# newとsuperとinitの検証
SampleInitClass()

# ジェネレータの検証
print("↓ジェネレータの検証です。")
for n in a.funcList([1, 2, 3, 4, 5]):
    print(n)

# デコレータの検証
@im.SampleDecolator
def hello():
    print("I am decorator")
hello()

# filterの検証
aList = [1, 2, 3]
print("filterの検証です。" + str(filter(a.isodd, aList)))

