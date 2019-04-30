
#try something like
import random
def isPrime(num)
    counter = 2
    while counter < num-1:
        if num%counter==0:
            return False
        counter = counter + 1
    return True
def random_number():
    x = random.randint(3,20)
    result = isPrime(x)
    return locals()

