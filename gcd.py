def gcd(a, b):
    
    larger = 0
    smaller = 0
    
    if(a > b):
        larger = a
        smaller = b
    
    else:
        larger = b
        smaller = a
    
    while smaller > 0:
           
        rem = larger % smaller    
        larger = smaller
        smaller = rem
    return larger
    pass

if __name__ == "__main__":
    res = gcd(16, 24)
    print(res)
    
    
