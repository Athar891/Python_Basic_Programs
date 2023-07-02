Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=[5,10,15]
>>> id(a)
2173617529224
>>> a[1]=20
>>> print(a)]
SyntaxError: invalid syntax
>>> print(a)
[5, 20, 15]
>>> id(a)
2173617529224
>>> b=[11,14,22]
>>> id(b)
2173577125320
>>> b[3]=24
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b[3]=24
IndexError: list assignment index out of range
>>> print(b)
[11, 14, 22]
>>> b[2]=24
>>> print(b)
[11, 14, 24]
>>> c=[Athar, Bca213001, 3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c=[Athar, Bca213001, 3]
NameError: name 'Athar' is not defined
>>> c=["Athar", "Bca213001", 3]
>>> print(c)
['Athar', 'Bca213001', 3]
>>> c[2]=2
>>> print(c)
['Athar', 'Bca213001', 2]
>>> a=2
>>> print(a)
2
>>> a=3
>>> print(a)
3
>>> tu('Athar', 'BCA213001', 3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tu('Athar', 'BCA213001', 3)
NameError: name 'tu' is not defined
>>> tu=('Athar', 'BCA213001', 3)
>>> tu[0]='Noor'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tu[0]='Noor'
TypeError: 'tuple' object does not support item assignment
>>> 
=== RESTART: C:/Users/Athar/Desktop/python_programming/Typeof_function.py ===
>>> 
=== RESTART: C:/Users/Athar/Desktop/python_programming/Typeof_function.py ===
<class 'type'>
>>> 
=== RESTART: C:/Users/Athar/Desktop/python_programming/Typeof_function.py ===
<class 'type'>
<class 'type'>
>>> 
=== RESTART: C:/Users/Athar/Desktop/python_programming/Typeof_function.py ===
<class 'type'>
<class 'type'>
<class 'type'>
<class 'type'>
<class 'type'>
>>> 
=== RESTART: C:/Users/Athar/Desktop/python_programming/Typeof_function.py ===
<class 'type'>
>>> a=4+2j
>>> b=2+2j
>>> c=a+b
>>> print(c)
(6+4j)
>>> a=4+2j
>>> b=2+2j
>>> c=a-b
>>> print(c)
(2+0j)
>>> a=4+2j
>>> b=2+2j
>>> ca*b
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    ca*b
NameError: name 'ca' is not defined
>>> a*b
(4+12j)
>>> a=4+2j
>>> b=2+2j
>>> a/b
(1.5-0.5j)
>>> int(14.4)
14
>>> float(14)
14.0
>>> float(14,2)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(14,2)
TypeError: float() takes at most 1 argument (2 given)
>>> float(14+4)
18.0
>>> complex(14,3)
(14+3j)
>>> complex(14)
(14+0j)
>>> 'Athar'
'Athar'
>>> 'there is "athar"'
'there is "athar"'
>>> """there is a boy who was speaking to a girl he liked but never had guts to confess his love to her"""
'there is a boy who was speaking to a girl he liked but never had guts to confess his love to her'
>>> orgname=Athar
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    orgname=Athar
NameError: name 'Athar' is not defined
>>> organame(2)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    organame(2)
NameError: name 'organame' is not defined
>>> orgname='Athar;
SyntaxError: EOL while scanning string literal
>>> orgname='Athar'
>>> orgname(2)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    orgname(2)
TypeError: 'str' object is not callable
>>> orgname[2]
'h'
>>> print('my name is athar reza\n and i am pursing bachelor's degree in computer application')
      
SyntaxError: invalid syntax
>>> print('my name is athar reza
      
SyntaxError: EOL while scanning string literal
>>> print('my name is athar reza\n and i am pursing bachelor\'s degree in computer application')
my name is athar reza
 and i am pursing bachelor's degree in computer application
>>> print('my name is athar\treza and i am pursing my bachelor\s degree in computer application')
my name is athar	reza and i am pursing my bachelor\s degree in computer application
>>> print('my name is athar reza \t and i am pursing my bachelor\s degree in computer application\\_
      
SyntaxError: EOL while scanning string literal
>>> print('my name is Athar Reza\t and I am pursing my Bachelor\s degree in \\computer application\\)
      
SyntaxError: EOL while scanning string literal
>>> print('my name is Athar Reza\t and I am pursing my Bachelor\s degree in \\computer application\\')
my name is Athar Reza	 and I am pursing my Bachelor\s degree in \computer application\
>>> print('my name is Athar Reza \t and i am pursing my bachelor\s degree in \\computer application\a')
my name is Athar Reza 	 and i am pursing my bachelor\s degree in \computer application
>>> 
>>> a='athar reza'
>>> a[8]
'z'
>>> a='Athar'
>>> b='Reza'
>>> print('this is', +a,b)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print('this is', +a,b)
TypeError: bad operand type for unary +: 'str'
>>> print("this is " , +a)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print("this is " , +a)
TypeError: bad operand type for unary +: 'str'
>>> print("this is",+a)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print("this is",+a)
TypeError: bad operand type for unary +: 'str'
>>> print('the letter that comes after d is %c', ('e'))
the letter that comes after d is %c e
>>> print('the lette that comes after d is %c'%('e'))
the lette that comes after d is e
>>> print("%20",('intershala'))
%20 intershala
>>> print("%20"%('Athar'))
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print("%20"%('Athar'))
ValueError: incomplete format
>>> print("%20s"%('Athar'))
               Athar
>>> print("%-20s"%('Athar'))
Athar               
>>> matches=163
>>> site='ebay'
>>> print('%s has %d matches',%(site,matches))
SyntaxError: invalid syntax
>>> print("%s has %d matches" %(site, matces))
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print("%s has %d matches" %(site, matces))
NameError: name 'matces' is not defined
>>> print(%s has %d matches"%(site,matches))
      
SyntaxError: invalid syntax
>>> print("%s has %d matches"%(site,matches))
ebay has 163 matches
>>> name='Athar'
>>> roll='BCA213001'
>>> "my name is {} and my roll_no is {}".format(name,roll)
'my name is Athar and my roll_no is BCA213001'
>>> "my name is {:s} and my roll_no is {:d}".format(roll,name)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    "my name is {:s} and my roll_no is {:d}".format(roll,name)
ValueError: Unknown format code 'd' for object of type 'str'
>>> name='Athar'
>>> roll='BCA213001'
>>> "my name is {:s} and my roll_no is {:d}".format(roll,name)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    "my name is {:s} and my roll_no is {:d}".format(roll,name)
ValueError: Unknown format code 'd' for object of type 'str'
>>> "my name is {:s} and my roll_no is {:d}".format(name,roll)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    "my name is {:s} and my roll_no is {:d}".format(name,roll)
ValueError: Unknown format code 'd' for object of type 'str'
>>> 'python'.upper().isupper()
True
>>> '0*12'.isdigit()
False
>>> '12.0'.isdigit()
False
>>> '012'.isdigit()
True
>>> m1={1,2,3,4,5}
>>> m1
{1, 2, 3, 4, 5}
>>> type(m1)
<class 'set'>
>>> s1={'intershala'}
>>> s1
{'intershala'}
>>> s1=set{'intershala'}
SyntaxError: invalid syntax
>>> s1=set('intershala')
>>> s1
{'i', 's', 'a', 'r', 'n', 'e', 'l', 't', 'h'}
>>> #suppose you want to know how many unique elements are present in a sent then we use set() function
>>> s2=set('hey, everyone my name is athar reza, and I am pursing bachelor\s in computer application')
>>> s2
{'\\', 'a', 'n', 'e', ',', 'b', 'r', 'g', 'l', 'y', 'c', 'v', 'I', 'u', 'i', 'd', 'o', 's', 'z', 'p', ' ', 't', 'h', 'm'}
>>> count(s2)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    count(s2)
NameError: name 'count' is not defined
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> s3={(10,10),20}
>>> s3
{20, (10, 10)}
>>> s4={[10,10],20}
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    s4={[10,10],20}
TypeError: unhashable type: 'list'
>>> s5={10,15,20,25}
>>> s5
{25, 10, 20, 15}
>>> s5(1)=12
SyntaxError: can't assign to function call
>>> s5(1)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    s5(1)
TypeError: 'set' object is not callable
>>> s6={}
>>> s6.update(['python','css
	   
SyntaxError: EOL while scanning string literal
>>> s6.update(['python','css','html'])
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    s6.update(['python','css','html'])
ValueError: dictionary update sequence element #0 has length 6; 2 is required
>>> s6.add('html','css','javascript')
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    s6.add('html','css','javascript')
AttributeError: 'dict' object has no attribute 'add'
>>> s6={'html')
SyntaxError: invalid syntax
>>> s6={'html','css',}
>>> s6
{'html', 'css'}
>>> s6.add('javascript')
>>> s6
{'javascript', 'html', 'css'}
>>> s6.update(['Web-development'])
>>> s6
{'javascript', 'Web-development', 'html', 'css'}
>>> s6.clear()
>>> s6
set()
>>> s6.add('html')
>>> s6
{'html'}
>>> s6.update('css','html','javascript','python')
>>> s6
{'i', 'v', 's', 'o', 'j', 'a', 'r', 'p', 'n', 'html', 'l', 't', 'y', 'h', 'm', 'c'}
>>> s6.clear()
>>> s6
set()
>>> s6.add('html','css')
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    s6.add('html','css')
TypeError: add() takes exactly one argument (2 given)
>>> s6.add('html')
>>> s6
{'html'}
>>> s6.update(['css','javascript','web-development']
	  )
>>> s6
{'javascript', 'html', 'css', 'web-development'}
>>> s6.discard('html')
>>> s6
{'javascript', 'css', 'web-development'}
>>> bucktlist=['something',"yes",'''no''']
>>> bucklist
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    bucklist
NameError: name 'bucklist' is not defined
>>> bucktlist
['something', 'yes', 'no']
>>> l1=['athar', 'reza
    
SyntaxError: EOL while scanning string literal
>>> l1=['Athar', 'Reza', 'Shams']
>>> l2=['Tabrez', 'Alam']
>>> l1+l2
['Athar', 'Reza', 'Shams', 'Tabrez', 'Alam']
>>> t1=('pritam','barai')
>>> t2=('Rukhsar','Raza')
>>> t1+t2
('pritam', 'barai', 'Rukhsar', 'Raza')
>>> l3=['python', 'java', 'css', 'html']
>>> l3
['python', 'java', 'css', 'html']
>>> l3.append('python')
>>> l3
['python', 'java', 'css', 'html', 'python']
>>> l3.insert('java')
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    l3.insert('java')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> l3.insert('javascript')
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    l3.insert('javascript')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> l3.append('javascript')
>>> l3
['python', 'java', 'css', 'html', 'python', 'javascript']
>>> l3.remove('python')
>>> l3
['java', 'css', 'html', 'python', 'javascript']
>>> l3.pop()
'javascript'
>>> l3.reverse()
>>> l3
['python', 'html', 'css', 'java']
>>> l3.sort()
>>> l3
['css', 'html', 'java', 'python']
>>> tuple(l3)
('css', 'html', 'java', 'python')
>>> l3
['css', 'html', 'java', 'python']
>>> [1,2]+[4]
[1, 2, 4]
>>> [1,3)*4
SyntaxError: invalid syntax
>>> max('ten','twenty','thirty
    
SyntaxError: EOL while scanning string literal
>>> max()
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    max()
TypeError: max expected 1 arguments, got 0
>>> max('ten','twenty','thirty')
'twenty'
>>> pages[11,13,15(37,21,43),17,19,21]
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    pages[11,13,15(37,21,43),17,19,21]
NameError: name 'pages' is not defined
>>> tuple('1,3')
('1', ',', '3')
>>> tuple((1,2))
(1, 2)
>>> tupe([1,2])
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    tupe([1,2])
NameError: name 'tupe' is not defined
>>> l1=['python','java','c++']
>>> l1.insert(len(l1),'sql')
>>> Country={"'India':'New Delhi'"}
>>> country
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    country
NameError: name 'country' is not defined
>>> country.get('India')
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    country.get('India')
NameError: name 'country' is not defined
>>> thisdic={"Indi":"New Delhi","Japan":"Tokyo"}
>>> thisdic
{'Indi': 'New Delhi', 'Japan': 'Tokyo'}
>>> thisdic.get("Indi")
'New Delhi'
>>> {len([1,2]):10}
{2: 10}
>>> {(1,2):10}
{(1, 2): 10}
>>> {[1,2]:10}
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    {[1,2]:10}
TypeError: unhashable type: 'list'
>>> sample={3+3j:e"complex"}
SyntaxError: invalid syntax
>>> sample={3+2j:"complex"}
>>> sample
{(3+2j): 'complex'}
>>> del thisdic("Indi")
SyntaxError: can't delete function call
>>> thisdic.clear("India")
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    thisdic.clear("India")
TypeError: clear() takes no arguments (1 given)
>>> thisdic.clear()
>>> thisdic
{}
>>> thisdic={"India":"New }
	 
SyntaxError: EOL while scanning string literal
>>> thisdic={"India":"New Delhi","Japan":"Tokyo","United States":"Washington DC"}
>>> thisdic
{'India': 'New Delhi', 'Japan': 'Tokyo', 'United States': 'Washington DC'}
>>> max thisdic
SyntaxError: invalid syntax
>>> thisdic.max()
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    thisdic.max()
AttributeError: 'dict' object has no attribute 'max'
>>> max(thisdic)
'United States'
>>> min(thisdic)
'India'
>>> sort(thisdic)
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    sort(thisdic)
NameError: name 'sort' is not defined
>>> len(thisdic)
3
>>> thisdic.items()
dict_items([('India', 'New Delhi'), ('Japan', 'Tokyo'), ('United States', 'Washington DC')])
>>> thisdic.keys()
dict_keys(['India', 'Japan', 'United States'])
>>> thisdic.values()
dict_values(['New Delhi', 'Tokyo', 'Washington DC'])
>>> 
