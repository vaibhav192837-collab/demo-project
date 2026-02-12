# # print table of user input

# n= int(input("enter a number: "))

# i=1

# for i in range(1,11):
#     m=n*i
#     print(f"{n}x{i}={m}")

# palindrome

# n="gaddag"
# rev=""
# for i in n:
#     rev= i+rev
    
    
# print (rev)

# if (n==rev):
#     print("is a palindrome")
    
# else:
#     print("is not a palindrome")   

# add 2 no

# def add(a,b):
#     return(a+b)

# a= int(input("enter number a: "))
# b= int(input("enter number b: "))

# print(add(a,b))


def fact(n):
    if n<=1:
        return 1
    else:
        
        return(n* fact(n-1))
        
n= int(input("enter number: "))

print("factor:",fact(n))


