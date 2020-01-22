my_list= [23, 45, 36, 27, 98, 12, 56, 78, 85]
print("My List:",my_list) 
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if(my_list[i]>my_list[j]):
            temp=my_list[i]
            my_list[i]=my_list[j]
            my_list[j]=temp
            
print("Sorted list: ",my_list)
