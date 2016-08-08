# -*- coding: utf-8 -*-
"""
    六六的python_homework
    写法的一些注意事项,避免编译器上一些提示:
    1.语句后的注释前,空两格
    2.: 或者 #后,加1空格
    3.def前最好有两空行
"""

########################
# 1.原始数据类型&操作符
########################

# 数字类型
3  # 直接表示为"3"

# 简单的算数
1 + 1  # 1+1=>2
8 - 1  # 8-1=>7
10 * 2  # 10*2=>20
35 / 5  # 35/5=>7

# 整数的除法自动取整
5 / 2  # 5/2=2.5=>2

# 精确的除法(浮点数)
2.0  # 浮点数
11.0 / 4.0  # =>2.75  对比11 / 4 = 2可显示精确结果

# 括号(最高优先级)
(1 + 3) * 2  # 1+3=4,4*2=>8

# 布尔值
True
False

# 取非(not)
not True  # => False
not False  # => True

# 相等
1 == 1  # =>True
2 == 1  # =>False

# 不等
1 != 1  # =>False
2 != 1  # =>True

# 其他比较符
1 < 10  # =>True
1 > 10  # =>False
2 <= 2  # =>True
2 >= 2  # =>True

# 可连起来写的比较运算
1 < 2 < 3  # =>True
2 < 3 < 2  # =>False

# ""/''表示字符串,含义相同
" This is a string. "
" This is also a string. "

# 字符串的拼接
" Hello " + " World! "  # => ' Hello  World! '

# 字符串也是字符列表,可取其中的某个字符
"This is a string"[0]  # => 该字符串第0位字符是'T' ;若将0改为1,取值为'h';改为2,取值为'i'...
# 若为"This is a string"[0] 则输出结果为'0';改为1,取值为'T'.空格占1个字符

# %用于格式化字符串
"%s can be %s" % ("strings", "interpolated")
# =>'strings can be interpolated'

# 推荐使用format方法格式化字符串,也可用变量名代替数字
"{0} can be {1}".format("strings", "formatted")
# ==>'strings can be formatted'
"{name} wants to eat {food}".format(name="Bob",food="lasagna")
# =>'Bob wants to eat lasagna'

# None 是对象,不可用相等'=='符号与之进行比较,要用'is'
None  # => None,输出为空
'etc' is None  # =>False
None is None  # =>True
# 'is'用来比较对象的相等性

# None, 0, 和空字符串都被算作'False',其他的均为 True
0 == False  # => True
"" == False  # => True
1 == False  # => False

########################
# 2.变量和集合
########################

# 输出
print "I'm Python. Nice to meet you!"

# 变量赋值,无需事先说明建议小写字母和下划线命名变量
some_var = 5
print some_var  # =>5

# 访问未赋值变量,抛出异常
some_other_var  # NameError: name 'some_other_var' is not defined

# if语句作为表达式
"yahoo!" if 3 > 2 else 2  # 若if为true,输出'yahoo',若为false,输出2

# 保存序列
li = []
# 可直接初始化列表
other_li = [4, 5, 6]  # print other_li[0]=>4
# 列表末尾添加元素
li.append(1)  # li列表中现在有的元素为:[1]  print li[0]=>1
li.append(2)  # li列表中现在有的元素为:[1,2]  print li[1]=>2
li.append(4)  # li列表中现在有的元素为:[1,2,4]  print li[2]=>4
li.append(3)  # li列表中现在有的元素为:[1,2]  print li[3]=>3
# 列表末尾移除元素
li.pop()  # 最末尾元素为3,被移除,此时print li => [1, 2, 4]
# 重新加入
li.append(3)  # print li => [1, 2, 4, 3]

# 访问列表
li[0]  # => 1
# 访问最后一个元素
li[-1]  # =>3
# 抛出异常(越界)
li[4]  # 抛出越界异常"IndexError: list index out of range"


# 切片语法(列表的索引访问),左闭右开区间
li[1:3]  # =>[2, 4]
# 省略开头的元素
li[2:]  # =>[4, 3]
# 省略末尾的元素
li[:3]  # =>[1, 2, 4] 若为li[0:3]也是相同结果

# 删除特定元素
del li[2]  # li[2]=4,删除后列表变为[1,2,3]

# 合并列表,不会改变两个列表
li + other_li  # [1, 2, 3]+[4, 5, 6]=[1, 2, 3, 4, 5, 6]

# 拼接合并列表
li.extend(other_li)  # li = [1, 2, 3, 4, 5, 6]

# 是否在列表中(in)
1 in li

# 返回长度
len(li)  # => 6

# 元祖,类似于列表,但不可改变
tup = (1, 2, 3)
tup[0]  # => 1
tup[0] = 3  # 类型错误

# 适用于元祖的列表操作
len(tup)  # => 3
tup + (4, 5, 6)  # =>(1, 2, 3, 4, 5, 6)
tup[:2]  # =>(1,2)
2 in tup  # True  4 in tup =>false

# 可将元祖解包赋给多个变量
a, b, c = (1, 2, 3)
# 若不加括号,会被自动视为元祖
d, e, f = 4, 5, 6
# 交换数字
e, d = d, e  # d= 4, e = 5 => e = 4, d =5

# 字典
# 存储映射关系字典
empty_dict = {}  # =>empty_dict = {}
# 字典初始化
filled_dict = {"one": 1, "two": 2, "three": 3}  # filled_dict = {'one': 1, 'three': 3, 'two': 2}
# 字典中括号访问元素
filled_dict["one"]  # filled_dict["one"]=> 1
# 保存所有键在列表中,键的顺序不唯一
filled_dict.keys()  # ['three', 'two', 'one']
# 把所有的值保存在列表中,和键的顺序相同
filled_dict.values()  # => [3, 2, 1]
# 判断键是否存在
"one" in filled_dict  # =>True 若"one"不打双引号 => NameError: name 'one' is not defined
1 in filled_dict  # =>  False
# 查询不存在的键
filled_dict["four"]  # => KeyError: 'four'
# 用get来避免KeyError
filled_dict.get("one")  # => 1
filled_dict.get("four")  # => 返回为空,None
# get方法支持在不存在的时候返回一个默认值
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4)  # => 4
# setdefault => 更安全的添加字典元素的方法
filled_dict.setdefault("five", 5)  # =>5
filled_dict.setdefault("five", 6)  # =>5 为何此处仍是5?

# 集合存储无顺序的元素
empty_set = set()
# 初始化一个集合
some_set = set([1, 2, 2, 3, 4])  # => {1, 2, 3, 4}
filled_set = {1, 2, 2, 3, 4}  # =>{1, 2, 3, 4}
# 向集合添加元素
filled_set.add(5)  # => {1, 2, 3, 4, 5}
# & 用于计算集合的交
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}
# | 用于计算集合的并
filled_set | other_set  # =>{1, 2, 3, 4, 5, 6}
# - 用户计算集合的差(A-B),仅计算A集合中与B不同的元素
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}
# 判断元素是否存在集合中(in)
2 in filled_set  # => True
10 in filled_set  # => False


########################
# 3.控制流程
########################
# 新建变量
some_var = 5
# if语句,注意缩进
if some_var > 10:
    print "some_var is totally bigger than 10."
elif some_var < 10:
    print "some_var is smaller than 10."
else:
    print "some_var is indeed 10."
# => some_var is smaller than 10.
# for循环,遍历列表
for animal in ["dog", "cat", "mouse"]:
    print "%s is a mammal" % animal
"""
输出:
dog is a mammal
cat is a mammal
mouse is a mammal
"""
# range(number) 返回从0到给定数字的列表
for i in range(4):
    print i
"""
输出:
0
1
2
3
"""
# while循环
x = 0
while x < 4:
    print x
    x += 1
"""
输出:
0
1
2
3
"""
# 用 try/except 块处理异常
try:
    # 用raise 抛出异常
    raise IndexError("This is an index error")
except IndexError as e:
    pass  # 通常pass还可以做一些恢复工作
# => 输出为空

########################
# 4.函数
########################
# 新建函数(def)
# def新建函数时,前面最好两行空格


def add(x, y):
    print "x is %s and y is %s" % (x, y)
    return x+y
    # 用return来返回值
# 调用函数(带参数)
add(5, 6)
"""
输出:"x is 5 and y is 6"11
返回:11
"""
# 调用函数(关键字赋值),无需考虑赋值顺序
add(y=6, x=5)
"""
同上,输出:"x is 5 and y is 6"11
返回:11
"""
# 定义接受多个变量的函数,变量按顺序排列


def varargs(*args):
    return args
# 调用
varargs(1, 2, 3)  # =>(1, 2, 3)
varargs(2, 6, 5, 7)  # =>(2, 6, 5, 7)
# 定义接受多个变量的函数,变量按关键字排列


def keyword_args(**kwargs):
    return kwargs
# 调用
keyword_args(big="foot", loch="ness")
# => {'big': 'foot', 'loch': 'ness'}
# 定义函数为两种形式


def all_the_args(*args, **kwargs):
    print args
    print kwargs
# 调用
all_the_args(1, 2, a=3, b=4)
"""
输出:
(1, 2)
{'a': 3, 'b': 4}
"""
# 调用函数时,可将元组和字典作为参数
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)  # =>(1, 2, 3, 4){}   等价于foo(1, 2, 3, 4)
all_the_args(**kwargs)  # =>(){'a': 3, 'b': 4}  等价于foo(a=3,b=4)
all_the_args(*args, **kwargs)  # 等价于foo(1, 2, 3, 4, a=3, b=4)
"""
输出:
(1, 2, 3, 4)
{'a': 3, 'b': 4}
"""
# 函数


def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)  # => 13
# 匿名函数
(lambda x: x > 2)(3)  # => True
# 内置高阶函数
map(add_10, [1, 2, 3])  # => [11, 12, 13]
filter(lambda x: x > 5, [3, 4, 5, 6, 7])  # => [6, 7]
# 用列表法巧妙引用高阶函数
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

########################
# 5.类
########################
# 新建从object类中集成的类


class Human(object):
    # 类属性,所有类的对象共享
    species = "H.sapiens"

    # 基本构造函数
    def __init__(self, name):
        # 给对象成员属性赋参数
        self.name = name

    # 成员方法,参数需要有self
    def say(self,msg):
        return "%s: %s" % (self.name, msg)

    """
    类方法由所有类的对象共享
    在调用时,将类本身传给第一个参数
    """
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法无需类和对象的引用即可调用方法
    @staticmethod
    def grunt():
        return "*grunt*"

# 实例化一个类
i = Human(name="Ian")
print i.say("hi")     # => Ian: hi

j = Human("Joel")
print j.say("hello")  # => Joel: hello
# 访问类的方法
i.get_species()  # => 'H.sapiens'
# 改变共享属性
Human.species = "H. neanderthalensis"
i.get_species()  # => 'H.neanderthalensis'
j.get_species()  # => 'H.neanderthalensis'

# 访问静态变量
Human.grunt()  # => '*grunt*'

########################
# 6.模块
########################
# 导入其他模块
import math
print math.sqrt(16)   # => 4.0

# 从模块中导入特定函数
from math import ceil, floor
print ceil(3.7)
print floor(3.7)

# 从模块中导入所有的函数(不推荐使用)
from math import *
# 简写模块名
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# 可创建&导入自己的模块,模块的名字就和文件的名字相同
# 也可以通过以下方法查看模块中有什么属性和方法
import math
dir(math)


