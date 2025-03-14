import random
print('DICE GAME')
print('GAME STARTS....')
ans='y'
while ans == "y":
    print('DICE ROLLING....')
    S=random.randint(1,6)
    print('YOU GOT:',S)
    ans=input('do you want to roll again?(y/n):')