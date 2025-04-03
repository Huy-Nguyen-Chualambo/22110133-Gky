def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib = [0] * (n + 1)
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Nhập số nguyên n từ người dùng
n = int(input("Nhập số nguyên n: "))

# Kiểm tra và in kết quả
if n < 0:
    print("Vui lòng nhập một số không âm.")
else:
    print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")
