'''
PLease Check Demo.py First
Ahmed Basem Ahmed Alsaeed Ali
TKH ID# 202000188
'''

#Importing tkinter Library to Create Canvases 
from tkinter import *
#Importing System Time library
import time
#Importing Math library for Stats
import numpy as np
##Intializing Variables
#------------------------------------------------------------------------------
Seconds = time.time()
# Bitmap Dimension variable / number of random numbers per Row
BitmapSize = 20
#Bitmap pixel Dimension (0.5 to avoid the overlaping of pixels)
PixelRadius = 0.5
#BitMap pixel Scale Factor
SF = 0

#initializing Variables for the Canvas
canvasLCG = 0
canvasCLCG = 0
windowLCG = 0
windowCLCG = 0
#------------------------------------------------------------------------------
#Seting Up Canvases
def SetupCanvas(CanvasSize,_BitmapSize):
    
    #Refrence to the Global variables
    global SF,BitmapSize,canvasLCG,canvasCLCG,windowLCG,windowCLCG
    
    # Bitmap Dimension variable / number of random numbers per Row
    BitmapSize =  int(int(_BitmapSize**(1/2)))
    # Calculate Pixel Scale
    SF = CanvasSize/BitmapSize
    
    #initalize Window for LCG & CLCG Canvases
    windowLCG = Tk()
    windowCLCG = Tk()
    
    #Change the Windows Titles
    windowLCG.title("Linear Congruential Generator "+ str(BitmapSize**2) + " Numbers")
    windowCLCG.title("Combined Linear Congruential Generator "+ str(BitmapSize**2) + " Numbers")
    
    #Setting up the Canvases Dimensions
    canvasLCG = Canvas(windowLCG,height=CanvasSize,width=CanvasSize)
    canvasCLCG = Canvas(windowCLCG,height=CanvasSize,width=CanvasSize)
#------------------------------------------------------------------------------ 
#Value Error Handling
def GetNumber():
    #Get User input
    userinput = input("\nHow Many Number Do You Need?\n")
    
    #Check if user inputs number only
    try:
        #if Number Assign it to seed
         Number= int(userinput)
         if Number <= 0:
             print("Please Try a +ve Number Try again!")
             Number = GetNumber()
    except ValueError:
        print("Please Use a Number Try again!")
        Number = GetNumber()
    
    #Return Number Value
    return Number
#------------------------------------------------------------------------------ 
#Value Error Handling
def GetSeed():
    print("\nPlease type in a Number")
    print("Or Use 'time' to use the system time as the seed")
    #Get User input
    userinput = input("The Seed: ")
    
    #Check if user inputs number or text
    try:
        #if Number Assign it to seed
         Seed= int(userinput)
         print("-->PRNG Mode")
    except ValueError:
        #If Text compare with time key 
        if userinput.lower() == "time":
            #Use System Time
            Seed = Seconds
            print("-->TRNG Mode")
            print("Time", )
        else:
            #Prompt user to try again
            print("-->Invalid Please Try Again")
            Seed = GetSeed()
    
    #Return Seed Value
    return Seed
#------------------------------------------------------------------------------
#Statistics Calculator
def Statistics(numbers):
    
    #Standard Deviation
    std = np.std(numbers)
    #Variance
    variance = std**2
    #Mean | Average
    avg = sum(numbers)/len(numbers)
    #Period(Unique Numbers Count)
    period =int(len(list(dict.fromkeys(numbers))))
    
    print("Average:",avg,"\nStandard Deviation:",std,"\nVariance:",variance)
    print("Total Numbers",int(len(numbers)),"\nUnique Numbers Count:", period)
    print(50*"-" + "Done Stats")
#------------------------------------------------------------------------------
#Linear Congruential Generator

#Seed
#Settings:[a,c,m] list of values of a,c,m 
#n: number of random generated Numbers
#f: Toggle to calculate whole numbers or a percentage from m 

def LCGList(_seed,settings,n,f = False):
    #Initalizing a list to store n numbers
    r = [0] * n
    
    a = settings[0]#Multiplier
    c = settings[1]#Increment
    m = settings[2]#Modulus
    
    #Loop for generating N numbers
    for i in range(0, n):
        #Calculating the Random Number
        _seed = ((a*_seed)+c)%m
        
        #Float Value as a percentage btw 0 & 1
        if f:
            #Fraction From m
            r[i] = _seed/m 
            
        else:
            #Whole Number
            r[i] = int(_seed)
        
    #return the random number list of size n
    return r
#------------------------------------------------------------------------------
#Combined Linear Congruential Generator

#Seed
#Settings:[m1,a1,m2,a2] list of values of m1,a1,m2,a2
#n: number of random generated Numbers
#f: Toggle to calculate whole numbers or a percentage from m 
#CLCG decreases the chances of redundancy in numbers and increases the period

def CLCGList(_seed,settings,n,f = False):
    #Initalizing a list to store n numbers
    r = [0] * n
    
    m1 = settings[0]#Modulus 1
    a1 = settings[1]#Multiplier 1
    m2 = settings[2]#Modulus 2
    a2 = settings[3]#Multiplier 2
    
    #Using a combination of user input and time
    y1 = _seed
    y2 = Seconds
    
    #Loop for generating N numbers
    for i in range(0, n):

        #Calculating 2 LCG numbers
        y1 = a1 * y1 % m1
        y2 = a2 * y2 % m2
        
        #The M1 value Controls the maximum number range
        #Calculating a combined LCG Random Number
        x = (y1 - y2) % m1
        
        #f is a toggle to return numbers in a fraction format between 0 & 1
        #Adding the Values to list
        #Handling 
        if f:
            r[i] = x / m1
        else:
            r[i] = int(x)
    #return the random number list of size n
    return r
#------------------------------------------------------------------------------
def printNumbers(Numbers):
    #Loop Through Array
    for n in Numbers:
        #Check if decimal
        if n%1 == 0:
            print(n,end=" ")
        else:
            #Use 2 Decimal Places
            print("{:.2f}".format(n),end=" ")
#------------------------------------------------------------------------------
# Grey Scale Color Conversion
def float2color( percentage ): 
    #Color Pigment R,G,B
    #Calculating Hex value of 1 Color pigment
    color_part_hex = str(hex(int(255 * percentage)))
    
    # A string variable to store the hex value of 1 color pigment
    s = color_part_hex.replace("0x","")
    
    #return hex code for color by using same value in all 3 pigments(GreyScale)
    return "#" + s*3
#------------------------------------------------------------------------------
#Co-ordinates(x,y), Side length, Color, T toggle for Text   
def create_Pixel(x, y, s, canvasName, C,text,T = False): 
    #Positioning pixel
    x0 = x - s
    y0 = y - s
    x1 = x + s
    y1 = y + s
    #Creating a Square with a grey scale color
    canvasName.create_rectangle(x0, y0, x1, y1, fill=float2color(C),outline="")
    #Toggle Text
    if T:
        canvasName.create_text(x, y, text=text, fill="red", font=('Helvetica 15 bold',int(0.3*s)))
#------------------------------------------------------------------------------
def DrawBitMap(_Seed,Keys,T):
    #looping variable
    j = 0
    #Creating 2 lists to store the random numbers in both Formats(Integers, Float)
    Combined  = CLCGList(_Seed,Keys[0],BitmapSize**2,True)
    CombinedF = CLCGList(_Seed,Keys[0],BitmapSize**2)
    #Creating 2 lists to store the random numbers in both Formats(Integers, Float)
    Linear = LCGList(_Seed,Keys[1],BitmapSize**2,True)
    LinearF = LCGList(_Seed,Keys[1],BitmapSize**2)
    
    
    # Drawing bitmap
    for y in range(BitmapSize):
        for x in range(BitmapSize):
            
            #Creating a pixel at the right position with the right color & Number Representation
            Text = str(CombinedF[j]) + "\n" +"{:.2f}".format(Combined[j])
            create_Pixel((x*SF)+(SF/2), (y*SF)+(SF/2), PixelRadius*SF, canvasCLCG,Combined[j],Text,T)
            
            #Creating a pixel at the right position with the right color & Number Representation
            Text = str(LinearF[j]) + "\n" +"{:.2f}".format(Linear[j])
            create_Pixel((x*SF)+(SF/2), (y*SF)+(SF/2), PixelRadius*SF, canvasLCG,Linear[j],Text,T)
           
            #increment J by 1
            j += 1
    
    #Packing Canvas Elements
    canvasLCG.pack()
    canvasCLCG.pack()
    
    #Opening Windows
    windowLCG.mainloop()        
    windowCLCG.mainloop() 
#------------------------------------------------------------------------------
#Ceaser Cipher Encrypting function (Takes a string for text and int for a key)
def Encrypt(text,key):
    
    #Initializing empty string
    cipher = ""
    #Skip symbols in ASCII Table
    offset = 65
    #Modulus to loop through the Characters
    m = 123
    
    #Looping through the letters of the Text
    for letter in text:
        #Retreiving Ascii Code
        asci = ord(letter)
        
        #Shifting Ascii Code
        asci = (asci + key)%m
        
        #Staying within the Characters Region of the ASCII Table
        if asci+offset < m:
            cipher = cipher + chr(asci+offset)
        else:
            cipher = cipher + chr(asci)
    
    print("The Cipher:",cipher)        
    print("The key is: + "+str(key))
    print("\n"+(50*"-") + "Encyption Done")
    #Return Encrypted Text
    return cipher
#------------------------------------------------------------------------------
#Mini Game
def MiniGame(key):
    text = "Cat"
    print(3*"\n"+(50*"-") + "Bonus Challenge")
    
    
    Encrypt(text,key)
    
    print("Decrypt the Cipher text to unlock the surprise")
    print("Take Care it's Case Sensitive")
    user = input("Decryption: ")
    
    if user == text:
        print("""                           Well Done                
                           ,   __, ,                
           _.._         )\/(,-' (-' `.__            
          /_   `-.      )'_      ` _  (_    _.---._ 
         // \     `-. ,'   `-.    _\`.  `.,'   ,--\\
        // -.\       `        `.  \`.   `/   ,'   ||
        || _ `\_         ___    )  )     \  /,-'  ||
        ||  `---\      ,'__ \   `,' ,--.  \/---. // 
         \\  .---`.   / /  | |      |,-.\ |`-._ //  
          `..___.'|   \ |,-| |      |_  )||\___//   
            `.____/    \\\O| |      \o)// |____/    
                 /      `---/        \-'  \         
                 |        ,'|,--._.--')    \        
                 \       /   `n     n'\    /        
                  `.   `<   .::`-,-'::.) ,'         
                    `.   \-.____,^.   /,'           
                      `. ;`.,-V-.-.`v'              
                        \| \     ` \|\              
                         ;  `-^---^-'/              
                          `-.______,')""")
        print("\n"+(50*"-") + "Challenge Finished")
        print("Please dont forget to check the 2 bitmaps in your taskBar")
    else:
        print("""  Try Again!
               _                        
               \`*-.                    
                )  _`-.                 
               .  : `. .                
               : _   '  \               
               ; *` _.   `*-._          
               `-.-'          `-.       
                 ;       `       `.     
                 :.       .        \    
                 . \  .   :   .-'   .   
                 '  `+.;  ;  '      :   
                 :  '  |    ;       ;-. 
                 ; '   : :`-:     _.`* ;
              .*' /  .*' ; .*`- +'  `*' 
              `*-*   `*-*  `*-*'""")
        MiniGame(key)
#------------------------------------------------------------------------------

    