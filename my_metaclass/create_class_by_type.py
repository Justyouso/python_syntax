# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-1 下午5:55

"""
使用type函数手动创建一个类，type需要接受是三个参数
1. 类的名称，若不指定，也要传入空字符串：""
2. 父类，注意以tuple的形式传入，若没有父类也要传入空tuple：()，默认继承object
3. 绑定的方法或属性，注意以dict的形式传入
"""


# 准备一个基类（父类）
class BaseClass:
    def talk(self):
        print("我是一个基类")

    def test(self):
        pass


# 准备一个方法
def say(self):
    print("hello")


# 使用type来创建类，并绑定方法和属性
User = type("User", (BaseClass,), {"name": "wc", "say": say})
