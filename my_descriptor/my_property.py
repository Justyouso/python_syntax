# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-30 下午10:29


"""
Property就是一个描述器，@Property等同于math=Property(math),即给Student添加类属性math,
在下面的例子中,math从头到尾都没有被赋值成一个数值,
1. 调用s.math=90时,通过Property的__set__方法调用Student中被@math.setter装饰的math方法给_math赋值
2. 调用s.math是,通过Property的__get__方法调用Student中被@Property装饰的math方法取出_math的值

所以在此例中,并没有对math直接赋值,而是通过调用Property相关方法对_math取值,赋值
"""


class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        print("in __get__")
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def __set__(self, obj, value):
        print("in __set__")
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)

    def __delete__(self, obj):
        print("in __delete__")
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)

    def getter(self, fget):
        print("in getter")
        # Property(fget, self.fset, self.fdel, self.__doc__),返回一个实例
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        print("in setter")
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        print("in deleter")
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class Student:
    def __init__(self, name):
        self.name = name

    """
    加上@Property等同于math=Property(math),即给Student添加类属性math
    """

    @Property
    def math(self):
        return self._math

    """
    @math.setter等同于math=math.setter(math)将math覆盖掉
    """

    @math.setter
    def math(self, value):
        self._math = value

    """
    @math.deleter等同于math=math.deleter(math)将math覆盖掉
    """

    @math.deleter
    def math(self):
        pass


if __name__ == "__main__":
    s = Student("wc")
    """
    1. 实例s中没有math属性,去类Student中找到.
    2. 在Student中math是一个描述器
    3. s.math=90 等同于 Student.math.__set__(s,90)
    4. 在Property中,__set__中 self.fget(obj,value) 
       其中 self.fget->math , obj->s , value->90 ,所以,
       self.fget(obj,value) 等同于 math(self,90), 也就是Student的set方法
    """
    s.math = 90
    # math属性并不在__init__中，所以会报语法
    print(s.math)
    pass
