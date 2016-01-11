
# coding: utf-8

# In[1]:

a = 7
print(a)
b = a
print(b)


# In[5]:

type(a)


# In[6]:

type(b)


# In[7]:

type(66)


# In[8]:

type(88.8)


# In[10]:

type('abcdefg')


# In[11]:

type('物件類型')


# In[12]:

66 + 88


# In[13]:

66 + 88 - 54 + 18


# In[14]:

6 * 6


# In[15]:

2 * 4 * 8


# In[16]:

8 / 5


# In[23]:

8 // 5
print('//代表取整數,捨去小數點' , '例如: 8 // 5 =' , 8 // 5)


# In[24]:

a = 95 
a


# In[25]:

a - 3


# In[29]:

a = 100
a = a - 3
a


# In[30]:

a = 100 
a -= 3
a


# In[31]:

a = 100
a += 8
a


# In[33]:

a = 100
a *= 10
a


# In[34]:

a = 100 
a /= 2
a


# In[35]:

a = 100
a //= 3
a 


# In[36]:

a = 4
a %= 3
a


# In[38]:

a = 2
a **= 2
a


# In[39]:

divmod(9,5)


# In[40]:

print('上面是同時取商9//5=1,餘數9%5=4',divmod(9,5))


# In[41]:

2 + 3 * 4


# In[42]:

( 2 + 3 ) * 4


# In[44]:

print('0b或0B為2二進制表示法' , '0o或0O為8進制表示法' , '0x或0X為16進制')


# In[45]:

0B110


# In[46]:

0o101


# In[47]:

0x10


# In[48]:

0XF


# In[49]:

0XA


# In[50]:

int(True)


# In[51]:

int(False)


# In[52]:

int(16.8)


# In[53]:

int(1.0e8)


# In[54]:

int('99')


# In[55]:

int('-68')


# In[57]:

int('+68')


# In[58]:

6 + 8.0


# In[59]:

True + 1 


# In[60]:

False + 1


# In[62]:

float(True)


# In[63]:

float(False)


# In[64]:

float(68)


# In[65]:

float('88.6')


# In[66]:

'snap'


# In[67]:

"crackle"


# In[68]:

"Nay, 'said the  naysayer'"


# In[69]:

"""Boom!"""


# In[70]:

'''Boom'''


# In[72]:

poem = '''THere was a Young Lady of Norway,
          Who casually sat in a doorway;
          When the door squeezed her flat,
          She exclaimed, "What of that?"
          This courageous Young Lady of Norway'''
poem


# In[73]:

poem = 'there was a young lady of norway
        when'


# In[74]:

poem = '''THere was a Young Lady of Norway,
          Who casually sat in a doorway;
          When the door squeezed her flat,
          She exclaimed, "What of that?"
          This courageous Young Lady of Norway
          '''
poem


# In[76]:

bottles = 88 
base = ''
base += 'current inventory : '
base += str(bottles)
base


# In[77]:

str(68.6)


# In[78]:

str(10e3)


# In[80]:

str(True)


# In[84]:

st = 'A man, \n A plan, \nA haha'
print(st)


# In[85]:

print('\tabc')


# In[86]:

print('a\tbc')


# In[87]:

print('ab\tc')


# In[92]:

test = "\"我需要字面的引號\"TEST."
print(test)


# In[90]:

test = "我需要字面的反斜線\\"
print(test)


# In[94]:

'字串可以' + '+字串'


# In[95]:

'字串可以接在' '後面'


# In[97]:

start = '字串可以用*複製 ' * 3 + '\n'
end = 'TEST ' * 3 + '\n'
print(start + start + end)


# In[98]:

test = '用中括號來擷取字元test[位移值]'
test[0]


# In[99]:

test2 = '用中括號來擷取字元test[位移值],位移值不可超過字串長度'
test2[1]


# In[1]:

name = 'LUN'
name.replace('L', 'U')


# In[2]:

'L' + name[1:]


# In[3]:

letters = 'abcdefghijklnmopqrstuvwxyz'
letters[:]


# In[8]:

letters[:5]


# In[7]:

letters[24:26]


# In[9]:

letters[20:]


# In[10]:

letters[-3:]


# In[11]:

letters[:-20]


# In[12]:

letters[0:14:3]


# In[13]:

letters[-1::-2]


# In[14]:

len(letters)


# In[15]:

empty=""
len(empty)


# In[17]:

test = 'gloves, mask, ambulance'
test.split(',')


# In[20]:

test_list = ['aa', 'bb','cc', 'dd', 'ee']
test_str = '-'.join(test_list)
test_str


# In[23]:

poem = '''all that doth flow we cannot liquid name
          or else would fire and water be the same;
          but that is liquid which is moist and wet
          fire that property can never get.
          then 'tis not cold that doth the fire put out
          but 'tis the wet that makes it die,no doubt.'''
poem[:13]


# In[24]:

len(poem)


# In[25]:

poem.startswith('all')


# In[26]:

poem.endswith('it die')


# In[27]:

poem.find('the')


# In[28]:

word = 'the'
poem.find(word)


# In[29]:

poem.rfind(word)


# In[30]:

poem.count(word)


# In[31]:

poem.isalnum()


# In[40]:

setup = 'A duck goes into a bar...'
setup.strip('.')


# In[33]:

setup


# In[34]:

setup.capitalize()


# In[35]:

setup.title()


# In[36]:

setup.upper()


# In[37]:

setup.lower()


# In[41]:

setup.swapcase()


# In[43]:

setup.center(30)


# In[44]:

setup.ljust(30)


# In[45]:

setup.rjust(30)


# In[46]:

setup.replace('duck', 'marmoset')


# In[48]:

setup = 'a duck goes into a bar...'
setup.replace('a', 'a famous',100)


# In[49]:

setup = 'a duck goes into a bar...'
setup.replace('a ', 'a famous',10)


# In[67]:

work = 60 * 60                                         #2-1
work


# In[68]:

second_per_hour = work                                 #2-2
second_per_hour


# In[69]:

work = second_per_hour * 24                            #2-3
work


# In[70]:

second_per_day = work                                  #2-4
second_per_day


# In[71]:

work = second_per_day / second_per_hour                #2-5
work


# In[72]:

work = second_per_day // second_per_hour               #2-6
work


# In[ ]:



