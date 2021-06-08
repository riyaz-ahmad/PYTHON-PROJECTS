import re

print("*****WELCOME TO MY MAGICAL CALCULATOR*****")
print('Enter "quit" in order to quit')
pre= 0
run= True

def calculator():
    global run
    global pre
    #eq= ""
    if pre==0:
        eq=input("Enter equation")  
    else:
        eq=input(str(pre))

    if eq=="quit":
        print('Thanks')
        run= False
    else:
        eq= re.sub('[a-zA-Z,.:""]', '', eq)
        if pre==0:
            pre=eval(eq)
        else:
            pre=eval(str(pre)+eq)


while run:
    calculator()

