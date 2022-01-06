import re

'''
数据解析
三种解析方式
    1、re解析    #运行速度最快、效率高、准确性搞。 但是上手难度高
    2、bs4解析   #代码简单、但执行效率不高
    3、xpath解析  #语法简单，容易上手


1   .       匹配除换行符以外的所有字符
2   \w      匹配字符或数字或下划线
3   \s      匹配任意的空白字符
4   \d      匹配数字
5   \n      匹配一个换行符
6   \t      匹配一个制表符
7
8   ^       匹配字符串的开始
9   $       匹配字符串的结尾
10
11  \W      匹配非字符或数字或下划线
12  \D      匹配非数字
13  \S      匹配非空白字符
14  a|b     匹配字符a或者字符b
15  ()      匹配括号内的表达式，也表示一个组
16  [...]   匹配字符组中的字符
17  [^...]  匹配除了字符组中字符的所有字符

量词：控制前面的元字符出现的次数
1   *       重复零次或更多次
2   +       重复一次或更多次
3   ?       重复零次或者1次
4   {n}     重复n次
5   {n,}    重复n次或更多次
6   {m,n}   重复md到n次

贪狼匹配和惰性匹配
1   .*      贪狼匹配
2   .*?     惰性匹配，# 在爬虫中使用较多

在线正则表达式：https://tool.oschina.net/regex
'''
s1 = '玩儿吃鸡游戏，晚上一起上游戏，干嘛呢？打游戏啊'
print('贪狼模式：',re.findall(r'玩儿.*游戏',s1))
print('惰性模式：',re.findall(r'玩儿.*?游戏',s1))



# #findall:匹配字符串中所有的符合正则的内容，返回list
li = re.findall(r"\d+","我的电话是10086，我女朋友的电话是10010")
print(li)

#finditer:匹配字符串中所有的内容，返回迭代器,从迭代器中拿到内容需要 .group()
rest = re.finditer(r"\d+","我的电话是10086，我女朋友的电话是10010")
for it in rest:
    print("电话:",it.group())

#search:全文检索，找到一个结果就返回。返回Match对象，拿数据需要 .gruop()
rest = re.search(r"\d+","我的电话是10086，我女朋友的电话是10010")
print(rest.group())

#match:从头开始匹配，返回Match对象。拿数据需要 .gruop()
rest = re.match(r"\d+","10086我的电话是10086，我女朋友的电话是10010")
print(rest.group())

#预加载正则表达式,   re.S:让 . 能匹配换行符
obj = re.compile(r"<div class = '.*?'><span id = '\d+'>.*?</span></div>",re.S)


s = '''
<div class = 'jay'><span id = '1'>土豆</span></div>
<div class = 'jj'><span id = '2'>地瓜</span></div>
<div class = 'sda'><span id = '3'>红薯</span></div>
<div class = 'fbd'><span id = '4'>山药</span></div>
<div class = 'sde'><span id = '5'>白菜</span></div>
'''

re_obj = re.compile(r"<div class = '.*?'><span id = '\d+'>.*?</span></div>",re.S)   #测试全部匹配 s
res = re_obj.finditer(s)
for item in res:
    print(item.group())

#通过(?P<name>正则表达式)，提取想要的内容到name中
re_obj1 = re.compile(r"<div class = '(?P<name>.*?')><span id = '(?P<id>\d+)'>(?P<nr>.*?)</span></div>",re.S)
res1 = re_obj1.finditer(s)
for it in res1:
    print(it.group("name"),'---',it.group("id"),'---',it.group("nr"))
