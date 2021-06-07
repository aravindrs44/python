#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#Expected output: 5
#Expected error: 

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#Expected output: 
#Expected error: Error that says number_of_days_in_a_week_silicon_or_triangle_sides() does not exist because it was never declared

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#Expected output: 5
#Expected error: 


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Expected output: 5
#Expected error: 

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Expected output: 5
#Expected error: the function number_of_fingers does not return a value
#Real Output: 5 None

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Expected output: 3 5 8
#Expected error: 
#Real output: 3 5 Error
#Real errors: Since the function add() does not return any values they cannot be added or concatenated

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#Expected output: 25
#Expected error: 

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#Expected output: 100 10
#Expected error: 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Expected output: 7 14 21
#Expected error: 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Expected output: 8
#Expected error: 

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#Expected output: 500 500 300 300
#Expected error: 

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#Expected output: 500 500 300 300
#Expected error: 

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#Expected output: 500 500 300 300
#Expected error: 

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#Expected output: 1 3 2 
#Expected error: 

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#Expected output: 1 3 5 10
#Expected error: 