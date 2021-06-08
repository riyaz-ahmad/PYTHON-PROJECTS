def game():
    count = 0
    print('\t\tCosider 3 dots one blank')
    print("First question is: ")
    print("\t\t\tL......al\n")
    p, q = input("enter 2 letters for two blanks separated by space: ").split()
    if (p == 'o' or p == 'O') and (q == 'c' or q == 'C'):
        print("\n\t\t\t'Local' is Right answer")
        count = count + 1
    else:
        print("\n\t\tu r wrong")
    print('\nSecond question is: ')
    print('\n\t\t\tc...n......rs...on')
    p, q, r, s = input('\nenter 4 missing letters oseparate them with space: ').split()
    if (p == 'o' or p == 'O') and (q == 'v' or q == 'V') and (r == 'e' or r == 'E') and (s == 'i' or s == 'I'):
        print("\n\t\t\t'Conversion' is right answer")
        count = count + 1
    else:
        print("U r wrong")
    print('\nThird blank is: ')
    print('\t\t\t\n...m......ing')
    p, q, r = input('\nEnter three letters for three blanks separate them with a space').split()
    if (p == q == 'a' or p == q == 'A') and (r == 'z' or r == 'Z'):
        print('\n\t\t\tAmazing is absolutely right answer')
        count = count + 1
    else:
        print('Sorry you are wrong')
    print('\t\t\n Your third question is: ')
    print('\n\t\t\t ...e...rch')
    p, q = input("Enter two letters for two blanks separate them by a space ").split()
    if (p == 'S' or p == 's') and (q == 'A' or q == 'a'):
        print('\t\t\t\n"Search" is right answer')
        count += 1
    else:
        print('wrong answer')

    print('\n\n\t\t\t\t\t\t\t\t\t---*********----RESULTS---**********---')
    print('\n\n\t\t\tName: ', name, end='      ')
    print('\t\t\tid: ', roll, end='      ')
    print('\t\t\tCorrect answers given: ', count)
    print("\n\n\t\t\t====*******************=THANKS=*******************====")


choice = input('Do you want to play?(y/n)')
if choice == 'y' or choice == 'Y':
    print("\t\t\t****WELCOME TO THIS GAME***")
    name = input('Enter your name')
    roll = input('enter your id')
    game()
else:
    print('+====Thanks====+')