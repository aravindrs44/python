#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#my changes
[1][0] = 15
students[0]['last_name'] = "Bryant"
sports_directory['soccer'][0] = 'Andres'

#2 Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for index in some_list:
        for key in index:
            print(key, "-", some_list[index].get(key))

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(students)
