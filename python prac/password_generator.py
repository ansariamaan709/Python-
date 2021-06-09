import random
def passwordGenerator(length):
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    symbol="@&#$"
    all=lower+numbers+symbol+upper
    Password ="".join(random.sample(all,length))
    x=list(Password)
    if x[0] in numbers and symbol:
        print(' This password is not valid')
    else:
        print(Password)
    return Password
passwordGenerator(8)
