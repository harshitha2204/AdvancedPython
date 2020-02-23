def square_it_func(a):
    return a * a

x = map(square_it_func, [1, 4, 7])
print(x) # prints '[1, 16, 49]'