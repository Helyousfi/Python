M = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(M[0:6:2])
print(M[::2])
print(M[::-1])

# To delete an item
del M[0]

M = [[10, 20, 30, 40, 50, 60, 70, 80, 90],
    [10, 20, 30, 40, 50, 60, 70, 80, 90],
    [10, 20, 30, 40, 50, 60, 70, 80, 90],
    [10, 20, 30, 40, 50, 60, 70, 80, 90]]

print(M[0][2]) # To print an element 
print(M.sort(reverse = True))

print(map(lambda x:x+1, [1,2,3]))
