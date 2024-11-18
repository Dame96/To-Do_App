print('Hello World!')  
hobbies = ['basketball','pool','gym']
for h in hobbies:
    print(h)
hobbies.append('reading')
print(hobbies)
for h in hobbies:
    print(h)
    hobbies.sort()
    hobbies.pop()
    print(hobbies)
hobbies.insert(0,'sleeping')
print(hobbies)
del hobbies[0]
print(hobbies)
hobbies.remove('gym')
print(hobbies)
hobbies[0] = 'sleep'
print(hobbies)
hobbies.append('runnuing')
print(hobbies)
hobbies.append('cooking')
print(hobbies)
hobbies.append('learning')
print(hobbies)
hobbies.append('sex')
print(hobbies)
hobbies.remove('sex')
print(hobbies)
import this
colors=['red','blue','white','black','grey']
print(colors)
colors = ['red','blue','green']
print(colors)
len(colors)
for value in range(1,5):
    print(value)
len(colors)
numbers= list(range(1,6))
print(numbers)
digits=[1,2,3,4,5]
min(digits)
print(digits)
sum(digits)