from multiprocessing import Process, Pool

def reverse():
    a = []
    for j in range(0,len(lst2)):
        lst = []
        for i in lst2:
            lst.append(i[j])
        a.append(lst)
    return a
    

def tenq(lst1, lst2):
    summ = 0 
    for i in lst1:
        for j in lst2:
            summ += i*j
    return summ


lst1 = [
[1, 2, 1], 
[3, 2, 1],
[1, 2, 3]
]

lst2 = [
[2, 1, 2], 
[1, 3, 1], 
[1, 2, 1]
]

count = 0
if len(lst1) == len(lst2):
    for i in lst1:
        for j in lst2:
            if len(i) == len(j):
                pass
            else:
                count += 1
else:
    count += 1
    
if count > 0:
    print('Матрицы разных размеров!')
    
print(reverse())

new_matr = []

for i in range(0,len(lst1)):
    lst = []
    for j in range(0,len(new_lst2)):
        a = tenq(lst1[i],new_lst2[j])
        lst.append(a)
    new_matr.append(lst)
        
print(new_matr) # [[16, 24, 16], [24, 36, 24], [24, 36, 24]]
