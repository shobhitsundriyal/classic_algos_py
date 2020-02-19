calls = 0

def recur_fibo(n):
    global calls
    if n <= 1:
        #calls += 1
        return n
    else:
        calls += 2
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input('Enter positive no: '))

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))

print('Total recursive calls for {} numbers is {}'.format(nterms, calls))