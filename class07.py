# Static 
def Greet(): # Function Initilization
    print("Hello Ali Jawwad") # Function body

# Greet() # Function Caller

# Dynamic
def Greet2(username): # parameters 
    print(f"Salam {username}")
    
Greet2("Ali") # Arguments 
Greet2("Mustafa")
Greet2("Asif")
Greet2("hasnain")


# Dynamic
def Cook(menu, isSpice):
    print(f"{menu} {isSpice}")

Cook("Biryani" , True) 
Cook("Nihari" , False)
Cook("Pie" , True)


def cook2():
    print("Daal")
    
cook2()
cook2()
cook2()
cook2()



# Calculator
def Calculator(num1, sign, num2):
    if sign == "+":
        print(num1 + num2)
        
    # Minus
    
    # Division (without decimal)
    
    # Multiplication
    
    # Remainder
    
    # 2 * 2 * 2 *2  
    
# Calculator(2 + 2 = 5)
Calculator(2.5 ,  "+" , 3.7) 




