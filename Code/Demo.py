'''
This a Demo For Generator.py Functions
Please Check Generator.py after This

Ahmed Basem Ahmed Alsaeed Ali
TKH ID# 202000188
'''
import Generator as G
from time import sleep

n = G.GetNumber()
Seed = G.GetSeed()

G.SetupCanvas(800,n)

#[CLCG[m1,a1,m2,a2],LCG[a,c,m]]
Keys = [[715,3.5,375,1.5],[3.5,1.5,375]]

#Function to Generate Numbers with a Header and a Footer
def Display(MyList,Label):
    print("\n"+(50*"-") + "Start",Label)
    G.printNumbers(MyList)
    
    print("\n"+(50*"-") + "Done",Label)  
    G.Statistics(MyList)

#Quick Demo of the Encryption Functions
def EncryptionDemo():
    print(3*"\n"+(50*"-") + "Start Encryption")
    keysetting = [19,1.5,31,3.5]

    #Generating 2 Random Number as a Key
    print("Generating Keys for Caesar cipher")
    CeaserKey = G.CLCGList(Seed,keysetting,2)

    print("This is a caesar cipher example using a random generated number Please enter a piece of text to cipher")
    #Take User input to encrypt it
    _text = input("The Text: ")

    G.Encrypt(_text,int(CeaserKey[0]))
    sleep(2)
    G.MiniGame(int(CeaserKey[1]))

#True: Whole Numbers False(Default): Float Numbers
Display(G.CLCGList(Seed, Keys[0], n,True),"CLCG")
sleep(1)
Display(G.LCGList(Seed, Keys[1], n),"LCG")

#EncryptionDemo()

#True: Show Numbers False(Default): Hide Numbers 
G.DrawBitMap(Seed,Keys,True)