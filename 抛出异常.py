#_*_coding:utf-8_*_
class School(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)
try:
    raise School(2*2)
except Exception as e:
    print("My exception occurred.value",e.value)