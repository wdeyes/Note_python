# Python_test
python代码练习

> 参考 [廖雪峰官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000) 进行学习，次笔记记录的较为精简，方便学习过Python的人查看复习，还未学习过的人可以一边从[廖雪峰官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000) 学习，一边使用此笔记进行巩固。 

## Python基础 

- 输入： 

```python 
a=input() 
a=input('a:') 
```

- list: 可变 

```python 
a=[1, 2, "hello"] 
```

- tuple: 不可变 

```python 
a=(1,) 
a=(1,2,3,L) 
```

- 条件判断： 

```python 
if a>=0: 
print('a:', a) 
```

- 循环： 

```python 
names = ['xiaoming', 'xiaohong', 'xiaowang'] 
for name in names: 
print(name) 
```

- dict: 存key-value 

```python 
d={'a':1, 'b':2, 'c':3} 
d.pop('a') 
```

- set: 存key值，key唯一，不可重复 

```python 
s=set([1, 2, 3]) 
s.add(4) 
s.remove(4) 
```

## 函数 

### 定义函数 

当返回多个值时，实际返回一个tuple； 
示例的angle默认值为0，调用函数时参数可以没有angle，其他为必选参数（必选参数在前，可选参数在后）； 
默认参数一定要不变对象； 
不变对象的作用：不需要给加锁； 

### 函数的参数 

1. **位置参数** ：调用时必选； 
2. **默认参数** ：调用时可选，构造函数时它必须指向不可变对象，否则会出现逻辑错误； 
3. **可变参数** ：（传入的个数是可变的）构造/调用时参数名前都加*，会自动组装成一个tuple，对它的改变不会影响原来的量； 
4. **关键字参数**：（类似可变参数，变为含有参数名）构造/调用时参数名前加**，会自动组装一个dict，对它的改变不会影响原来的量； 
5. **命名关键字参数**：对关键字参数限制名字，用*隔开； 

### 递归

- 尾递归和循环等价