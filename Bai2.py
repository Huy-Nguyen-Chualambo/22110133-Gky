def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Nhập một số nguyên không âm: "))

if n < 0:
    print("Vui lòng nhập một số không âm.")
else:
    print(f"{n}! = {factorial(n)}")
