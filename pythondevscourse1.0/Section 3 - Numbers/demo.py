import math

# Whole Numbers ---> Integers (int)
# Decimal Numbers e.g price ---> Float
# Algebraic Expressions ---> Algebraic Expression


#BIDMAS - Bracket, Indices (power or exponent), Division, Multiplication, Addition and Substraction

age = 20
height = 1.71

x = 3
#2x + 1
expression = (2 * x) + 1

#Maths Operations
a = 12
b = 3

#print(3 ** 2)##Indice Expression Operations
print(a / b)#Division return a literal value of type flaot or integer
print(3 // 14)#Strictly return a integer/whole number value
print(3 / 14)#Return a float#

##By default the division operator of even two whole (int) values returns a decimal number (float)

print(a * b)#Multiplcation
print(a + b)#Addition
print(a - b)#Substraction

#Special Operations

#Find the remainder
print(a % b)##Modulus
## 5 + 5 + 5 = 15
##17-15 = 2











#module - folder that contains useful code that we can user for our application

sqaure_root = math.sqrt(144)
print(sqaure_root)


#functions
value = -3
print(abs(value))
print(math.pow(value, 2))

#input

user_input = input("What is the first number in your calculation ")
print(user_input) #Print the input that was given the by the user on lin6