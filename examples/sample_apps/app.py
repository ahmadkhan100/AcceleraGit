# examples/sample_app/app.py

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    print("Calculating Fibonacci(35)...")
    result = fibonacci(35)
    print(f"Result: {result}")

if __name__ == '__main__':
    main()
