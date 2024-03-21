# 类属性
class People:
    name = "Tom"  # 公有的类属性
    __age = 18  # 私有的类属性

    def __init__(self, age):
        self.__age = age
        self.height = 1.75
        self.weight = 70

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def BMI(self):
        bmi = self.weight / self.height ** 2
        return bmi


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    p = People(20)  # 初始化实例的私有属性为20

    print(p.name)  # 通过实例对象访问公有属性 Tom
    print(People.name)  # 通过类对象访问公有属性 Tom
    p.name = "李四"  # 对实例属性赋值
    print(p.name)  # 实例属性为 李四
    print(People.name)  # 类属性为  Tom

    print(p.get_age())  # 通过实例方法来访问类私有属性 20
    p.set_age(25)  # 通过实例方法来设置类私有属性
    print(p.get_age())  # 通过实例方法来访问类私有属性 25
    # print(People.get_age())    不能通过类的方法来输出类私有属性，因为self没有指定

    p.sex = "男"  # 定义一个实例属性
    print(p.sex)  # 实例属性可以通过实例名来访问，不能通过类名来访问

    if p.BMI() < 23:  # 通过方法访问bmi变量值
        print("Normal Weight!")
    else:
        print("Over Weight!")
