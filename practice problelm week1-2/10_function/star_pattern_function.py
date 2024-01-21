def print_pattern(n=5):
    # n = input("Enter the digit that you want to print pattern")
    for i in range(n):
        s = ''
        for j in range(i+1):
            s += '*'
        print(s)

print_pattern()