
# coding: utf-8

# In[1]:

second_per_day = 86400        # 60 sec/min * 60 min/hr * 24 hr/day
second_per_day


# In[2]:

print('No comment: quotes make the # harmless.')


# In[3]:

alphabet = ''
alphabet += 'abc'
alphabet += 'def'
alphabet += 'ghi'
alphabet


# In[4]:

alphabet = 'abcdefghi' +            'jklmnop' +            'qrstuv' +            'wxyz'
alphabet


# In[5]:

1 + 2 +3


# In[6]:

a = True
if a:
    print("Woe!")
else:
    print("Whee!")


# In[7]:

furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human. Or a hairless bear.")


# In[8]:

color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
else:
    print("I've never heard of the color", color)


# In[9]:

# 相等 ==
# 不相等 !=
# 小於 <
# 小於等於 <=
# 大於 >
# 大於等於 >=
# 成員資格 in

x = 7


# In[10]:

x == 5


# In[11]:

x == 7


# In[12]:

5 < x


# In[13]:

x < 10


# In[14]:

5 < x and x < 10


# In[15]:

(5 < x) and (x < 10)


# In[16]:

5 < x or x < 10


# In[17]:

5<x and x>10


# In[18]:

5 < x and not x > 10


# In[19]:

5 < x < 10     # 5 < x and x < 10


# In[20]:

1 < x < 8 < 999


# In[21]:

a = []
if a:
    print("T")
else:
    print("F")


# In[22]:

count = 1
while count <= 5:
    print(count)
    count += 1


# In[1]:

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())


# In[2]:

while True:
    value = input("Interger, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 ==0:
        continue
    print(number, "squard is ", number*number)


# In[3]:

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number ', number)
        break
    position += 1
else :
    print('No even number found')


# In[4]:

letters = ['a','b','c']
current = 0
while current < len(letters):
    print(letters[current])
    current += 1


# In[5]:

for letter in letters:
    print(letter)


# In[6]:

word = 'cat'
for letter in word:
    print(letter)


# In[8]:

colors = {'R':'red','G':'green','B':'blue'}
for color in colors:
    print(color)


# In[9]:

for color in colors.values():
    print(color)


# In[10]:

for item in colors.items():
    print(item)


# In[11]:

for letter , color in colors.items():
    print(letter , 'is' , color)


# In[13]:

things= []
for thing in things:
    print('thing is ', thing)
    break
else:
    print("nothing")


# In[14]:

days = ['Monday','Tuesday','wednesday']
fruits = ['banana','orange','peach']
drinks = ['coffee','tea','beer','milk']
for day,fruit,drink in zip(days,fruits,drinks):
    print(day,' : ','eat ',fruit,'- drink ',drink)


# In[16]:

english = 'Monday','Tuesday','Wednesday'
french = 'Lundi','Mardi','Mercredi'
list(zip(english,french))


# In[17]:

dict(zip(english,french))


# In[19]:

for x in range(1,6):
    print(x)


# In[20]:

list(range(1,6))


# In[22]:

for x in range(5,0,-1):
    print(x)


# In[23]:

list(range(0,11,2))


# In[25]:

numbers = []                            #跟上面一樣
for number in range(1,6):
    numbers.append(number)
numbers


# In[26]:

numbers = [number for number in range(1,6)]
numbers


# In[27]:

numbers = [number-1 for number in range(1,6)]
numbers


# In[28]:

a = [number for number in range(1,6) if number % 2 == 1 ]
a


# In[29]:

a = [] 
for number in range(1,6):
    if number % 2 == 1:
        a.append(number)
a


# In[30]:

rows = range (1,4)
cols = range (1,3)
for row in rows:
    for col in cols:
        print(row,col)


# In[31]:

rows = range (1,4)
cols = range (1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)


# In[32]:

for row,col in cells:
    print(row,col)


# In[39]:

word = 'letters'
counts = {letter : word.count(letter) for letter in word}
counts


# In[41]:

word = 'letters'
counts = {letter : word.count(letter) for letter in set(word)}
counts


# In[42]:

a = {number for number in range(1,6) if number % 3 == 1}
a


# In[69]:

test = (number for number in range(1,6))
type(test)


# In[70]:

for number in test:
    print(number)


# In[71]:

test_list = list(test)
test_list


# In[72]:

test = (number for number in range(1,6))
test_list = list(test)
test_list


# In[74]:

def do_nothing():
    pass
do_nothing()


# In[75]:

def sound():
    print('wow!')
sound()


# In[76]:

def agree():
    return True

if agree():
    print('T')
else:
    print('F')
    


# In[87]:

def echo(i):
    return i
echo('gun!')


# In[95]:

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green apple"
    else:
        return "what",color,'is?'
commentary('blue')


# In[96]:

def test(a,b,c):
    return {'A':a,'B':b,'c':c}
test('apple','banana','???')


# In[97]:

test(c="???",a='apple',b='banana')


# In[102]:

def test(a,b,c='???'):
    return {'A':a,'B':b,'c':c}
test('apple','banana')


# In[103]:

def test(a,b,c='???'):
    return {'A':a,'B':b,'c':c}
test('apple','banana','ccc')


# In[104]:

def buggy(arg,result=[]):
    result.append(arg)
    print(result)
buggy('a')


# In[105]:

buggy('b')


# In[108]:

def work(arg):
    result=[]
    result.append(arg)
    print(result)
work('a')


# In[109]:

work('b')


# In[110]:

def test(arg, take = None):
    if take is None:
        take = []
    take.append(arg)
    print(take)
test('a')


# In[111]:

test('x')


# In[112]:

def args(*arg):
    print('write:', arg)
args(3,2,1,'what?','ok!')


# In[113]:

def letter(a,b,*c):
    print('no.1:',a)
    print('no.2:',b)
    print('no.all:',c)
letter('100','98','66','88','0')


# In[115]:

def testdic(**x):
    print('dict',x)
testdic(a='apple',b='banana',c='cherry')


# In[116]:

def echo(anything):
    'echo returns its input argument'
    return anything
help(echo)


# In[118]:

print(echo.__doc__)


# In[119]:

def answer():
    print(88)
answer()


# In[120]:

def test(run):
    run()
test(answer)


# In[121]:

def add_(a,b):
    print(a+b)
type(add_)


# In[122]:

def test1(func,a,b):
    func(a,b)
test1(add_,6,8)


# In[123]:

def sum_(*a):
    return sum(a)
sum_(1,2,3,4,5)


# In[124]:

def run1(f,*a):
    return f(*a)
run1(sum_,0,2,4,6,8)


# In[127]:

def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)
outer(10,20)


# In[130]:

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)
knights('Ni!')


# In[132]:

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('bot')
a


# In[133]:

a()


# In[134]:

b()


# In[135]:

def story(words,func):
    for word in words:
        print(func(word))

stairs = ['thud','meow','thud','hiss']

def cap(x):
    return x.capitalize() + '!'

story(stairs,cap)


# In[136]:

story(stairs, lambda word: word.capitalize() + '!')


# In[140]:

def my_range(first,last,step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1,6)
ranger


# In[141]:

for x in ranger:
    print(x)


# In[143]:

# global 變數     
# 變數 = XXX              <--------可在區域內更改全域變數


# In[146]:

slist = [1,2,3]
position = 5
try:
    slist[position]
except:
    print('must between 0 and',len(slist)-1,'but got',position)


# In[148]:

guess_me = 7                                                          #4-1

if guess_me < 7:
    print('too low')
    
elif guess_me == 7:
    print('just right')
    
else:
    print('too high')


# In[149]:

guess_me = 7                                                          #4-2
start = 1

while True:
    if start == guess_me:
        print('found it!')
        break
    elif start < guess_me:
        print('too low')
    else:
        print('oops')
        break
        
    start += 1


# In[153]:

test = []                                                              #4-3
for i in range(3,-1,-1):
    test.append(i)
    
test


# In[160]:

list(i for i in range(10) if i % 2 == 0 )                              #4-4


# In[167]:

a = range(10)                                                          #4-5
squares = {key:key**2 for key in a}
squares


# In[169]:

odd = {number for number in range(10) if number % 2 == 1}              #4-6
odd


# In[170]:

a = (i for i in range(10))                                             #4-7
for i in a:
    print('got',i)


# In[173]:

def good():                                                            #4-8
    a = 'Harry','Ron','Hermione'
    return list(a)

good()


# In[182]:

def get_odd(first=0, last=10 ,step=1):                                 #4-9
    number = first 
    while number < last:
        yield number
        number += step
        
get_odds = get_odd(1,10)
time = 0
for i in get_odds:
    if i % 2 == 1:
        odd = i
        time += 1
        if time == 3:
            print(i)


# In[203]:

def test(func):                                                       #4-10
    def new(*a,**b):
        print('start', func.__name__)
        print('numbes.a=',a)
        print('dicts.b=',b)
        result = func(*a,**b)
        print('result=',result)
        print('end')
        return result
    return new

@test
def funct(a, b):
    return a + b

funct(6,8)


# In[204]:

class OopException(Exception):                                        #4-11
    pass
try:
    raise OopException('Caught an oops')
except OopException as exc:
    print(exc)


# In[206]:

titles = ['Creature of Habit', 'Crewel Fate']                         #4-12
plots = ['A nun turns into a monster', 'A hanuted yarn shop']
dict(zip(titles,plots))


# In[ ]:



