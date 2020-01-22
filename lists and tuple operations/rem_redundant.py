my_list = [10,20,10,30,40,10,20,50,20,40,50,20,10,30,40]
final_list=[]
for i in my_list:
    if i not in final_list:
        final_list.append(i)
        
print("My List:",my_list) 
print("List after duplicates removal: ",final_list)
