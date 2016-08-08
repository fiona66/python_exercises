# -*- coding: utf-8 -*-
# 中文用户需要声明以上部分的代码,同时文件本身也需要存储成UTF-8编码
import os
# 导入其他模块代码(os.py)


def main():  # def前面最好空两格
    print 'Hello World!'

    print "这里是Alice\'的问候."
    print '这是Bob\'的问候.'

    # 函数调用,声明在之后
    foo(5, 10)

    # 字符可乘
    print '=' * 10
    print '这将直接执行'+os.getcwd()  # +连接符,os.getcwd()调用os模块的函数

    # 变量实例化
    counter = 0
    counter += 1

    # 内置列表类型对象,可包含不同类型数据,甚至包含其他列表对象
    food = ['苹果', '杏子', '李子', '梨']
    for i in food:  # for in 循环语句使用冒号结束声明
        print '俺就爱整只:'+i

    print '数到10'
    for i in range(10):
        print i


# 函数声明,冒号结束声明
def foo(param1, secondParam):
    res = param1+secondParam
    print '%s 加 %s 等于 %s' % (param1, secondParam, res)  # 括号前的%前后最好空格
    # 冒号结束判断句,在if...elif..else行最后
    if res < 50:
        print '这个'
    # and/or逻辑运算符,不适用 && 和 ||
    elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):
        print '那个'
    else:
        print '恩...'
    return res  # 这是单行注释
    '''这是
    多行注释'''

# 调用主函数main()
if __name__ == '__main__':
    main()
