# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-30 下午9:50


class A:
    def add(self, x):
        y = x + 1
        print("A", y)


class C:
    def add(self, x):
        y = x + 1
        print("C", y)


class B(A, C):
    def add(self, x):
        print(x)
        """
        执行第一继承类A中的add
        """
        super().add(x)
        """
        执行C类的add方法，猜想人为没有指向B的第一继承类A，自动调用第二继承类
        """
        super(A, self).add(x)


if __name__ == "__main__":
    b = B()
    b.add(2)  # 3
    print(b)