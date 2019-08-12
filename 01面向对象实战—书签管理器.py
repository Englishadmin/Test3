# @Author:chengxiang
# @time:2019/7/19 9:49
'''
URLItem:
属性：
	标题	str
	网址	str
	星级	int
	访问次数 int
方法:
	修改标题，网址，星级
	返回标题，网址，星级访问次数
	打印书签内容
'''


# 用于存储一个书签的信息
class URLItem:
    def __init__(self, title, url, stars):
        self.__title, self.__url, self.__stars, self.__visits = title, url, stars, 0
        # 成员变量声明为___开头，则该变量只能通过self在当前类的成员方法中调用，不能在类外调用

    def set_title(self, title):
        self.__title = title

    def set_url(self, url):
        self.__url = url

    def set_stars(self, stars):
        if stars < 1:
            self.__stars = 1
        elif stars > 5:
            self.__stars = 5
        else:
            self.__stars = stars

    def get_title(self):
        return self.__title

    def get_url(self):
        return self.__url

    def get_stars(self):
        return self.__stars

    def get_visits(self):
        return self.__visits

    # 打印一个书签的信息
    def show(self):
        print("".center(30, "="))
        print("标题:{}\n网址:{}\n星级:{}\n访问次数:{}".format(self.__title, self.__url, "*" * self.__stars, self.__visits))
        print("".center(30, "="))


# url = URLItem("千锋", "www.1000phone.net", 5)
# url.show()

'''
URLManager:
属性:
	通过一个列表，储存并管理大量的书签
方法:
	添加书签
	删除书签(通过标题，通过网址)
	修改书签的标题（通过旧标题，查找书签）
	修改书签的网址
	修改书签的星级
	将所有书签按照访问次数排序后输出
	将所有书签按照星级排序后输出


'''


# 储存并管理大量书签
class URLManager:
    def __init__(self):
        self.__list = []  # 创建一个收藏夹的同时创建list

    # 在列表中查找这个标题的书签
    def __find_urlitem(self, title):
        for i in self.__list:
            if i.get_title() == title:
                return i
        return None

    # 添加书签
    def add_url(self, title: str, url: str, stars: int):
        # 先找列表里有没有该书签
        item = self.__find_urlitem(title)
        if item != None:  # 返回一个对象都为真，只有None为假
            print("标题为{}的书签已存在，添加失败".format(title))
            return
        item = URLItem(title, url, stars)  # 创建书签
        self.__list.append(item)  # 添加到列表
        print("书签{}已添加成功".format(title))

    # 通过标题删除书签
    def remove_url(self, title):
        # 寻找需要删除的书签
        item = self.__find_urlitem(title)
        if not item:
            print("书签{}不存在，删除失败".format(title))
            return
        # 如果存在，item就是
        self.__list.remove(item)
        print("书签{}已删除成功".format(title))

    # 根据网址删除书签
    def remove_urlitem_url(self, url):
        is_exist = False  # 表示不存在url为指定url标签
        for i in self.__list:
            if i.get_url() == url:
                self.__list.remove(i)
                print("书签{}已删除成功".format(i.get_title()))
                is_exist = True
        if is_exist:
            print("网址为{}的书签均已删除".format(url))
        else:
            print("网址为{}的书签不存在，删除失败".format(url))

    # 修改书签的标题(通过旧标题查找书签)
    def change_urlitem_title(self, old_title, new_title):
        # 通过find函数找到需要修改的书签
        item = self.__find_urlitem(old_title)
        if not item:
            print("标题为{}的书签不存在，修改失败".format(old_title))
            return
        item.set_title(new_title)
        print("书签{}以修改标题为{}".format(old_title, new_title))

    # 修改书签的网址
    def change_urlitem_url(self, title, new_url):
        item = self.__find_urlitem(title)
        if not item:
            print("标题为{}的书签不存在，修改失败".format(title))
            return
        item.set_url(new_url)
        print("书签{}以修改网址为{}".format(title, new_url))

    # 修改书签的星级
    def change_urlitem_stars(self, title, new_stars):
        item = self.__find_urlitem(title)
        if not item:
            print("标题为{}的书签不存在，修改失败".format(title))
            return
        item.set_stars(new_stars)
        print("书签{}以修改星级为{}".format(title, "*" * new_stars))

    # 将所有书签按访问次数排序后输出
    def show_urlitem_visits(self):
        for i in range(0, len(self.__list) - 1):
            for j in range(0, len(self.__list) - 1 - i):
                if self.__list[j].get_visits() < self.__list[j + 1].get_visits():
                    self.__list[j], self.__list[j + 1] = self.__list[j + 1], self.__list[j]
        for i in self.__list:
            i.show()

    # 将所有书签按照星级排序后输出
    def show_urlitem_stars(self):
        for i in range(0, len(self.__list) - 1):
            for j in range(i + 1, len(self.__list)):
                if self.__list[i].get_stars() < self.__list[j].get_stars():
                    self.__list[j], self.__list[i] = self.__list[i], self.__list[j]
        for i in self.__list:
            i.show()


manager = URLManager()
manager.add_url("千锋", "www.1000phone.net", 5)
manager.add_url("百度", "www.baidu.com", 4)
manager.add_url("百度", "www.baidu.com", 4)
manager.remove_url("百度")
manager.add_url("百度", "www.baidu.com", 4)
manager.add_url("新浪", "www.sina.com", 3)
manager.add_url("雅虎", "www.yahoo.com", 2)

manager.change_urlitem_stars("雅虎", 4)
manager.change_urlitem_stars("新浪", 3)
manager.change_urlitem_stars("百度", 2)

manager.change_urlitem_title("百度", "谷歌")

manager.change_urlitem_url("千锋", "10000iphone")

manager.change_urlitem_title("雅虎", "Yahoo!!")
# manager.show_urlitem_stars()
manager.show_urlitem_visits()
