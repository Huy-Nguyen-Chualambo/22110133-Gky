def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Hoán đổi hai phần tử
                swapped = True
        if not swapped:
            break 

arr = list(map(int, input("Nhập các số nguyên cách nhau bởi dấu cách: ").split()))

bubble_sort(arr)

print("Mảng sau khi sắp xếp:", arr)
