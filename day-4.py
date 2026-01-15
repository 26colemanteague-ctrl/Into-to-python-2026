num= float(input("what do you want to see"))
def isPrime(num):
    prime=True
    div=num-1
    while div > 1:
        if num % div == 0:
            prime = False
    div=div-1
    return prime
print(isPrime(4))