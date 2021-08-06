import primetest

def primefactors(num):
    primelist = primetest.listPrime(0,num)
    primefactor = []

    for i in primelist:
        while num > 0:
            if num%i==0:
                primefactor.append(i)
                num = num/i
            else:
                break    
    return(primefactor)

def primefactors_alt(num):
    primefactor = []
    i = 2
    while i<= num :
        if num%i==0:
            primefactor.append(i)
            num = num/i
        else:
            i = i+1    
    return(primefactor)

print(primefactors(30))
print(primefactors_alt(30))