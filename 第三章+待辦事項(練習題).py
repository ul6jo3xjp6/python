
# coding: utf-8

# In[5]:

empty_list=[]
weekdays =['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
test = list()
len(empty_list)


# In[2]:

len(weekdays)


# In[6]:

test


# In[7]:

list('abc')


# In[8]:

atuple = ('aa','bb','cc')
list(atuple)


# In[9]:

birthday = '1997/1/18'
birthday.split('/')


# In[10]:

splitme = 'a/b//c/d//e'
splitme.split('/')


# In[11]:

test=['1', '2', '3']
test[0]


# In[12]:

test[-1]


# In[14]:

test1=['0','1','2']
test3=['3','4','5']
test6=['6','7','8']
testlist = [test1,test3,test6]
testlist


# In[15]:

testlist[0]


# In[26]:

test = ['apple','sumsung','htc']
test[1] = 'asus'
test


# In[20]:

test[:]


# In[21]:

test[1:2]


# In[22]:

test[::2]


# In[27]:

test.append('nokia')
test


# In[28]:

test2=['america','taiwan']
test.extend(test2)
test


# In[29]:

test = ['apple','asus','htc']
test2=['america','taiwan']
test += test2
test


# In[30]:

test = ['apple','asus','htc']
test2=['america','taiwan']
test.append(test2)
test


# In[31]:

test=['taiwan','america']
test.insert(1,'japan')
test


# In[32]:

del test[2]
test


# In[48]:

test=['taiwan','america','japan']
test.remove('america')
test


# In[40]:

test=['taiwan','japan','america']
test.pop(1)


# In[41]:

test


# In[43]:

test=['taiwan','japan','america']
test.pop()


# In[44]:

test


# In[45]:

test=['taiwan','japan','america']
test.pop(-1)


# In[46]:

test=['taiwan','japan','america']
test.index('japan')


# In[50]:

country=['taiwan','japan','america']
'taiwan' in country


# In[51]:

'korea' in country


# In[52]:

test=['0','1','2','1','3']
'1' in test


# In[53]:

test.count('1')


# In[54]:

','.join(test)


# In[56]:

test=['1','2','0','5','4']
test.sort()
test


# In[58]:

test=['a','c','b','e','d']
testabc = sorted(test)
testabc


# In[59]:

test


# In[60]:

a = ['1','2','3']
a


# In[61]:

b = a
b


# In[62]:

a[0] = 't'
a


# In[63]:

b


# In[64]:

b[0] = 'pp'
b


# In[65]:

a


# In[66]:

a = ['1','2','3']
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'change'
a


# In[67]:

b


# In[68]:

c


# In[69]:

d


# In[70]:

empty_tuple = ()
empty_tuple


# In[73]:

one_tuple ='a',
one_tuple


# In[74]:

many = 'a','b','c'
many


# In[75]:

many = ('a','b','c')
many


# In[76]:

test = ('1','2','3')
a,b,c = test
a


# In[77]:

b


# In[78]:

c


# In[79]:

a = '00'
b = '11'
a,b = b,a
a


# In[80]:

b


# In[81]:

testlist = ['a','b','c']
tuple(testlist)


# In[82]:

empty_dic = {}
empty_dic


# In[83]:

word = {'a':'apple' , 'b':'bank' , 'c':'cow'}
word


# In[84]:

lol = [['a','apple'],['b','bank'],['c','cow']]
dict(lol)


# In[85]:

lol = [('a','apple'),('b','bank'),('c','cow')]
dict(lol)


# In[86]:

lol = (['a','apple'],['b','bank'],['c','cow'])
dict(lol)


# In[87]:

los = ['aa','bb','cc']
dict(los)


# In[88]:

test = {'A':'apple','B':'boom!','C':'cow'}
test['D']='dick'
test


# In[89]:

test['D'] = 'drop'
test


# In[91]:

test = {'A':'apple','B':'boom!'}
other = {'C': 'cow', 'D': 'drop'}
test.update(other)
test


# In[97]:

test = {'A':'apple','B':'boom!','D':'dick'}
other = {'C': 'cow', 'D': 'drop'}
test.update(other)
test


# In[99]:

del test['D']
test


# In[100]:

test.clear()
test


# In[102]:

test = {'A':'apple','B':'boom!'}
'A' in test


# In[103]:

test['B']


# In[104]:

test = {'A':'apple','B':'boom!','C':'cow'}
test.get('B')


# In[105]:

test.get('G', 'nothing')


# In[107]:

test.get('G')


# In[108]:

test = {'A':'apple','B':'boom!','C':'cow'}
test.keys()


# In[111]:

test.values()


# In[112]:

list(test.values())


# In[113]:

list(test.items())


# In[114]:

color = {'R':'red','B':'blue','G':'green'}
savecolor = color
color["G"]='disappear'
savecolor


# In[115]:

color = {'R':'red','B':'blue','G':'green'}
savecolor = color.copy()
color["G"]='disappear'
savecolor


# In[117]:

empty_set=set()
empty_set


# In[118]:

even_numbers = {0,2,4,6,8}
even_numbers


# In[120]:

odd_numbers = {1,3,5,7,9}
odd_numbers


# In[121]:

set('letters')


# In[122]:

list('letters')


# In[123]:

tuple('letters')


# In[127]:

set(['l', 'e', 't', 't', 'e', 'r', 's'])


# In[128]:

set({'A':'apple','B':'bank'})


# In[142]:

drinks = {'martini':{'vodka','vermouth'},
          'black russian':{'vodka','kahlue'},
          'white russian':{'cream','kahlue','vodka'},
          'manhattan':{'rye','vermouth','bitters'},
          'screwdriver':{'orange juice','vodka'}
          }

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)


# In[135]:

for a , x in drinks.items(): 
    if x & {'vermouth', 'orange juice'}: 
        print(a)


# In[137]:

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth','cream'}:
        print(name)


# In[144]:

bruss = drinks['black russian']
wruss = drinks['white russian']


# In[139]:

a = {1 , 2}
b = {2 , 3}
a & b


# In[140]:

a.intersection(b)


# In[145]:

bruss & wruss


# In[146]:

a | b


# In[147]:

a.union(b)


# In[148]:

bruss | wruss


# In[149]:

a - b


# In[150]:

a.difference(b)


# In[151]:

bruss - wruss


# In[152]:

wruss-bruss


# In[153]:

a ^ b


# In[154]:

bruss ^ wruss


# In[155]:

a <= b


# In[156]:

bruss <= wruss


# In[157]:

a < b


# In[158]:

a < a


# In[159]:

bruss < wruss


# In[160]:

a >= b


# In[161]:

a >= a


# In[162]:

bruss >= wruss


# In[163]:

wruss >= bruss


# In[164]:

a > b


# In[165]:

wruss > bruss


# In[166]:

b > b


# In[168]:

test_list = ['a','b','c']
test_tuple = ('a','b','c')
test_dict = {'a':'aaa','b':'bbb','c':'ccc'}
test_list[2]


# In[169]:

test_tuple[1]


# In[171]:

test_dict['a']


# In[173]:

a = ['apple','asia']
b = ['bank','boom!']
c = ['cow','cross']
tuple_list = a , b , c
tuple_list


# In[175]:

list_list = [a,b,c]
list_list


# In[176]:

dict_list = { 'a' : a , 'b' : b , 'c' : c }
dict_list


# In[278]:

yearlist = [1997,1998,1999,2000,2001]                                        #3-1
yearlist


# In[279]:

yearlist[3]                                                                  #3-2


# In[280]:

yearlist[-1]                                                                 #3-3


# In[187]:

m = "mozzarella"                                                             #3-4
c = "cin derella"
s = "salmonella"
things = [m , c , s]
things


# In[282]:

things = [m.title() , c.title() , s.title()]                                 #3-5
things


# In[192]:

things = [m.upper() , c.upper() , s]                                         #3-6
things


# In[284]:

things = [m , c , s]                                                         #3-7
del things_3_7[-1]
things.append('Nobel Prize')
things


# In[285]:

g = 'Groucho'                                                                #3-8
c = 'Chico'
h = 'Harpo'
surprise = [g,c,h]
surprise


# In[286]:

surprise = [g,c,h.lower()[-1::-1].title()]                                   #3-9
surprise


# In[287]:

e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}                        #3-10
e2f


# In[288]:

e2f['walrus']                                                                #3-11


# In[289]:

a = list(e2f.keys())                                                         #3-12
b = list(e2f.values())
f2e = {b[0]:a[0],b[1]:a[1],b[2]:a[2]}
f2e.items()


# In[290]:

f2e['chien']                                                                 #3-14


# In[291]:

e2f = list(e2f.keys())                                                       #3-14
set(e2f)


# In[292]:

catt = ['Henir','Grumpy','Lucy']                                             #3-15
animals = {'cat':catt, 'octopi':{}, 'emus':{}}
life = {'animals':animals, 'plants':{}, 'other':{}}
life


# In[293]:

life.keys()                                                                  #3-16


# In[294]:

life['animals'].keys()                                                       #3-17


# In[295]:

life['animals']['cat']                                                       #3-18

