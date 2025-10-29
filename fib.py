import argparse

#!/usr/bin/env python3
"""
Generate a list of Fibonacci numbers.
Usage: python Untitled-1.py --count 10
"""


def fibonacci(n: int) -> list:
    """Return a list of the first n Fibonacci numbers (starting with 0, 1)."""
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def main():
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers")
    parser.add_argument("-n", "--count", type=int, default=10, help="how many numbers to generate")
    args = parser.parse_args()
    print(fibonacci(args.count))

if __name__ == "__main__":
    main()