def my_func(n1, n2, n3):
    numbers = [n1, n2, n3]
    max = sorted(numbers, reverse=True)
    return max[0]

print(my_func(2, 52, 8))

"""def max_(*args):
    return max(args)
print(max(2, 5, 76))"""