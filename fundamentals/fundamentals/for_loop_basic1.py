# Basic - Print all integers from 0 to 150.
for count in range(0,151):
    print(count)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for count in range(5,1001,5):
    print(count)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for count in range (1,101):
    print(count)
    if count % 5:
        print("Coding")
    elif count % 10:
        print("Coding Dojo")

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(0, 500000):
    sum = sum + x
print (sum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours
for n in range(2018, -1, -4):
    print(n)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 3
highNum = 12
mult = 3
for x in range(3,13,3):
    print(x)