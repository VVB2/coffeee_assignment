#Note each block is one Assignment Question
import copy
import itertools
from itertools import groupby
from operator import itemgetter
from array import *

#Array

array_num = array('i', [1,3,5,3,7,3,9])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])

array_num.reverse()
print(array_num)

print(array_num.count(3))

array_num.remove(3)
print(array_num)

#Dictionary

my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorted(my_dict.items(),key = lambda kv: kv[1]))
print(sorted(my_dict.items(),key = lambda kv: kv[1],reverse=True))

samp_dict = {0: 10, 1: 20}
samp_dict.update({2: 30})
print(samp_dict)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

for key, value in my_dict.items():
    print(key, value)

n = 5
res = {}
for i in range(1, n+1):
    res[i] = i*i
print(res)

myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
u_value = set(val for dic in L for val in dic.values())
print("Unique Values: ",u_value)

s = 'w3resource'
counter = {}
for i in s:
    counter[i] = 1 + counter.get(i,0)
print(counter)

dict1 = {1: ["Samuel", 21, 'Data Structures'],2: ["Richie", 20, 'Machine Learning'],3: ["Lauren", 21, 'OOPS with java'],}
print("{:<10} {:<10} {:<10}".format('NAME', 'AGE','COURSE'))
for key, value in dict1.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course))

sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
counter = 0
for i in sample_data:
    if i['success']:
        counter += 1
print(counter)

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)

student = {'name': 'Alex','class': 'V','roll_id': '2'}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)

#Sets
my_set = set([1, 2, 3, 2])
print(my_set)

for i in my_set:
    print(i)

my_set.add(5)
my_set.add(6)
print(my_set)

my_set.remove(2)
print(my_set)

if 3 in my_set:
    my_set.remove(3)
print(my_set)

setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
print(setc1.union(setc2))

print(setc1.difference(setc2))

print(setc1.symmetric_difference(setc2))

print(setc1)
setc1.clear()
print(setc1)

x = frozenset([1, 2, 3, 4, 5])
print(x)

print(max(x), min(x))

#Lists

x = [i for i in range(1,10)]
print(sum(x))

mul = 1
for i in x:
    mul *= i
print(mul)

print(min(x))

s = ['abc', 'xyz', 'aba', '1221']
c = 0
for i in s:
    if len(i) >= 2 and i[0] == i[-1]:
        c += 1
print(c)

x = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def last(n): return n[-1]
print(sorted(x, key = last))

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))

li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1)
print(li2)

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))

def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

print(list(itertools.permutations([1,2,3])))

list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)

list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)

def circularly_identical(list1, list2):
    return(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
if (circularly_identical(list1, list2)):
    print("Yes")
else:
    print("No")

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)

num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", num)
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)

#Tuple
