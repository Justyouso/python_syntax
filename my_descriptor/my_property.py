# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-30 下午10:29


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
    s.math = 90
    print(s)
# s.math(90)
# print(s)
