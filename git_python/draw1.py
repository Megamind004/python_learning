for prime in range(2,100):
    for factor in range(2,int(prime**0.5)):
        if prime % factor == 0:
            break
    else:
        print (f'{prime} is Prime Number !')
