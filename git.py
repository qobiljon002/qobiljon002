# # # # # # # # print(5%3)

# # # # # # # # print(2*4)
A=1,2,3,4,5,6,7,8,9,10,11
for num in (A):
    print(A)
# # # # # # from random import randint
# # # # # # print(randint(0,10))
# # # # # from random import random
# # # # # print(random()*100)
# # # # from random import random
# # # # from math import floor
# # # # print(floor(random()*100))

# # # names=['Xasan','xusan']
# # # print(names)
from random import randint
num=int(input(' enter number.'))
list=[]
i=0
while i<num:
    list.append(randint(0,10))
    i+=1
print(list)     
from random import randint
num=int(input(' enter number.'))
list=[randint(0,100)for i in range(num)]

# print(list)
# print([elem for elem in list])
a=[[1,2,3], [4,5,6], [7,8,9]]
for line in a:
    for elem in line:
        print(elem)
