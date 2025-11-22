                            #   Student Grade Calculator
                            
marks = int(input("Enter your marks: "))                            

if marks >= 90:
    grade = "A"
    msg = "congrats you got A grade Excellent work"
elif marks >= 75:    
    grade= "B"
    msg = "congrats you got B grade ! Good job Keep it up!"
elif marks >= 60:
    grade = "C"
    msg = "You got C Grade, keep improving study hard"
elif marks <= 40:
    grade = "D"
    msg ="You pass , try improving next time"
else:
    grade = "F"
    msg = "You  fail, try harder --- better luck next time"        
    
print(f"Your grade is {grade}.\n {msg}")
    