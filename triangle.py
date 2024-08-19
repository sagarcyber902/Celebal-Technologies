def lower_triangular(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print('*' * i)
    print("\n")

def upper_triangular(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print('*' * i)
    print("\n")

def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    print("\n")

n = 5  
lower_triangular(n)
upper_triangular(n)
pyramid(n)
