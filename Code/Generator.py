'''
PLease Check Demo.py First
Ahmed Basem Ahmed Alsaeed Ali
TKH ID# 202000188
'''

#Importing tkinter library to create canvases'
# And file Dialog window
from tkinter import *
from tkinter import filedialog
#Importing system time library
import time
#Importing math library for Statistics
import numpy as np

#Intializing Variables
#------------------------------------------------------------------------------
#NumMap Dimension variable / number of random numbers per Row
NumMapSize = 20
#NumMap pixel Dimension (0.5 to avoid the overlaping of pixels)
PixelRadius = 0.5
#NumMap pixel Scale Factor
SF = 0
#Holds the Period of LCG or CLCG
period = 0

#initializing Variables for the Canvas
canvasLCG = 0
canvasCLCG = 0
windowLCG = 0
windowCLCG = 0

#------------------------------------------------------------------------------
#Seting Up Canvases
#CanvasSize: Dimension,n: the number of genertaed numbers
def SetupCanvas(CanvasSize,n):
    
    #Refrence to the global variables
    global SF,NumMapSize,canvasLCG,canvasCLCG,windowLCG,windowCLCG
    # NumMap dimension variable / Number of random numbers per Row
    NumMapSize =  int(int(n**(1/2)))
    # Calculate pixel scale factor
    SF = CanvasSize/NumMapSize
    
    #Initalize window for LCG & CLCG canvases
    windowLCG = Tk()
    windowCLCG = Tk()
    #Change the windows titles
    windowLCG.title("Linear Congruential Generator "+ str(NumMapSize**2) + " Numbers")
    windowCLCG.title("Combined Linear Congruential Generator "+ str(NumMapSize**2) + " Numbers")
    
    #Setting up the canvases dimensions
    canvasLCG = Canvas(windowLCG,height=CanvasSize,width=CanvasSize)
    canvasCLCG = Canvas(windowCLCG,height=CanvasSize,width=CanvasSize)
#------------------------------------------------------------------------------ 
#Value Error Handling
def GetNumber():
    #Get user input
    userinput = input("\nHow many number do you need?\n")
    #Check if user inputs number only
    try:
        #If number, assign it to seed
         Number= int(userinput)
         if Number <= 0:
             print("Please try a +ve number, Try Again!")
             Number = GetNumber()

    except ValueError:
        #Prompt the user to try again
        print("Please use a number, Try Again!")
        Number = GetNumber()
    #Return number value
    return Number
#------------------------------------------------------------------------------ 
#Value Error Handling
def GetSeed():
    print("\nPlease type in a number")
    print("Or use the word 'time' to use the system time as the seed")
    print("Or use the word 'file' to Select a text file")
    #Get user input
    userinput = input("The Seed: ")
    #Check if user inputs number or text
    try:
        #if number assign it to seed
         Seed= int(userinput)
         print("-->PRNG Mode")

    except ValueError:
        #If string compare with time key 
        if userinput.lower() == "time":
            #Use System Time
            Seed = time.time()
            print("-->TRNG Mode")
            print("Time", Seed)
        elif userinput.lower() == "file":
            print("-->PRNG File Mode")
            # Get Seed from file
            Seed = openfile()
            
        else:
            #Prompt user to try again
            print("-->Invalid Please Try Again!")
            Seed = GetSeed()
    #Return seed value
    return Seed
#------------------------------------------------------------------------------
# Get Seed from file function
def openfile():
    print("Please Select a file")
    #Open Window for User to Select a File 
    SelectFileWindow = Tk()
    SelectFileWindow.withdraw()

    #Retrieve a file from the file dialog menu
    filepath =  filedialog.askopenfilename()

    try:
        #try opening the file
        file = open(filepath,"r")
        #try to read the file
        Seed = int(file.read())
        #Success statement 
        print("Seed Retrieved:",Seed)
    except:
        #Incase of faliure prompt user to try again
        print("-->Invalid file name. Please Try Again!")
        openfile()
    return Seed
#------------------------------------------------------------------------------
#Statistics Calculator
def Statistics(numbers):
    #Standard deviation
    std = np.std(numbers)
    #Variance
    variance = std**2
    #Mean | Average
    avg = sum(numbers)/len(numbers)
    #Period(Unique numbers count)
    #crating a dictionary from the list to eliminate any duplicates
    Unique =int(len(list(dict.fromkeys(numbers))))
    
    print("Average:",avg,"\nStandard Deviation:",std,"\nVariance:",variance)
    print("Total Numbers",int(len(numbers)),"\nUnique Numbers Count:", Unique)
    print("Period:", period)
    print(50*"-" + "Done Stats")
#------------------------------------------------------------------------------
#Linear Congruential Generator
#Seed
#Settings:[a,c,m] list of values of a,c,m 
#n: number of random generated Numbers
#f: Toggle to calculate whole numbers or a percentage from m 
def LCGList(_seed,settings,n,f = False):
    global period
    #Initalizing a list of size n to store numbers
    r = [0] * n
    a = settings[0]#Multiplier
    c = settings[1]#Increment
    m = settings[2]#Modulus
    
    #Loop for generating n numbers
    for i in range(0, n):
        #Calculating the random Number
        _seed = ((a*_seed)+c)%m
        #Float Value as a percentage btw 0 & 1
        if f:
            #Fraction from m
            r[i] = _seed/m 
        else:
            #Whole number
            r[i] = int(_seed)
    period = "Not Calculated"
    #Return the random number list of size n
    return r
#------------------------------------------------------------------------------
#Combined Linear Congruential Generator
#Seed
#Settings:[m1,a1,m2,a2] list of values of m1,a1,m2,a2
#n: number of random generated Numbers
#f: Toggle to calculate whole numbers or a percentage from m 
#CLCG decreases the chances of redundancy in numbers and increases the period
def CLCGList(_seed,settings,n,f = False):
    
    global period
    #Initalizing a list of size n to store numbers
    r = [0] * n
    
    m1 = settings[0]#Modulus 1
    a1 = settings[1]#Multiplier 1
    m2 = settings[2]#Modulus 2
    a2 = settings[3]#Multiplier 2
    
    #Using a combination of user input and time
    y1 = _seed
    y2 = time.time()
        
    period = ((m1-1)*(m2-1))/((2**2)-1)
    
    #Loop for generating n numbers
    for i in range(0, n):

        #Calculating 2 LCG numbers
        y1 = a1 * y1 % m1
        y2 = a2 * y2 % m2
        #The M1 value controls the maximum number range
        #Calculating a combined LCG random number
        x = (y1 - y2) % m1
        #f is a toggle to return numbers in a fraction format between 0 & 1
        #Adding the values to the list r
        if f:
            r[i] = x / m1
        else:
            r[i] = int(x)
    
    #return the random number list of size n
    return r
#------------------------------------------------------------------------------ 
def PrintNumbers(Numbers):
    #Loop through Numbers array or list
    for n in Numbers:
        #Check if decimal
        if n%1 == 0:
            print(n,end=" ")
        else:
            #Use 2 decimal places
            print("{:.2f}".format(n),end=" ")
#------------------------------------------------------------------------------
# Grey Scale Color Conversion
def Float2Color( percentage ): 
    #Color Pigments R,G,B
    #Calculating Hex value of 1 Color pigment
    color_part_hex = str(hex(int(255 * percentage)))
    
    # A string variable to store the hex value of 1 color pigment
    s = color_part_hex.replace("0x","")
    
    #return hex code for color by using same value in all 3 pigments(GreyScale)
    return "#" + s*3
#------------------------------------------------------------------------------
#Co-ordinates(x,y), Side length, Color, T toggle for text   
def CreatePixel(x, y, s, canvasName, C,text,T = False): 
    #Positioning pixel
    x0 = x - s
    y0 = y - s
    x1 = x + s
    y1 = y + s
    #Creating a square with a grey scale color of side length s
    canvasName.create_rectangle(x0, y0, x1, y1, fill=Float2Color(C),outline="")
    #Toggle text
    if T:
        canvasName.create_text(x, y, text=text, fill="red", font=('Helvetica 15 bold',int(0.3*s)))
#------------------------------------------------------------------------------
def DrawNumMap(_Seed,Keys,T):
    #looping variable
    j = 0
    #Creating 2 lists to store the random numbers in both Formats(Integers, Float)
    Combined  = CLCGList(_Seed,Keys[0],NumMapSize**2,True)
    CombinedF = CLCGList(_Seed,Keys[0],NumMapSize**2)
    #Creating 2 lists to store the random numbers in both Formats(Integers, Float)
    Linear = LCGList(_Seed,Keys[1],NumMapSize**2,True)
    LinearF = LCGList(_Seed,Keys[1],NumMapSize**2)
    
    # Drawing bitmap
    for y in range(NumMapSize):
        for x in range(NumMapSize):
            
            #CLCG
            #Creating a pixel at the right position with the right color & Number representation
            Text = str(CombinedF[j]) + "\n" +"{:.2f}".format(Combined[j])
            CreatePixel((x*SF)+(SF/2), (y*SF)+(SF/2), PixelRadius*SF, canvasCLCG,Combined[j],Text,T)
            #LCG
            #Creating a pixel at the right position with the right color & Number representation
            Text = str(LinearF[j]) + "\n" +"{:.2f}".format(Linear[j])
            CreatePixel((x*SF)+(SF/2), (y*SF)+(SF/2), PixelRadius*SF, canvasLCG,Linear[j],Text,T)
           
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
    #Skip symbols in ASCII Table before offset value
    offset = 65
    #Modulus to loop through the Characters
    m = 123
    #Make sure cipher key is not = 0
    if key == 0:
        key += 3
    
    #Looping through the letters of the Text
    for letter in text:
        #Retreiving Ascii code
        asci = ord(letter)
        
        #Shifting Ascii code 
        asci = (asci + (key))%m
        
        #Staying within the characters region of the ASCII table
        if asci+offset < m:
            cipher = cipher + chr(asci+offset)
        else:
            cipher = cipher + chr(asci)
    
    print("The Cipher:",cipher)        
    print("The key is: + "+str(key))
    #Return encrypted text
    return cipher
#------------------------------------------------------------------------------
#Mini Game
def MiniGame(key):
    text = "Cat"
    print(3*"\n"+(50*"*") + "Bonus Challenge")
    
    #Encrypt the text string variable
    Encrypt(text,key)
    
    #Prompt user to enter the deciphered message 
    print("Decrypt the Cipher text to unlock the surprise")
    print("Take Care it's Case Sensitive")
    userinput = input("Decryption: ")
    
    #Check if user answer is correct and printing ASCII art
    if userinput == text:
        print("""
                        !!! Well Done !!!           
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
                          
        print("\n"+(50*"*") + "Challenge Finished")
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
        #Prompting user to try again
        MiniGame(key)
#------------------------------------------------------------------------------

    