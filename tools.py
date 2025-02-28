def add(*args):
    return sum(args)

def max_number(*args):
    return max(args)

def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

def faculty(n):
    if n == 1:
        return n
    else:
        return n * faculty(n-1)
    
print(faculty(4))

