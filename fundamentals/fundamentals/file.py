num1 = 42   #variable declaration
num2 = 2.3  #variable declaration
boolean = True  #Data type - Boolean
string = 'Hello World'  #Data type - String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #Composite - Tuples
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #Composite -Dictionary
fruit = ('blueberry', 'strawberry', 'banana')   #Composite - List
print(type(fruit))  #log statement - Composite list
print(pizza_toppings[1])    #log statement - Composite Tuples (access value)
pizza_toppings.append('Mushrooms')  #Composite Tuples (add value)
print(person['name'])   #log statement - Composite Dictionary (access value)
person['name'] = 'George'   #Composite Dictionary (change value)
person['eye_color'] = 'blue'    #Composite Dictionary (add value)
print(fruit[2]) #log statement - Composite list (access value)

if num1 > 45:   #Conditional - if    
    print("It's greater")   #log statement
else:   #Conditioanl - else
    print("It's lower") #log statement

if len(string) < 5: #Conditional - if
    print("It's a short word!") #log statement
elif len(string) > 15:  #Conditional - else if
    print("It's a long word!")  #log statement
else:   #Conditional - else   
    print("Just right!")    #log statement

for x in range(5):  #for loop start
    print(x)    #log statement
for x in range(2,5):    #for loop start
    print(x)    #log statement
for x in range(2,10,3): #for loop start
    print(x)    #log statement
x = 0   #variable declaration
while(x < 5):   #while loop start
    print(x)    #log statement
    x += 1  #increment

pizza_toppings.pop()   #Tuples (delete value)
pizza_toppings.pop(1)   #Tuples (delete value)

print(person)   #log statement (tuples dictionary)
person.pop('eye_color') #tuples (delete value from dictionary)
print(person)   #log statement (tuples dictionary)

for topping in pizza_toppings:  #for loop start
    if topping == 'Pepperoni':  #conditional if
        continue    #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional if
        break   #for loop break

def print_hello_ten_times(): #function parameter
    for num in range(10):   #for loop
        print('Hello')  #function return

print_hello_ten_times() #function log statement

def print_hello_x_times(x): #function parameter
    for num in range(x):    #function for loop
        print('Hello')  #function return

print_hello_x_times(4)  #function argument

def print_hello_x_or_ten_times(x = 10): #function parameter
    for num in range(x):    #function for loop
        print('Hello')  #function return

print_hello_x_or_ten_times()    #function argument
print_hello_x_or_ten_times(4)   #function argument


"""
Bonus section
"""

# print(num3)   #NameError: name <variable name> is not defined
# num3 = 72     #NameError: name <variable name> is not defined
# fruit[0] = 'cranberry'    #IndexError: list index out of range
# print(person['favorite_team'])    #KeyError: 'favorite_team'
# print(pizza_toppings[7])  #IndexError: list index out of range
#   print(boolean)  #IndentationError: unexpected indent
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  #AttributeError: 'tuple' object has no attribute 'pop'