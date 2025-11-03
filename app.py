import time

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    
    a = 10
    b = 4
    while True:
        print("!!!app 실행 중!!!")
        print(f"Add: {a} + {b} = {add(a, b)}")
        print(f"Subtract: {a} - {b} = {subtract(a, b)}")
        print("-" * 30)
        time.sleep(2)
