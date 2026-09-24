#Lab3 Python programs

#1.program to find numbers which are divisible by 7 and 
#multiple of 5 between 1500 and 2700
for number in range(1500,2700):
    if number % 7 == 0 and number % 5 == 0:
        print(number)
#2.program to convert temp to and frm celcius and fahrenheit
c = float(input("enter temp in celcius: "))
f = (c * 9 / 5) + 32
print(c, "c is ",round(f),"in fahrenheit")
 
c = float(input("enter temp in fahrenheit: "))
c = (f - 32) * 5 / 9
print(f,"f is" ,round (c), "in celcius")
#3.program to guess number between 1 to 9.
import random 
number = random.randint(1,9)
while True:
    guess = int(input("guess no between 1 and 9:"))

    if guess == number:
        print("well guessed!")
        break
    else:
        print("wrong guess try again:")
#4.construct star pattern by nested loop
for i in range(1 , 6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*",end="")
    print()
#5.program accepting a word and reverse it
word = input("enter a word:")
print("reversed word:" , word[::-1])
#6.program to count even and odd from a series 
numbers = (1,2,3,4,5,6,7,8)
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("number of even numbers:",even)
print("number of odd numbers",odd)
#7.print each item and coresponding type from list
datalist = [1452,11.23,1+2j,True,'w3resource',
(0,-1),(5,12),{"class": "V","section":"A"}]
for item in datalist:
    print(item, "->", type(item))
#8.print all numbers from 0 to 6 except 3and6 use continue
for number in range(7):
    if number == 3 or number == 6:
        continue 
    print(number)
#9.program to get fibonacci series between 0 and 50
a = 0
b = 1
while b <= 50:
    print(b , end="")
    print()
    a , b = b, a + b
#10.take two digits and give 2 dimensional array,i*j
rows = int(input("enter number of rows:"))
columns = int(input("enter number of columns:"))
array = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(i*j)
    array.append(row)
print(array)
#11.accept sequence of lines blank line end print im lowercase
print("enter lines (blank line to terminate):")
while True:
    line = input()
    if line == "":
        break
    print(line.lower())
#12.accept sequence of 4 digit print divisible by 5
data = input("enter 4 digit binary number :")
numbers = data.split(",")
result = []
for binary in numbers:
    if int(binary,2) % 5 == 0:
        result.append(binary)

print(",".join(result))
#13.accept string calculate digits and letters
text = input("enter string:")
letters = 0
digits = 0
for character in text:
    if character.isalpha():
        letters += 1
    elif character.isdigit():
        digits += 1

print("letters",letters)
print("digits",digits)
#14.check validity
password = input("enter password:")
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "$#@" for c in password)
if (6 <= len(password) <= 16 and
    has_lower and has_upper and has_digit and has_special) :
    print("valid password")
else:
    print("invalid password")
        