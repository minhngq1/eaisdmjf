def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

n = int(input("Nhập số n để tính Fibonacci: "))
print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")