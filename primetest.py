
def checkPrime(num):
    flag = False

    if num > 1:
        for i in range (2, num):
            if num%i==0:
                flag = True
                break

    if num<=1 or flag:
        return 'NonPrime'
    else:
        return 'Prime'

def listPrime(min=0, max=10):
    primelist = []

    for i in range(min, max+1):
        if checkPrime(i)=='Prime':
            primelist.append(i)

    return(primelist)

##Testing Function
print(listPrime(0,31))
# print(checkPrime(31))

# for i in range (10, 0):
#     print(i)