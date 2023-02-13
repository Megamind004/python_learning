import random


def game_strategy(comp,you):

    if comp == you:
        return None

    elif comp == 'st':
        if you == 's':
            return False
        elif you == 'p':
            return True

    elif comp == 'p':
        if you == 'st':
            return False
        elif you == 's':
            return True

    elif comp == 's':
        if you == 'p':
            return False
        elif you == "st":
            return True

you = input("Your turn : Stone(st), Paper(p),Scissor(s)")
print('Computer"s turn : Stone(s), Paper(p), Scissor(s)')

randNumber = random.randint(1,3)

if randNumber == 1:
    comp = 'st'

elif randNumber == 2:
    comp = 'p'

elif randNumber == 3:
    comp = 's'

print(f'Computer Chose {comp}')
print(f'You Chose {you}')

a = game_strategy(comp, you)


if a == None:
    print("The game is Tie ! Try again !")
elif a:
    print("  You Win !!!  " )
else :
    print("  You Lost !!!  " )











