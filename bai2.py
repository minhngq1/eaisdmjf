def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    num = int(input("Nhập một số để tính giai thừa: "))
    print(f"Giai thừa của {num} là: {factorial(num)}")