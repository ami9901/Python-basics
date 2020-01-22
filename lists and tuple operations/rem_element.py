my_tuple = (1,2,3,4,5,6,7,8,9,10)
print("Initial Tuple: ",my_tuple)

my_list=list(my_tuple)

n=int(input("Enter a position for the element to be deleted: "))
del my_list[n-1]
my_tuple=tuple(my_list)
print("After removal of element at position",n,": ",my_tuple)
