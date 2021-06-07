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
x[1][0] = 15
students[0]['last_name'] = "Bryant"
sports_directory['soccer'][0] = 'Andres'

#2 Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for i in range (len(some_list)):
        print(f"first_name - {some_list[i]['first_name']}, last_name - {some_list[i]['last_name']}")

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(students)

#3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(f"{some_list[i][key_name]}")

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary2('last_name', students)

#4 Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    keys = some_dict.keys()
    for key_counter in keys:
        print(f"{len(some_dict[key_counter])} {key_counter}")
        for lister in range(len(some_dict[key_counter])):
            print(some_dict[key_counter][lister])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)