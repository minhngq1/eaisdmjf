def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Nhập một số để kiểm tra số nguyên tố: "))
    if is_prime(num):
        print(f"{num} là số nguyên tố.")
    else:
        print(f"{num} không phải là số nguyên tố.")