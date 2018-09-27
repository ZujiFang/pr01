import math
import sys
 
def prime(n):
    if n <= 1:
        return 0
    for i in range(3,int(math.sqrt(n)+1),2):
    #for i in range(2,n):
        if n%i == 0:
            return 0
    return 1
 
if __name__ == "__main__":
    n = 1000000
    count =0
    for i in range(1000,n+1):
        if prime(i)*prime(i+2):
            #print(i,i+2)
            count = count +1
    print(count)