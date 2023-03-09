def print_graph(n):
    for k in range(n):
        print("*", end="")
    return ""
    
def get_power(x, n):
    n = 2
    return x ** n

for i in range(-8, 9):
    l = get_power(i, 2)
    print(print_graph(l))

