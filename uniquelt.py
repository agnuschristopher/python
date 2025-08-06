n=int(input("Enter the no. of elements: "))
nums=[]
for i in range(n):
    num=int(input(f"Enter element{i+1}: "))
    nums.append(num)
unique=set(nums)    
print("Unique elements: ",unique)