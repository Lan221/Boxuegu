N = int(input("N:"))
fib = [0]*(N+1)
fib[0]=0
fib[1]=1
for i in range(2,N+1):
    fib[i] = fib[i-2]+fib[i-1]
print(fib[i])