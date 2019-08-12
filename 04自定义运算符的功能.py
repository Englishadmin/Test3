# @Author:chengxiang
# @time:2019/7/19 16:21
# ptthon可以自定义运算符的功能
class Point:
    def __init__(self,x,y):
        self.__x,self.__y = x, y

    def __repr__(self):
        return "({},{})".format(self.__x,self.__y)

    #自定义两个点相加得到一个新的Point对象
    def __add__(self, other):
        #s1+s2  加号是个幌子，实际上是调用这个函数
        return Point(self.__x+other.__x,self.__y + other.__y)
    def __truediv__(self, other):
        return 4
p1=Point(3,4)
p2=Point(5,6)
p3=Point(5,6)
p =p1+p2+p3
print(p)
