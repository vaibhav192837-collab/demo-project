str="Vaibh"
rev=""
str1=str.lower()
for i in str.lower():
    rev=i+rev
    print(i, rev)

if str.lower()==rev:
    print("\nis a palindrome\n")
else:
        print("is not a palindrome",rev)

# # itiration condition     rev value 
#     1   i=v                 v
#     2.  i=a                 av
#     3.  i=i                 iav
#     4.  i=b                 biav
#     5.  i=h                 hbiav: