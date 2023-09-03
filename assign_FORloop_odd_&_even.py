# even = 0 
# odd = 0
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in number :
#     if i % 2 == 0
#         even += 1
#     else :
#         odd += 1
# print("number of even numbers from given tuple", even)
# print("number of odd numbers from given tuple", odd)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
i = 0
while i< len(number) : 
    if i % 2 == 0:
        even += 1
    else :
         odd += 1
    i = i+1
print("number of even numbers from given tuple", even)
print("number of odd numbers from given tuple", odd)