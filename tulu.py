
import os

print("tutlu started...")

while(True):
    spell = input()
    if(spell == 'q'):
        break
    elif(spell == '.'):
        os.system("git add .")
        print("commit message")
        message = input()
        os.system("git commit -m " + message)
    elif(spell == 'ls'):
        os.system("git status")
        print('incomplete feature TT')
    
#os.system("git status")