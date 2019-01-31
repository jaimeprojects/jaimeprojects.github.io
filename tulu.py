
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
        os.system('git push origin master')
        break
    elif(spell == 'ls'):
        os.system("git status")
        print('incomplete feature TT')
print('-- all done --ʕっ•ᴥ•ʔっ')
#os.system("git status")