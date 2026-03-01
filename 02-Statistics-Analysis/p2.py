# IF ELSE conditional statement

age = int(input("Enter your age: "))
if age >=18:
     print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
    
    
    
    
                       # practise 1
                       
                       
                       

time = int(input("Enter the time in 24 hour format: "))
t =  24 - time 
if time < 12:
    print("Good Morning!",t, "hours left for the day.")
elif time < 18:
    print("Good Afternoon!", t, "hours left for the day.")
else:
    print("Good Evening!",t, "hours left for the day.")   





                                  # Practise 2

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("congrats you got A grade")
    
elif marks >= 75:
    print("congrats you got B grade")
    
elif marks >= 60:
    print("You got C Grade, good keep improving study hard")
    
else:
    print("You are fail, better luck next time")


     
    #    FOR WHILE LOOP
    
    
for i in range(1,6):
    print(i)
    
                        # practice 4 "printing 1 to 100"

for i in range(1,101):
    print(i)

                       #   printing even numbers upto 50      
         
for i in range(1,51):
    if i%2==0:
        print(i)       

                          # printing my name 5 times
   
x = "shahul"
for i in range(5):
    print(x)        



        # FUNCTIONS
        
# def greet(name):
#     print("Hello", name)
    
def area_of_square(side):
    area = side * side
    return area        
print(area_of_square(5))




#                             adding two numbers using function


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def add_numbers(a,b):       
    sum = a + b
    return sum
print("The sum is:", add_numbers(a,b))





                #       calculate area of rectangle
                
                
def area_rectangle(length, width):
    return length * width

print(area_rectangle(5, 3))



                 
                 
                #  Convert Celsius to Fahrenheit
                
c = float(input("Enter temperature in Celsius: "))             
def c_F(celsius):
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", fahrenheit) 
print(c_F(c))                 

      
        
        
        
                         #     NUMBER GUESSING GAME

import random            
n = random.randint(1, 100)

while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == n:
                print("You got it right! , Congrats .")
        elif guess > n:
                print("Too high! Try again.")
        else:
                print("Too low! Try again.")

                
                
                
        #      calculator program
        
def add(a, b):
        return a + b
def sub(a, b):
        return a - b
def div(a, b):
        return a/b
def mul(a, b):
        return a*b

while True:
        print("\n 1.Add 2.subtract 3.divide 4.multiply 5.exit")
        choice = input("choose ")
        
        if choice == '5':
                break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if choice == '1':
                print("Result:", add(a, b))
        elif choice == '2':  
                print("Result:", sub(a, b))
        elif choice == '3':
                print("Result:", div(a, b))      
        elif choice == '4':
                print("Result:", mul(a, b))        
        else:
                print("Invalid choice, please try again.")        
                
             