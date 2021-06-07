num1 = 42   #variable declaration, numbers
num2 = 2.3  #variable declaration, numbers
boolean = True  #variable declaration, boolean
string = 'Hello World'  #variable declaration, Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #list.initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #dictionary.initialize
fruit = ('blueberry', 'strawberry', 'banana')   #tuple initialize
print(type(fruit))  #log statement, type check
print(pizza_toppings[1])   #log statement, access list value
pizza_toppings.append('Mushrooms')  #list.add value
print(person['name'])   #log statement, dictionary.access value
person['name'] = 'George' #dictionary.change value
person['eye_color'] = 'blue'    #dictionary.add value
print(fruit[2]) #log statement, tuple.access value

if num1 > 45:   #if 
    print("It's greater")   #log statement
else:   #else
    print("It's lower") #log statement

if len(string) < 5: #if, length check
    print("It's a short word!") #log statement
elif len(string) > 15:  #else if , length statement
    print("It's a long word!")  #log statement
else:   #else
    print("Just right!")    #log statement

for x in range(5):  #for loop.start at 0, for loop.end at 4
    print(x)    #log statement
for x in range(2,5):    #for loop.start at 2, for loop.end at 4
    print(x)    #log statement
for x in range(2,10,3): #for loop.start at 2, for loop.end at 9, for loop.increment by 3
    print(x)    #log statement
x = 0   #variable declaration
while(x < 5):   #while. stop at 4
    print(x)    #log statement
    x += 1  #while.increment

pizza_toppings.pop()    #list.delete value
pizza_toppings.pop(1)   #list.access value

print(person)   #log statement, dictionary.access values
person.pop('eye_color') #dictionary.delete value
print(person)   #log statement, dictionary.access values

for topping in pizza_toppings:  #for loop. start at 0, for loop.end at len(pizza_toppings)-1, length check
    if topping == 'Pepperoni':  #if
        continue    #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if
        break   #break

def print_hello_ten_times():    #function
    for num in range(10):   #function.argument, for loop.start at 0, for loop.end at 9
        print('Hello')  #log statement

print_hello_ten_times() #function.call

def print_hello_x_times(x): #function, function.parameters
    for num in range(x):    #function.argument, for loop.start at 0, for loop.end at x-1
        print('Hello')  #log statement

print_hello_x_times(4)  #function.call, function.arguments

def print_hello_x_or_ten_times(x = 10): #function, variable declaration
    for num in range(x):    #for loop.start at 0, for loop.end at 9
        print('Hello')  #log statement

print_hello_x_or_ten_times()    #function.call
print_hello_x_or_ten_times(4)   #function.call, function.parameter


"""
Bonus section
"""

print(num3) #NameError: name <variable name> is not defined
num3 = 72   #
fruit[0] = 'cranberry'  #TypeError: 'tuple' object does not support item assignment or tuple.change value
print(person['favorite_team'])  #KeyError: 'favorite_team'
print(pizza_toppings[7])    #IndexError: list index out of range
   print(boolean)   #IndentationError: unexpected indent
fruit.append('raspberry')   #AttributeError: 'tuple' object has no attribute 'append' or tuples.add value
fruit.pop(1)    #AttributeError: 'tuple' object has no attribute 'pop' or tuples.delete value