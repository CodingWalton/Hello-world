# coding=gbk   
#python脚本出现中文注释需要加上一行内容防止报错

###第二章变量
message="Hello World!"
print (message)

name="abc lovepeace"
print (name.title())  #每个单词首字母改大写
print (name.upper())    #字符串全改大写
print (name.lower())  #字符串全改小写

first_name="liu"
second_name="ziming"
full_name=first_name+" "+second_name
print(full_name)         #python中使用'+'号来合并字符串 可以在变量赋值的时候任意拼接或者print的时候任意拼接

print("\tpython\npython2")  #\t在字符串前加空白 制表符  \n换行符

words=" python "
words1=words.rstrip()  #剔除末尾空白
words2=words.lstrip()  #剔除开头空白
words3=words.strip()  #剔除两头空白
print("\t",words,"\n\t",words1,"\n\t",words2,"\n\t",words3)

age=23
message="happy" +str(age)+"rd birthday"  #str将非字符串的类型转化为字符串类型
print(message)

print(0.2+0.3)

####第三章列表
animals=["dog","cat","tiger"]
print(animals)
print(animals[0])
print(animals[0].title()," ",animals[1].title()," ",animals[1].title())
print(animals[-1].title()) #直接访问最后一个列表元素

message="I love " + animals[-1]  #可以直接使用列表的值做变量操作
print(message)

animals=["dog","cat","tiger"]
print(animals)
animals[0]="elephant"  #列表元素的修改
print(animals)
animals.append('dog')  #append()将元素添加至列表末尾
print(animals)
animals.insert(3,'bird') #insert(i,'')将元素插入值第i个元素的位置，包括i元素以及后面的元素均右移一位
print(animals)
del animals[0]    #del 删除对应位置的列表元素
print(animals)
poped_animal = animals.pop()   #pop()能删除列表末尾的元素，并且将被删元素其作为返回值返回
print("\t",animals,"\n\t",poped_animal)
poped_animal = animals.pop(0)  #pop(i)能删除对应位置的元素，并将被删除元素返回
print("\t",animals,"\n\t",poped_animal)
animals=["dog","cat","tiger"]
print(animals)
animals.remove('dog')  #remove()若不知道要删除元素的位置指导删除对象的名称，则直接使用remove通过名称删除列表元素  注意：只能删一个，若列表中多个名字重复的变量remove也只能删除第一个出现的元素
print(animals)

#列表排序
element = ['animal','feeling','car','quantity','box','garbage']
print(element)
element.sort()   #sort()按字母顺序永久性排列
print(element)
element.sort(reverse=True)  #sort(reverse=Ture)按字母顺序倒序永久性排列
print(element)

print(sorted(element))   #临时按字母顺序排序
print(sorted(element,reverse=True))   #临时按字母倒序排序

element = ['animal','feeling','car','quantity','box','garbage']
print(element)
element.reverse()   #reverse()反转列表元素
print(element)

print(len(element))  #len()返回列表长度

###第四章 操作列表

word_lists = ['a','b','d','e','c']
for word_list in word_lists:
	print(word_list)
	print(word_list.title()+'very good!\n')
print('Thank you everyone very much !!!')

##数值列表
for value in range(1,5):    #range(1,5)产生数字1到4
	print(value)

numbers = list(range(1,6))   #联合list he range创建一个数值列表  list将数字转换为列表
print(numbers)

even_numbers = list(range(0,13,2)) #使用range可以指定步长
print(even_numbers)

squares=[]   #定义一个空列表  此例通过range和for循环创造了一个1到10的平方的数字列表
for value in range(1,11):
	square=value**2     # **表示乘方
	squares.append(square)  #新值加到列表末尾
	print(squares)
print(squares)

print(min(squares))    #min返回数字列表最小值
print(max(squares))    #max返回数字列表最大值
print(sum(squares))    #sum返回数字列表求和值

#列表解析
cubes = [value**3 for value in range(1,11)]  #快速生成数字列表的方法
print(cubes)
#millions=[value for value in range(1,1000000)]
#print(millions)

#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])   #输出0，1，2编号组成的列表
print(players[2:4])   #输出2，3编号组成的列表
print(players[:2])    #输出从开始到1号编号组成的列表
print(players[2:])    #输出从2号编号到列表末尾组成的列表
print(players[-3:])   #输出从倒数第三位到末尾组成的列表

#遍历切片
for player in players[:2]:
	print(player)
#复制列表
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
copy_players = players[:]  #对被复制列表做切片，切片不加起始和终止的索引，即可完全复制列表
print(copy_players)

duplicate_players = players  #这里并不是对players进行了复制，而是将duplicate_players指向了players列表，相当于地址相同，均指向同一个列表  
print(duplicate_players)


#元组   元组的值不可修改
constants = (0,1)
print(constants)
print(constants[0],constants[1])
#constant[0]=50   错误语句 元组的值不可修改
constants1 = ('a','b')
print(constants1)
print(constants1[0],constants1[1])

for constant in constants:    #遍历元组
	print(constant)

constants = (0,1)
constants = (200,2)   #元组的值虽然不可修改，但是可以直接赋值
constants1 = ('a','b')
constants1 = ('c','d','e')
print(constants,constants1)

###if语句
phones = ['apple','Xiaomi','Samsung','honor','oppo']
for phone in phones:
	if phone == 'apple':   
		print(phone.upper())
	else:
		print(phone.title())

phones = ['APple','Xiaomi','SamSung','hoNor','Oppo']
for phone in phones:
	if phone.lower() == 'apple':  #程序设计中，不要考虑大小写，将对比词使用lower()函数全部小写化进行比较，可以避免很多麻烦   
		print(phone.upper())
	else:
		print(phone.title())
	
temp='cad'
if temp != 'cad' :
	print('I got it !')
else:
	print('Joking me!')

rabbit_num = 50
tiger_num = 20
if (rabbit_num <= 45) or (tiger_num >=10):    #使用 and or 处理多个条件
	print ('That is not correct answer')
else:
	print ('correct!')

#条件检查 == != > < >= <= (and or) in  not in   使用条件检查反馈值为 true 和false
word = 'ele'
liss = ['a','b','ele']
age = 18
print('\t',age == 18,'\n\t',age!=18,'\n\t',word == 'ele','\n\t',word != 'ele')
print('\t',word in liss,'\n\t',word not in liss)
#布尔表达式
#布尔值有true false两种一般用于记录条件
active = True
progress = False
if active != True:
	print ('I am ok!')
else:
	print ('Not yet!')

#if-elif-else
age = 10
if age > 18:
	print('adult')
elif age > 12 and age <= 18:
	print('teenager')
else:
	print('child')

if age < 4:
	price = 0
elif age < 12:
	price = 20
elif age < 18:
	price = 40
elif age < 65:
	price = 80
else:
	price = 0
print('You need to pay for about',price)

#使用if处理列表
#检查列表是否为空
new_lists = []
if new_lists:         #空列表直接放入if条件句，返回False  非空列表返回True  可以作为列表处理的先决判断，以防空列表索引报错
	print('Not empty!')
else:
	print('Empty!')
#在if条件句中进行遍历
old_lists = ['a','b','c']
new_lists = ['a','b','e']
for new_list in new_lists:
	if new_list in old_lists:   #直接在if条件中使用遍历，存在返回True，遍历不存在返回False
		print ('Available')
	else:
		print ('Unavailable')





