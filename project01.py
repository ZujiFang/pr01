import math
import sys
 
def prime(n):
    for i in range(3,int(math.sqrt(n)+1)):
    #for i in range(2,n):
        if n%i == 0:
            return 0
    return 1
 
if __name__ == "__main__":
    n = 1000000
    a,b=1000,1002
    count =0
    for i in range(1000,n+1):
        if prime(i)*prime(i+2):
            a,b=i,i+2
            #print(i,i+2)
            count = count +1
    print('The total number of twin primes between 1000 and 1000000 is %d' %count)
    print('The biggest twin prime is %d %d' %(a,b))