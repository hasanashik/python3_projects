
def check_prime_or_not(n):
    for i in range(2, n):
        if n%i == 0:
            #print(f"{n} equals {i} * {n/i}")
            return False
        else:
            continue
    #print(f"{n} is a prime number")
    return True

def prime_generator(bound):
    # your code starts here (delete the pass):
    #ashik code start
    for i in range(bound):
        if i == 0 or i == 1:
            continue
        if check_prime_or_not(i):
            yield i
        i += 1
            

bound = 20
g = prime_generator(bound)
print(next(g))
print(next(g))
print(next(g))
print(next(g))