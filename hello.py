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



###字典
dic0 = {'animal':'dog','age':2}     
dic = {'color':'red','points':dic0}   #字典是一系列键值对，与键关联的值可以是数字、字符串、列表乃至字典。可将任何python对象用作字典的值
print( dic['color'] ,dic['points'])   #键值之间用：，键值对之间用，  字典十分类似C里的结构体
#添加键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['X_pos'] = 0     #添加键值对的方式
alien_0['Y_pos'] = 25
print(alien_0)
#创建空字典
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
#修改字典的值
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print("Its color has changed into",alien_0['color']+'. The point is',str(alien_0['points']),'!')
#删除键值对
print(alien_0)
del alien_0['points']
print(alien_0)
#用类似对象共同属性组成字典
favorite_languages = {    #对于较长的字典采用这种输入格式
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
print(favorite_languages)

##遍历字典
user_0 = {
    'username': 'efermi',
	'first': 'enrico',
    'last': 'fermi',
    }
for k,v in user_0.items():   #使用item()遍历字典所有键值对
	print('\nKeys:',k)
	print('\nValue:',v)
for k in user_0.keys():      #使用keys()遍历字典中所有键
	print(k.title())
for k in user_0:             #遍历字典名时，默认遍历所有的键，与keys()时一样
	print(k.title())
for v in user_0.values():    #使用values()遍历字典所有值
	print(v.title())


#按顺序遍历字典所有键
user_0 = {
    'username': 'efermi',
	'first': 'enrico',
    'last': 'fermi',
    }
for k in sorted(user_0.keys()):
	print(k+'\n')

favorite_languages = {    
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
print(favorite_languages)
for language in favorite_languages.values():
	print(language)           #存在重复项
for language in set(favorite_languages.values()):
	print(language)           #set()可以直接剔除重复元素构成独一无二的元素构成的set集合 
	                          #set集合类似于列表，但元素组成独一无二
##嵌套
alien_0 = {'color': 'green', 'points': 5}     
alien_1 = {'color': 'yellow', 'points': 10}  
alien_2 = {'color': 'red', 'points': 15} 
aliens = [alien_0, alien_1, alien_2]    #每个外星人都是一个字典，外星人集成一个列表
for alien in aliens:      
	print(alien)

a = [0,'a',{'color': 'yellow', 'points': 10}]  #列表可由任意形式组成
print(a[2]['color'])

aliens=[]
for i in range(30):     #产生30个外星人，由30个字典组成列表
	alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(alien)
for alien in aliens[:5]:   #切片，从一开始到编号5前一个，也即是编号4
	print(alien)

#也可在字典中储存列表
favorite_languages = {    
	'jen': ['python','c'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell']
	}
for n,l in favorite_languages.items():
	print(n.title()+"'s favorite languages are")
	for ll in l:
		print('\n',ll.title())

#在字典中储存字典	
users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton'
		},
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris'
		}
	}

#####用户输入和while循环
'''
###input()工作原理
message = input("Tell me something, and I will repeat it back to you: ") 
input暂停程序，等待用户输入并将输入值存储到message
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see." 
prompt += "\nWhat is your first name? " 
name = input(prompt) 
print("\nHello, " + name + "!")
#使用input赋值会将输入值自动以字符串的形式存储

age = input('How old are you ? ')
age = int(age)   #将数字的字符串表示转换为数值表示 
if age >= 18:
	print('You are an adult !')
else:
	print ('So young are you !')
'''
#取余(求模)运算符 %
print(15%10,2%2)

###While循环
#name = ['0']
#while name:        #这里非空列表返回True，所以无限循环
#	name=name
	
#使用break退出循环
age = 18
while True:
	age+=5
	if age > 50:
		break
	else:
		print(age)
#使用continue跳过本次循环
nums = []
num = 0
while num < 10:
	num+=1
	if num % 2 == 0:
		continue
	nums.append(num)	
	print('Odd num get '+str(num))
print(nums)

##使用while处理列表和字典
#移动列表元素
unconfirmed_users = ['alice', 'brian', 'candace']  
confirmed_users = []
while unconfirmed_users:    #直到unconfirmed_users为空，while停止运行
	temp = unconfirmed_users.pop()
	confirmed_users.append(temp)
print(confirmed_users)
#删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
num = 0
for a in pets:
	if a == 'cat':
		print(a)
		num+=1
print(num)
while 'cat' in pets:
	pets.remove('cat')
print(pets)
'''
#通过用户输入填充字典
information = {} 
signal = True
while signal:
	justice = input ('Do you want to answer the questions?(y/n)')
	if justice.lower() == 'y':
		signal = True
	elif justice.lower() == 'n':
		signal = False
		break
	else:
		continue
	name = input ("What's your name?")
	information[name] = input ('How old are you ? ')
print(information)
'''

#####函数
def greet_user (username):
    '''显示简单问候'''
    print('Hello!',username)
def favorite_book (book):
    print('My favorite book is '+book)
    
greet_user('Jack')
favorite_book ('child book')
#位置实参
def describe_pet(animal_type, pet_name):
      """显示宠物的信息"""
      print("\nI have a " + animal_type + ".")
      print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')  #位置对应

#关键字实参   关键字实参不用对应形参位置
describe_pet(animal_type = 'hamster',pet_name = 'Jack')

#给形参提供默认值，在调用的时候可以省略输入实参
def favorite_book (book = 'English book'):
    print('My favorite book is '+book)
favorite_book()

#函数返回值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名""" 
    full_name = first_name + ' ' + last_name      
    return full_name.title()  
musician = get_formatted_name('jimi', 'hendrix')  
print(musician)

def get_formatted_name2(first_name,last_name,middle_name = ''):
    if middle_name == '':
        fix_name = first_name + ' ' + last_name
    else:
        fix_name = first_name + ' ' + middle_name + ' ' + last_name
    return fix_name.title()
name = get_formatted_name2('Jack','chen')
print(name)

#函数可以返回列表、字典等复杂的数据结构
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""     
    person = {'first': first_name, 'last': last_name}     
    return person  
musician = build_person('jimi', 'hendrix') 
print(musician)

#结合while循环与函数做一个交流窗
'''
def name_combination (first_name,last_name):
    fix_name = first_name + ' ' + last_name
    return fix_name
while True:
    print('Tell me your name','\n',"Enter 'q' at any time to quit")
    f_name = input("What's your first_name? ")
    if f_name == 'q':
        break
    l_name = input("What's your last_name? ")
    if l_name == 'q':
        break
    fix = name_combination (f_name,l_name)
    print('Hello ! '+fix)
'''
#形参为列表
def greet_users(names):      
    """向列表中的每位用户都发出简单的问候"""      
    for name in names:          
        msg = "Hello, " + name.title() + "!"          
        print(msg) 
usernames = ['hannah', 'ty', 'margot']  
greet_users(usernames)

#切片表示传递列表实参，防止函数永久性改变列表
# funtion_name(list_name[:])      #使用切片表示，将列表的副本传递给函数，这样不会改变原列表！！！

#传递任意数量的实参
def make_pizza(*toppings):       #形参前加一个*将toppings创建一个空元组，并将所有实参收集进入这个元组
    """打印顾客点的所有配料"""    
    print(toppings) 
make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#位置实参+任意数量实参
def make_pizza(size, *toppings):    
    """概述要制作的比萨"""    
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")    
    for topping in toppings:        
        print("- " + topping) 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#使用任意数量的关键字实参 （传递任意数量的键值对，或传递字典）
def build_profile(first, last, **user_info):        #user_info前的**两个星号，使python建立了一个空字典来储存任意数量的键值对
    """创建一个字典，其中包含我们知道的有关用户的一切"""      
    profile = {}
    profile['first_name'] = first      
    profile['last_name'] = last     
    for key, value in user_info.items():         
        profile[key] = value      
    return profile  

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')    #传递任意数量的键值对
print(user_profile)

##在模块中储存函数  （类似于Matlab的.m文件储存函数）
#导入函数所在的模块    该模块与主程序在同一个目录
import makepizza    
makepizza.make_pizza(16, 'pepperoni')  
makepizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#导入模块中的函数   
from makepizza import make_pizza
make_pizza(16, 'pepperoni')  
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#导入模块中任意数量的函数，用,分隔开
#    from module_name import function_0, function_1, function_2
#导入函数时使用as给导入函数指定别名
from makepizza import make_pizza as mp
mp(16, 'pepperoni')  
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#使用as给模块指定别名
import makepizza as p          #通用语法：import module_name as mn
p.make_pizza(16, 'pepperoni')  
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#使用*将模块内的所有函数全部导入
from makepizza import *            
#通用语法:import module_name *
#这种方法可以直接使用函数名，不需要  module_name.function_name 的方法调用模块内的函数
#但建议不要使用此方法，若函数名字冲突会出现意料之外的错误
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


######类

###方法
#类中的函数成为方法    
#所有 方法 的定义均包含self形参 ，该形参必不可少，
#每个与类相关联的方法调用都自动传递实参self，他是一个指向实例本身的引用，让实例能够访问类中的属性和方法
##创建一个Dog类
class Dog():
    def __init__(self,name,age):   #__init__为双下划线！！！ self必不可少并且是第一个形参，在创建Dog类给一个实例的时候，Dog类会先调用方法__init__将其余参量进行相关赋值操作
        self.name = name           #以self为前缀的变量都可供类中的所有方法使用，还可以通过类的实例访问这些变量，可以通过实例访问的变量成为 属性 ！！！
        self.age = age
    def sit(self):
        print(self.name.title()+' is now sitting !')
    def roll_over(self):
        print(self.name.title()+' rolled over !')

my_dog = Dog('Jack',6)
print(my_dog.name.title(),'  ',str(my_dog.age))     #通过句点的形式访问属性 name 和 age
#调用方法(类中的函数)
my_dog.sit()                  #通过句点的形式调用方法
my_dog.roll_over()
#可通过Dog类创建多个实例
dog1 = Dog('John',3)
dog2 = Dog('Bob',2)
dog1.sit()
dog2.roll_over()

##创建一个Car类
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0    #给属性设置默认值，就无需设置提供初始值的形参
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model    #使用 self. 可以在方法中访问属性的值
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):      #建立一个方法来修改属性的值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer !')
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""  
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You can not roll back an odometer !')
    def fill_gas_tank(self):
        print('The gas tank has been filled !')
         

my_new_car = Car('audi', 'a4', 2016)  
print(my_new_car.get_descriptive_name())  
my_new_car.read_odometer()

#修改属性的值
# 1直接修改属性值
my_new_car.odometer_reading = 23   #直接访问并进行修改
my_new_car.read_odometer()
# 2通过方法修改属性的值  在Car类里增添一个方法来修改对应属性的值
my_new_car.update_odometer(50)
my_new_car.read_odometer()
# 3通过方法递增属性的值
my_used_car = Car('subaru', 'outback', 2013)  
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(-50)
my_used_car.read_odometer()

###继承

#创建子类  创建子类时，父类必须包含在当前文件中，且位于子类前面

##将实例用作类中的属性  
class Tyre ():
    def __init__(self,weight=50,height=30):
        self.weight = weight
        self.height = height
    def decribe_tyre (self):
         print("This car's tyre is " + str(self.weight) + " Kg.")
         print("This car's tyre is " + str(self.height) + " m.")


class ElectricCar (Car):        #定义子类名称后，括号内必须指定父类的名称
    def __init__(self,make,model,year):         #方法__init__要接受创建Car实例所需的信息，也就是括号内的形参
        '''先super初始化父类属性，然乎在初始化子类独特属性'''
        super().__init__(make,model,year)  #super()函数将父类子类相连，让子类实例包含父类的所有属性，父类也叫超类 注意：此处不能加入self形参
        self.battery_size = 70             #子类独特的属性
        self.tyre = Tyre()                 #将tyre的实例作为ElectricCar类的属性
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def fill_gas_tank(self):               #重写父类的方法(函数)，直接将父类的原方法重写就可以 ，将忽略父类的方式写法而直接认可子类方法的新写法
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2016)  
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.tyre.decribe_tyre()               #调用实例my_tesla的属性中的实例tyre的属性decribe_tyre

###从模块中导入类
from car import CCar
###从模块中导入任意数量的类
from car import CCar,CCar1
###导入整个模块  然后采用句点的形式访问需要的类   导入模块后可以采用句点的形式使用函数和类
import car
my_car = car.CCar('volkswagen', 'beetle', 2016)
###导入所有类    将模块car中的所有包括函数和类全部导入，这样可以不用使用句点的形式表示，可以直接使用名称
#加*的方式等同于将模块直接复制，所以存在重复定义的可能，若只是导入模块使用类和函数的前提是模块名＋句点，所以不存在重复定义的可能
''' from car import * '''

# !!! 也可以在模块中导入另一个模块 !!! 非常类似于C中的 include
































	
	






