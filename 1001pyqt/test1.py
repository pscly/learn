# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：
# import sys
#
# print(sys.argv)

class A:
    def __init__(self, name, *args, **kwargs):
        self.name = name

class B(A):
    def __init__(self,*args, **kwargs):
        super(B, self).__init__(*args, **kwargs)
        self.name2 = 'n2'

b = B(name=123,name2=31)
print(b.name)
print(b.name2)
