################################# 基础 ###############

# print("Hello World")
# print("{0:.3f}".format(1.0/3))
# print("{0:_>11}".format('hello'))
# print('a', end=' ')
# print('a', end=' ')
# print('c')

# print('''what's your name''')
# print('what\'s your name')
# print("what's your name")
# print('''this is first line\nthis is second line''')
# print(r"hello\nhello")
# print('This is a string. \
# This continues the string.')

# i=5
# print('value is {0}'.format(i))
# print('value is', i)

# x=5
# print('x is',x)


######################### 控制流 ####################
# number=23
# switch=True
# while switch:
# 	guess=int(input('enter an integer: '))
# 	if guess==number:
# 		print('Your guess is ight')
# 		switch=False
# 	elif guess<number:
# 		print('lower')
# 	else:
# 		print('higher')
# else:
# 	print('project is over')

# for i in list(range(5)):
# 	print(i)
# else:
# 	print('for is over')


# while True:
# 	s=input('enter: ')
# 	if s=='quit':
# 		break
# 	print(len(s))

############################## 函数 #####################
# x=50
# def func():
# 	global x
# 	print(x)
# 	x=2
# 	print(x)

# func()
# print(x)

# def total(a=5, *number, **phonebook):
# 	print('a', a)
# 	for item in number:
# 		print(item)
# 	for first, second in phonebook.items():
# 		print(first, second)

# total(10,1,2,3,ming=1, ning=2, tian=3)


# def print_max(x, y):
# 	'''打印两个数字中的最大值

# 	这两个数字是整数'''
# 	x=int(x)
# 	y=int(y)
# 	if x>y:
# 		print(x) 
# 	elif y>x:
# 		print(y)
# 	else:
# 		pass

# print_max(1,2)
# # help(print_max)
# print(print_max.__doc__)


########################## 模块 ###################

# import sys
# import os
# print('the command line arguments are: ')
# for i in sys.argv:
# 	print(i)
# print(os.getcwd())
# print('\n\nThe python path is', sys.path)


# from math import sqrt
# print(sqrt(16))
# import math
# print(math.sqrt(16))


# if __name__ == '__main__':
# 	print('itself')
# else:
# 	print('others')

# import module
# module.say()
# print(module.__version__)

############################## 数据结构 ########################

# ###### List ##########
# mylist=['banana', 'apple']
# print('I have', len(mylist), 'item.')
# print('These items are:', end=' ')
# for item in mylist:
# 	print(item, end=' ')

# mylist.append('rice')
# print('\nMylist is now', mylist)
# mylist.sort()
# print('Sorted mylist is', mylist)

# print('The first item is', mylist[0])
# olditem=mylist[0]
# del mylist[0]
# print('I bought the', olditem)
# print('Mylist is now', mylist)

######## Tuple ##########
# zoo=('python', 'elephant', 'penguin')
# print('The number of animals in the zoo is', len(zoo))

# new_zoo=(zoo, 'monkey', 'camel')
# print('The number of animals in the new zoo is', len(new_zoo))
# print('All animals in new zoo are', new_zoo)
# print('Animals in old zoo are', new_zoo[0])
# print('The first animal in old zoo is', new_zoo[0][0])
# print('The number of animals in the new zoo is', 
# 	len(new_zoo)-1+len(new_zoo[0]))


######### Dictionary #######
# ab={'Swaroop': 'swaroop@swaroopch.com',
# 	'Larry':'larry@wall.rog'
# }
# print('Swaroop\'s address is', ab['Swaroop'])
# del ab['Swaroop']
# # print('\nThere are {} contacts in the address-book\n'. format(len(ab)))
# print('\nThere are', len(ab), 'contacts in the address-book\n')

# ab['Guido']='guido@python.org'

# for name, address in ab.items():
# 	print('Contact {0} at {1}'.format(name, address))

# if 'Guido' in ab:
# 	print('\nGuido\'s address is', ab['Guido'])


# shoplist=['apple', 'mango', 'carrot', 'banana']
# name='swaroop'

# print('Item 0 is', shoplist[0])
# # print('Item 4 is', shoplist[4])
# print('Item -1 is', shoplist[-1])
# print('Ttem -2 is', shoplist[-2])
# print('Character 0 is', name[0])

# print('\nItem 1 to 3 is', shoplist[1:3])
# print('Item 2 to end is', shoplist[2:])
# print('Item 1 to -1 is', shoplist[1:-1])
# print('Item start to end is', shoplist[:])

# print('\ncharacters 1 to 3 is', name[1:3])
# print('Character 2 to end is', name[2:])
# print('Character 1 to -1 is', name[1:-1])
# print('Character start to end', name[:])

# print('\n', shoplist[2::-3])



# shoplist=['apple', 'mango', 'carrot', 'banana']
# mylist=shoplist
# del shoplist[0]
# print('shoplist is', shoplist)
# print('mylist is', mylist)

# mylist=shoplist[:]
# del mylist[0]
# print('shoplist is', shoplist)
# print('mylist is', mylist)

# a=1
# b=a
# b=2
# print('a is', a)
# print('b is', b)


# name='Swarrop'
# if name.startswith('Swa'):
# 	print('yes, the string starts with "Swa"')
# if 'wa' in name:
# 	print('yes, the contains the string "a"')
# if name.find('b') !=-1:
# 	print('yes, it contains the string "war"')
# else:
# 	print('"b" is', name.find('b'))

# delimiter='_*_'
# mylist=['Brazil', 'Russia', 'India', 'China']
# print(delimiter.join(mylist))


################################## 数据结构总结：list[] tuple() dictionary{} set{}
























