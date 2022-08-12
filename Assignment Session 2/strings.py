#Note each block is one Assignment Question
import textwrap

s = 'thisisatest'
print(len(s))

s = 'google.com'
res = {}
for i in s:
    res[i] = 1+res.get(i, 0)
print(res)

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1
print(change_char('restart'))

def ing(str1):
    return str1 + 'ing'
print(ing('abc'))
print(ing('string'))

s = ['hello', 'test', 'longest', 'small', 'test2']
max_len = 0
i = 0
for index, data in enumerate(s):
    if len(data) > max_len:
        max_len = len(data)
        i = index
print(s[i])

l = input('Enter a string:')
print(l.upper())
print(l.lower())

items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])

sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print(textwrap.fill(sample_text, width=50))

str1 = 'The quick brown fox jumps over the lazy dog.'
print(str1.count("fox"))

print(str1[::-1])

str1 = 'W3RESOURCE.COM'
print(str1[:4].lower() + str1[4:])