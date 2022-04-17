n = 50
def PrimeArr(n):
    prime = []
    for num in range(n):
        if num > 1: 
            for i in range(2, num):
                if (num % i) == 0: 
                    break
            else:
                prime.append(num)
    return prime
PrimeArr(n)