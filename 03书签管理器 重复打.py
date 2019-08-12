# @Author:chengxiang
# @time:2019/7/19 14:13
# 用于存储一个书签的信息
class URLItem:
    def __init__(self, title, url, stars):
        self.__title, self.__url, self.__stars, self.__visits = title, url, stars, 0

    def set_title(self, title):
        self.__title = title

    def set_url(self, url):
        self.__url = url

    def set_stars(self, stars):
        if stars < 1:
            self.__url = 1
        elif stars > 5:
            self.__stars = 5
        else:
            self.__stars = stars

    def get_title(self):
        return self.__title

    def get_url(self):
        return self.__url

    def get_stars(self):
        return self.__visits

    def show(self):
        print("".center(30, '='))
        print('标题:{}\n网址:{}\n星级:{}\n访问次数:{}'.format(
            self.__title, self.__url, self.__stars * '*', self.__visits))
        print(''.center(30, '='))


url = URLItem("千锋", 'www.1000phone.net', 5)
url.show()


class URLManager:
    def __init__(self):
        self.__list = []

    def __find_urlitem(self, title):
        for i in self.__list:
            if i.get_title() == title:
                return i
        return None

    def add_url(self, title: str, url: str, stars: int):
        item = self.__find_urlitem(title)
        if item:
            print("标题为{}的书签已存在，添加失败".format(title))
            return
        item = URLItem(title, url, stars)
        self.__list.append(item)
        print("书签{}已添加成功".format(title))
