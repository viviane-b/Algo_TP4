#Nom, Matricule
#Nom, Matricule

import math
import random 
import sys

def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


# sieve algorithm

def sieve(n):
    isPrime  = [1]*n
    x = 2
    b = math.floor(math.sqrt(n))

    for i in range (2, b):
        j = 0
        x = 0

        if isPrime[i] == 1:

            while x < n:
                isPrime[x] = 0
                x = i**2 + j*i
                j += 1

    return isPrime


aList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

def millerRabin(n, a):
    s = 0
    t = n-1

    while (t%2==1):
        s += 1
        t = math.floor(t/2)   

    x = a**t % n    

    if (x==1 or x==n-1):
        return True    
    
    for i in range (1, s-1):
        x = x**2 %n        
        if x == n-1:
            return True
   
    return False


def isPrime(n):
    if n in aList:
        return True

    for a in aList:
        test = millerRabin(n,a)
        if (not test):
            return False
    return True

def concatPrimes(x,y):
    a = str(x)
    b = str(y)
    c = a+b
    return (int(c))


def isSpecial(primes, k):
    indexCliques = []
    primesClique = []
    sommesSpeciales = []

    while len(sommesSpeciales) < k:
        print(sommesSpeciales)
        for a in range(len(primes)):
            for b in range (a, len(primes)):
                if isPrime(concatPrimes(primes[a],primes[b])) and isPrime(concatPrimes(primes[b],primes[a])):

                    for c in range (b, len(primes)):
                        if isPrime(concatPrimes(primes[a],primes[c])) and isPrime(concatPrimes(primes[b], primes[c])) and isPrime(concatPrimes(primes[c],primes[b])) and isPrime(concatPrimes(primes[c],primes[a])):

                            for d in range (c, len(primes)):
                                #print(primes[a], primes[b], primes[c], primes[d])
                                if isPrime(concatPrimes(primes[a], primes[d])) and isPrime(concatPrimes(primes[b], primes[d])) and isPrime(concatPrimes(primes[c], primes[d])) and isPrime(concatPrimes(primes[d],primes[a])) and isPrime(concatPrimes(primes[d],primes[b])) and isPrime(concatPrimes(primes[d],primes[c])) and ((a,b,c,d) not in indexCliques):
                                    indexCliques.append((a,b,c,d))
                                    primesClique.append([primes[a],primes[b],primes[c],primes[d]])
                                    sommesSpeciales.append(primes[a]+primes[b]+primes[c]+primes[d])

                                    print(primesClique)
    return(primesClique)




def main(args):
    n = int(args[0])
    output_file = args[1]

    primes = []
    primesBool = sieve(1000)
    for i in range (2, len(primesBool)):
        if primesBool[i]==1:
            primes.append(i)
            print(i)

    x = 211
    print(x, "is prime? ", isPrime(x))

    tab = isSpecial(primes, 2)

    print(tab)
    answer = 0

    # answering
    write(output_file, str(answer))

    

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])