# -*- coding:utf-8 -*-

class Dog:

    def __del__(self):
        print("--over---")

    #私有方法
    def __sendMsg(self):
        print("---正在发送短信----")
        print("...")
        print("---成功发送短信----")

    #公有方法
    def sendMsg(self, money):
        if (money > 100):
            self.__sendMsg()
        else:
            print("余额不足，请先充值再发送短信")

dog = Dog()
dog.sendMsg(500)

dogA = dog
del dog
del dogA  #最终销毁对象会调用__del__方法
#如果在程序结束时,有些对象还存在,那么python解释器会自动调用它们的__del__方法来完成清理工作
