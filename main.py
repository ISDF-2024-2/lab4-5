# 类属性
class People:
    name = "Tom"       # 公有的类属性
    __age = 18          # 私有的类属性


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    p = People()
    print(p.name)  # 实例对象
    print(People.name)  # 类对象

    # print(p.__age)    	 # 错误 不能在类外通过实例对象访问私有的类属性
    # print(People.__age)  	 # 错误 不能在类外同过类对象访问私有的类属性

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
