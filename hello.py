# coding=gbk   
#python�ű���������ע����Ҫ����һ�����ݷ�ֹ����

###�ڶ��±���
message="Hello World!"
print (message)

name="abc lovepeace"
print (name.title())  #ÿ����������ĸ�Ĵ�д
print (name.upper())    #�ַ���ȫ�Ĵ�д
print (name.lower())  #�ַ���ȫ��Сд

first_name="liu"
second_name="ziming"
full_name=first_name+" "+second_name
print(full_name)         #python��ʹ��'+'�����ϲ��ַ��� �����ڱ�����ֵ��ʱ������ƴ�ӻ���print��ʱ������ƴ��

print("\tpython\npython2")  #\t���ַ���ǰ�ӿհ� �Ʊ��  \n���з�

words=" python "
words1=words.rstrip()  #�޳�ĩβ�հ�
words2=words.lstrip()  #�޳���ͷ�հ�
words3=words.strip()  #�޳���ͷ�հ�
print("\t",words,"\n\t",words1,"\n\t",words2,"\n\t",words3)

age=23
message="happy" +str(age)+"rd birthday"  #str�����ַ���������ת��Ϊ�ַ�������
print(message)

print(0.2+0.3)

####�������б�
animals=["dog","cat","tiger"]
print(animals)
print(animals[0])
print(animals[0].title()," ",animals[1].title()," ",animals[1].title())
print(animals[-1].title()) #ֱ�ӷ������һ���б�Ԫ��

message="I love " + animals[-1]  #����ֱ��ʹ���б��ֵ����������
print(message)

animals=["dog","cat","tiger"]
print(animals)
animals[0]="elephant"  #�б�Ԫ�ص��޸�
print(animals)
animals.append('dog')  #append()��Ԫ��������б�ĩβ
print(animals)
animals.insert(3,'bird') #insert(i,'')��Ԫ�ز���ֵ��i��Ԫ�ص�λ�ã�����iԪ���Լ������Ԫ�ؾ�����һλ
print(animals)
del animals[0]    #del ɾ����Ӧλ�õ��б�Ԫ��
print(animals)
poped_animal = animals.pop()   #pop()��ɾ���б�ĩβ��Ԫ�أ����ҽ���ɾԪ������Ϊ����ֵ����
print("\t",animals,"\n\t",poped_animal)
poped_animal = animals.pop(0)  #pop(i)��ɾ����Ӧλ�õ�Ԫ�أ�������ɾ��Ԫ�ط���
print("\t",animals,"\n\t",poped_animal)
animals=["dog","cat","tiger"]
print(animals)
animals.remove('dog')  #remove()����֪��Ҫɾ��Ԫ�ص�λ��ָ��ɾ����������ƣ���ֱ��ʹ��removeͨ������ɾ���б�Ԫ��  ע�⣺ֻ��ɾһ�������б��ж�������ظ��ı���removeҲֻ��ɾ����һ�����ֵ�Ԫ��
print(animals)

#�б�����
element = ['animal','feeling','car','quantity','box','garbage']
print(element)
element.sort()   #sort()����ĸ˳������������
print(element)
element.sort(reverse=True)  #sort(reverse=Ture)����ĸ˳��������������
print(element)

print(sorted(element))   #��ʱ����ĸ˳������
print(sorted(element,reverse=True))   #��ʱ����ĸ��������

element = ['animal','feeling','car','quantity','box','garbage']
print(element)
element.reverse()   #reverse()��ת�б�Ԫ��
print(element)

print(len(element))  #len()�����б���

###������ �����б�

word_lists = ['a','b','d','e','c']
for word_list in word_lists:
	print(word_list)
	print(word_list.title()+'very good!\n')
print('Thank you everyone very much !!!')

##��ֵ�б�
for value in range(1,5):    #range(1,5)��������1��4
	print(value)

numbers = list(range(1,6))   #����list he range����һ����ֵ�б�  list������ת��Ϊ�б�
print(numbers)

even_numbers = list(range(0,13,2)) #ʹ��range����ָ������
print(even_numbers)

squares=[]   #����һ�����б�  ����ͨ��range��forѭ��������һ��1��10��ƽ���������б�
for value in range(1,11):
	square=value**2     # **��ʾ�˷�
	squares.append(square)  #��ֵ�ӵ��б�ĩβ
	print(squares)
print(squares)

print(min(squares))    #min���������б���Сֵ
print(max(squares))    #max���������б����ֵ
print(sum(squares))    #sum���������б����ֵ

#�б����
cubes = [value**3 for value in range(1,11)]  #�������������б�ķ���
print(cubes)
#millions=[value for value in range(1,1000000)]
#print(millions)

#��Ƭ
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])   #���0��1��2�����ɵ��б�
print(players[2:4])   #���2��3�����ɵ��б�
print(players[:2])    #����ӿ�ʼ��1�ű����ɵ��б�
print(players[2:])    #�����2�ű�ŵ��б�ĩβ��ɵ��б�
print(players[-3:])   #����ӵ�������λ��ĩβ��ɵ��б�

#������Ƭ
for player in players[:2]:
	print(player)
#�����б�
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
copy_players = players[:]  #�Ա������б�����Ƭ����Ƭ������ʼ����ֹ��������������ȫ�����б�
print(copy_players)

duplicate_players = players  #���ﲢ���Ƕ�players�����˸��ƣ����ǽ�duplicate_playersָ����players�б��൱�ڵ�ַ��ͬ����ָ��ͬһ���б�  
print(duplicate_players)


#Ԫ��   Ԫ���ֵ�����޸�
constants = (0,1)
print(constants)
print(constants[0],constants[1])
#constant[0]=50   ������� Ԫ���ֵ�����޸�
constants1 = ('a','b')
print(constants1)
print(constants1[0],constants1[1])

for constant in constants:    #����Ԫ��
	print(constant)

constants = (0,1)
constants = (200,2)   #Ԫ���ֵ��Ȼ�����޸ģ����ǿ���ֱ�Ӹ�ֵ
constants1 = ('a','b')
constants1 = ('c','d','e')
print(constants,constants1)

###if���
phones = ['apple','Xiaomi','Samsung','honor','oppo']
for phone in phones:
	if phone == 'apple':   
		print(phone.upper())
	else:
		print(phone.title())

phones = ['APple','Xiaomi','SamSung','hoNor','Oppo']
for phone in phones:
	if phone.lower() == 'apple':  #��������У���Ҫ���Ǵ�Сд�����Աȴ�ʹ��lower()����ȫ��Сд�����бȽϣ����Ա���ܶ��鷳   
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
if (rabbit_num <= 45) or (tiger_num >=10):    #ʹ�� and or ����������
	print ('That is not correct answer')
else:
	print ('correct!')

#������� == != > < >= <= (and or) in  not in   ʹ��������鷴��ֵΪ true ��false
word = 'ele'
liss = ['a','b','ele']
age = 18
print('\t',age == 18,'\n\t',age!=18,'\n\t',word == 'ele','\n\t',word != 'ele')
print('\t',word in liss,'\n\t',word not in liss)
#�������ʽ
#����ֵ��true false����һ�����ڼ�¼����
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

#ʹ��if�����б�
#����б��Ƿ�Ϊ��
new_lists = []
if new_lists:         #���б�ֱ�ӷ���if�����䣬����False  �ǿ��б���True  ������Ϊ�б�����Ⱦ��жϣ��Է����б���������
	print('Not empty!')
else:
	print('Empty!')
#��if�������н��б���
old_lists = ['a','b','c']
new_lists = ['a','b','e']
for new_list in new_lists:
	if new_list in old_lists:   #ֱ����if������ʹ�ñ��������ڷ���True�����������ڷ���False
		print ('Available')
	else:
		print ('Unavailable')



###�ֵ�
dic0 = {'animal':'dog','age':2}     
dic = {'color':'red','points':dic0}   #�ֵ���һϵ�м�ֵ�ԣ����������ֵ���������֡��ַ������б������ֵ䡣�ɽ��κ�python���������ֵ��ֵ
print( dic['color'] ,dic['points'])   #��ֵ֮���ã�����ֵ��֮���ã�  �ֵ�ʮ������C��Ľṹ��
#��Ӽ�ֵ��
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['X_pos'] = 0     #��Ӽ�ֵ�Եķ�ʽ
alien_0['Y_pos'] = 25
print(alien_0)
#�������ֵ�
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
#�޸��ֵ��ֵ
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print("Its color has changed into",alien_0['color']+'. The point is',str(alien_0['points']),'!')
#ɾ����ֵ��
print(alien_0)
del alien_0['points']
print(alien_0)
#�����ƶ���ͬ��������ֵ�
favorite_languages = {    #���ڽϳ����ֵ�������������ʽ
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
print(favorite_languages)

##�����ֵ�
user_0 = {
    'username': 'efermi',
	'first': 'enrico',
    'last': 'fermi',
    }
for k,v in user_0.items():   #ʹ��item()�����ֵ����м�ֵ��
	print('\nKeys:',k)
	print('\nValue:',v)
for k in user_0.keys():      #ʹ��keys()�����ֵ������м�
	print(k.title())
for k in user_0:             #�����ֵ���ʱ��Ĭ�ϱ������еļ�����keys()ʱһ��
	print(k.title())
for v in user_0.values():    #ʹ��values()�����ֵ�����ֵ
	print(v.title())


#��˳������ֵ����м�
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
	print(language)           #�����ظ���
for language in set(favorite_languages.values()):
	print(language)           #set()����ֱ���޳��ظ�Ԫ�ع��ɶ�һ�޶���Ԫ�ع��ɵ�set���� 
	                          #set�����������б���Ԫ����ɶ�һ�޶�
##Ƕ��
alien_0 = {'color': 'green', 'points': 5}     
alien_1 = {'color': 'yellow', 'points': 10}  
alien_2 = {'color': 'red', 'points': 15} 
aliens = [alien_0, alien_1, alien_2]    #ÿ�������˶���һ���ֵ䣬�����˼���һ���б�
for alien in aliens:      
	print(alien)

a = [0,'a',{'color': 'yellow', 'points': 10}]  #�б����������ʽ���
print(a[2]['color'])

aliens=[]
for i in range(30):     #����30�������ˣ���30���ֵ�����б�
	alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(alien)
for alien in aliens[:5]:   #��Ƭ����һ��ʼ�����5ǰһ����Ҳ���Ǳ��4
	print(alien)

#Ҳ�����ֵ��д����б�
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

#���ֵ��д����ֵ�	
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

#####�û������whileѭ��
'''
###input()����ԭ��
message = input("Tell me something, and I will repeat it back to you: ") 
input��ͣ���򣬵ȴ��û����벢������ֵ�洢��message
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see." 
prompt += "\nWhat is your first name? " 
name = input(prompt) 
print("\nHello, " + name + "!")
#ʹ��input��ֵ�Ὣ����ֵ�Զ����ַ�������ʽ�洢

age = input('How old are you ? ')
age = int(age)   #�����ֵ��ַ�����ʾת��Ϊ��ֵ��ʾ 
if age >= 18:
	print('You are an adult !')
else:
	print ('So young are you !')
'''
#ȡ��(��ģ)����� %
print(15%10,2%2)

###Whileѭ��
#name = ['0']
#while name:        #����ǿ��б���True����������ѭ��
#	name=name
	
#ʹ��break�˳�ѭ��
age = 18
while True:
	age+=5
	if age > 50:
		break
	else:
		print(age)
#ʹ��continue��������ѭ��
nums = []
num = 0
while num < 10:
	num+=1
	if num % 2 == 0:
		continue
	nums.append(num)	
	print('Odd num get '+str(num))
print(nums)

##ʹ��while�����б���ֵ�
#�ƶ��б�Ԫ��
unconfirmed_users = ['alice', 'brian', 'candace']  
confirmed_users = []
while unconfirmed_users:    #ֱ��unconfirmed_usersΪ�գ�whileֹͣ����
	temp = unconfirmed_users.pop()
	confirmed_users.append(temp)
print(confirmed_users)
#ɾ�������ض�ֵ�������б�Ԫ��
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
#ͨ���û���������ֵ�
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

#####����
def greet_user (username):
    '''��ʾ���ʺ�'''
    print('Hello!',username)
def favorite_book (book):
    print('My favorite book is '+book)
    
greet_user('Jack')
favorite_book ('child book')
#λ��ʵ��
def describe_pet(animal_type, pet_name):
      """��ʾ�������Ϣ"""
      print("\nI have a " + animal_type + ".")
      print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')  #λ�ö�Ӧ

#�ؼ���ʵ��   �ؼ���ʵ�β��ö�Ӧ�β�λ��
describe_pet(animal_type = 'hamster',pet_name = 'Jack')

#���β��ṩĬ��ֵ���ڵ��õ�ʱ�����ʡ������ʵ��
def favorite_book (book = 'English book'):
    print('My favorite book is '+book)
favorite_book()

#��������ֵ
def get_formatted_name(first_name, last_name):
    """�������������""" 
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

#�������Է����б��ֵ�ȸ��ӵ����ݽṹ
def build_person(first_name, last_name):
    """����һ���ֵ䣬���а����й�һ���˵���Ϣ"""     
    person = {'first': first_name, 'last': last_name}     
    return person  
musician = build_person('jimi', 'hendrix') 
print(musician)

#���whileѭ���뺯����һ��������
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
#�β�Ϊ�б�
def greet_users(names):      
    """���б��е�ÿλ�û��������򵥵��ʺ�"""      
    for name in names:          
        msg = "Hello, " + name.title() + "!"          
        print(msg) 
usernames = ['hannah', 'ty', 'margot']  
greet_users(usernames)

#��Ƭ��ʾ�����б�ʵ�Σ���ֹ���������Ըı��б�
# funtion_name(list_name[:])      #ʹ����Ƭ��ʾ�����б�ĸ������ݸ���������������ı�ԭ�б�����

#��������������ʵ��
def make_pizza(*toppings):       #�β�ǰ��һ��*��toppings����һ����Ԫ�飬��������ʵ���ռ��������Ԫ��
    """��ӡ�˿͵����������"""    
    print(toppings) 
make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#λ��ʵ��+��������ʵ��
def make_pizza(size, *toppings):    
    """����Ҫ�����ı���"""    
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")    
    for topping in toppings:        
        print("- " + topping) 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#ʹ�����������Ĺؼ���ʵ�� ���������������ļ�ֵ�ԣ��򴫵��ֵ䣩
def build_profile(first, last, **user_info):        #user_infoǰ��**�����Ǻţ�ʹpython������һ�����ֵ����������������ļ�ֵ��
    """����һ���ֵ䣬���а�������֪�����й��û���һ��"""      
    profile = {}
    profile['first_name'] = first      
    profile['last_name'] = last     
    for key, value in user_info.items():         
        profile[key] = value      
    return profile  
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')    #�������������ļ�ֵ��
print(user_profile)

##












































































	
	






