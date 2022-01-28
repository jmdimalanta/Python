#Update Values in Dictionaries and Lists
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
def updatedList():
    for i in x:
        if x[1][0] == 10:
            x[1][0] = 15
        print(x)
updatedList()

#Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
def updated_last_name():
    students[0]['last_name']=' Bryant'
    return(students[0])
print(updated_last_name())

#In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
def updatedDirectory():
    sports_directory['soccer'][0] ='Andres'
    return(sports_directory)
print(updatedDirectory)

#Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
def updatedValue():
    z[0] = {'x': 10, 'y': 30}
    return(z)
print(updatedValue())

#Iterate Through a List of Dictionaries
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary():
    for v in students:
        print(v)
iterateDictionary()

#Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2():#first name
    res = [sub['first_name'] for sub in students]
    print(str(res))
iterateDictionary2()

def iterateDictionary2():#last name
    res = [sub['last_name'] for sub in students]
    print(str(res))
iterateDictionary2()

#Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print (dojo)
def printInfo():
    for key, values in dojo.items():
        print(key, len(key)-2)
        if(isinstance(values, list)):
            for value in values:
                print(value)
        else:
            print(value)
printInfo()