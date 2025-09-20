num = int(input("Enter a number: "))

print(f"\nMultiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\nBonus: Multiplication Tables from 1 to 5\n")
for n in range(1, 6):
    print(f"--- Table of {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()
