def mul(m,n):
    if n==0:
        return 0
    else:
        return m+mul(m,n-1)
print("Product: "+str(mul(6,8)))