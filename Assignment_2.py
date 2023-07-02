Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Player_Name=["Virat Kholi"]#Here player name is string datatype(as name of a person can                                    always be in characters and sequence of characters are not                                   hing but a string.
>>> Country=["India"]#here also country name is a string and reasong is same as above.
>>> T20_Stats=[5000]#here datatype is numeric as points are counted in numbers
>>> Oneday_Stats=[8000]#here also datatype is numeric and reason is same as above
>>> Test_Stats=[10000]#here also datatype is numeric
>>> Ipl_Team=["RCB"]
>>> Player_Name+Country+T20_Stats+Oneday_Stats_Ipl_Team
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Player_Name+Country+T20_Stats+Oneday_Stats_Ipl_Team
NameError: name 'Oneday_Stats_Ipl_Team' is not defined
>>> 
>>> Player_Name+Country+T20_Stats+Oneday_Stats+Test_Stats+Ipl_Team
['Virat Kholi', 'India', 5000, 8000, 10000, 'RCB']
>>> Type(Player_Name)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Type(Player_Name)
NameError: name 'Type' is not defined
>>> Type("Player_Name")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Type("Player_Name")
NameError: name 'Type' is not defined
>>> Type("Virat")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Type("Virat")
NameError: name 'Type' is not defined
>>> a=10
>>> type(a)
<class 'int'>
>>> 
