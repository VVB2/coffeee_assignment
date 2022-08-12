#Note each block is one Assignment Question
import calendar
import datetime
import os
import time
import glob
import sys
import socket
from os.path import exists
from http.client import HTTPConnection

first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
print(f'Hello {last_name} {first_name}')

input_numbers = input('Enter comma seperated numbers:')
numbers = input_numbers.split(',')
list_numbers, tuple_numbers = [], ()
for number in numbers:
    list_numbers.append(number)
tuple_numbers = tuple(list_numbers)
print(f'List: {list_numbers}')
print(f'Tuple: {tuple_numbers}')

help(os)

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

print(calendar.month(2022,11))

f_date = datetime.date(2014, 7, 2)
l_date = datetime.date(2014, 7, 11)
delta = l_date - f_date
print(f'{delta.days} days')

test_data = [1, 5, 8, 3]
print(3 in test_data)
print(-1 in test_data)

def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)
histogram([2, 3, 6, 5])

print(''.join(str(test_data)))

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

file_exists = exists(r'Assignement Session 2\basic_python.py')
print(file_exists)

print(os.system('dir'))

print(os.cpu_count())

print(os.listdir())

print(os.environ['ALLUSERSPROFILE'])

print(os.getlogin())

st = time.time()
for i in range(10):
    time.sleep(0.1)
et = time.time()
print(et - st)

print(os.path.abspath('basic_python.py'))

print(time.ctime(os.path.getmtime('basic_python.py')))
print(time.ctime(os.path.getctime('basic_python.py')))

print(max(5, 8, 3))

files = glob.glob('*.py')
files.sort(key=os.path.getmtime)
print('\n'.join(files))

print("This is the name/path of the script:",sys.argv[0])
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

module_name = ', '.join(sorted(sys.builtin_module_names))
print(module_name)

print(sys.getsizeof(('g', 'e', 'e', 'k', 's')))

print(sys.getrecursionlimit())

s = "The quick brown fox jumps over the lazy dog." 
print(s.count('o'))

print(datetime.datetime.now())

os.system('cls')

print(socket.gethostname())

conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
contents = result.read() 
print(contents)