#input: [[1, 2], [3, 4], [5, 6, 7]]

#output: [[[7, 6, 5], [4, 3], [2, 1]]

nested_list = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list1(l):
    l.reverse()
    for i in l:
        if type(i)==list:
            reverse_list1(i)
            
reverse_list1(nested_list)
print(nested_list)       
            
    