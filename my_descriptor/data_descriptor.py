# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-29 上午10:20

"""
math 是数据描述符，而 chinese 是非数据描述符。从下面的验证中，可以看出，
当实例属性和数据描述符同名时，会优先访问数据描述符（如下面的math），
而当实例属性和非数据描述符同名时，会优先访问实例属性（__getattribute__）
"""


# 数据描述符
class DataDes:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        self._score = value

    def __get__(self, instance, owner):
        print("访问数据描述符里的 __get__")
        return self._score


# 非数据描述符
class NoDataDes:
    def __init__(self, default=0):
        self._score = default

    def __get__(self, instance, owner):
        print("访问非数据描述符里的 __get__")
        return self._score


class Student:
    math = DataDes(10)
    chinese = NoDataDes(0)

    def __init__(self, name, math, chinese):
        self.name = name
        self.math = math
        self.chinese = chinese

    def __getattribute__(self, item):

        """
        将self转换成Student父类对象，再调用父类的方法
        python3 中super(Student,self)=super()
        """
        return super().__getattribute__(item)


if __name__ == "__main__":
    s = Student("wc", 100, 80)
    print(s.__dict__)
    print(type(s).__dict__)
    print(Student.mro())
    # 数据描述符
    print(s.math)
    # 非数据描述符
    print(s.chinese)
