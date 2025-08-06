m=int(input("enter the number: "))
n=int(input("enter the number: "))
squares=sorted({x**2 for x in range(m, n+1) if x%2 ==0})
print(squares)