test_list = ["Ram",1,"Shyam",2,"Aman",3]
l1 = []
l2 = []

for i in test_list :
    if isinstance(i,int) :
        l1.append(i)
    else :
        l2.append(i)

l1.sort()
l2.sort()
l1.extend(l2)
print("sorted list : -- > " , l1)