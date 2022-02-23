import math 


def HiUser():
    name = input("enter your name: ")
    print("Hey ", name)

def UserAge():
    age = int(input("enter your age: "))
    print("you will be 100 yo at: ", 2022 + (100 - age))

def Cone():
    hauteur = float(input("enter the height: ")) 
    rayon = float(input("enter the ray: "))
    volume = 1/3 * (math.pi * math.pow(rayon,2)) * hauteur
    print("the volume is: ", volume)

def OddEven():
    number = float(input("enter your number to check if it Odd or Even: "))
    if number % 2 == 0:
        print(number, " is an even number")
    elif number % 2 != 0:
        print(number, " is an odd number") 

def fibonacci():
    Term = int(input("Enter a number: "))
    Term1 = 0
    Term2 = 1
    c = 0
    if Term <= 0:
        print("Incorrect input")
    elif Term == 1:
        print(Term1)
    else:
        print("The fibonacci of ", Term,  " is:")
        while c < Term:
            print(Term1)
            K = Term1 + Term2
            Term1 = Term2
            Term2 = K
            c += 1
def Ppcm():
    FirstNumber = int(input("enter your first number: "))
    SecondNumber = int(input("enter your secon number: "))
    if FirstNumber > SecondNumber:
        TheBiggerNum = FirstNumber
    else:
        TheBiggerNum = SecondNumber

    while(True):
        if((TheBiggerNum % FirstNumber == 0) and (TheBiggerNum % SecondNumber == 0)):
            PPCM = TheBiggerNum
            break
        TheBiggerNum += 1
    print("The ppcm is :", PPCM)

def Pgcd(): 
    stnum = int(input("enter your first number: "))
    ndnum = int(input("enter your secon number: "))    
    while ndnum != 0 :
        stnum, ndnum = ndnum, stnum % ndnum  
    print(stnum)
