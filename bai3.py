def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = list(map(int, input("Nhập mảng số nguyên: ").split()))
print("Mảng sau khi sắp xếp:", bubble_sort(arr))