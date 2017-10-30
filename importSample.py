# coding: utf-8

"""A sample module"""
class SampleImportClass:
    def funcImportInstance(self, **params):
        print ("importとキーワード付き引数である辞書型の検証です。" + str(params))
    def SampleDecolator(self, func):
        def wrapper():
            print("↓デコレータの検証です↓")
            func()
            print("↑デコレータの検証です↑")
        return wrapper
