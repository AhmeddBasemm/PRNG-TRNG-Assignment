'''
This a Demo For Generator.py Functions
Please Check Generator.py after This

Ahmed Basem Ahmed Alsaeed Ali
TKH ID# 202000188
'''
import Generator as G
from time import sleep


print("This is a Random Number Generator")
#Variables
#Number of Values to Output
n = G.GetNumber()
#Seed Value
Seed = G.GetSeed()

#True: Show Numbers, False(Default): Hide Numbers 
#Show/Hide on Numbers on Bitmap Toggle
ShowNumbersOnCanvas = False

#[CLCG[m1,a1,m2,a2],LCG[a,c,m]]
Keys = [[715,3.5,375,1.5],[3.5,1.5,375]]

#True: Float Numbers, False: Whole Numbers
#Output Float Values Setting [CLCG,LCG]
FloatOutputSetting = [False,False]

#Setup Canvas Size and Number of output Values

#Function to Generate Numbers with a Header, a Footer, and Statistics
def Display(MyList,Label):
    
    #print the header and the numbers
    print("\n"+(50*"-") + "Start",Label)
    G.PrintNumbers(MyList)
    
    #print the footer and the Statistics
    print("\n"+(50*"-") + "Done",Label)  
    G.Statistics(MyList)

#Quick Demo of the Encryption Functions
def EncryptionDemo():
    #Header
    print(3*"\n"+(50*"*") + "Start Encryption")
    #CLCG Settings
    GenSetting = [19,1.5,31,3.5]
    #Generating 2 Random Number as a Key
    CeaserKey = G.CLCGList(Seed,GenSetting,2)
    print("This is a caesar cipher example using a random generated number Please enter a piece of text to cipher")
    #Take User input to encrypt it
    _text = input("The Text: ")

    #Calling the Encrypt Function
    G.Encrypt(_text,int(CeaserKey[0]))
    #Footer
    print("\n"+(50*"*") + "Encyption Done")
    #Delay for 1 second to enhance User Experience
    sleep(1)
    #Calling the MiniGame Function
    G.MiniGame(int(CeaserKey[1]))

#Generate CLCG Number List and Display it
Display(G.CLCGList(Seed, Keys[0], n,FloatOutputSetting[0]),"CLCG")
#Delay for 1 second to enhance User Experience
sleep(1)
#Generate LCG Number List and Display it
Display(G.LCGList(Seed, Keys[1], n,FloatOutputSetting[1]),"LCG")
#Run an Encryption Demo
EncryptionDemo()
G.SetupCanvas(800,n)
#Calling Draw Number Map Function and Passing the Right Parameters
G.DrawNumMap(Seed,Keys,ShowNumbersOnCanvas)