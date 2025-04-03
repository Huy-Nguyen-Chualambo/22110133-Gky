def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Hoán đổi hai phần tử
                swapped = True
        if not swapped:
            break  # Thoát vòng lặp sớm nếu không có hoán đổi

# Nhập mảng từ người dùng
arr = list(map(int, input("Nhập các số nguyên cách nhau bởi dấu cách: ").split()))

# Sắp xếp mảng bằng Bubble Sort
bubble_sort(arr)

# In kết quả
print("Mảng sau khi sắp xếp:", arr)
