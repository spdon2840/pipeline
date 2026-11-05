import os
import sys

def main():
    try:
        num1_str = os.environ.get('NUM1', '0')
        num2_str = os.environ.get('NUM2', '0’)

        num1 = float(num1_str)
        num2 = float(num2_str)

        largest = max(num1, num2)

        print(f"The largest number is: {largest}")

    except ValueError:
        print("Error: Please ensure you entered valid numeric values.")
        sys.exit(1)

if __name__ == "__main__":
    main()
