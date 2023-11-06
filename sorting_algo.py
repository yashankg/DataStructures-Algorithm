A = [64, 25, 12, 22, 11]
print("Original array : ",A)
n = len(A)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
 
print ("Sorted array : ",A)
for k in range(n):
    print(A[k] , end=" ")


'''
A=[]
n = int(input("Enter number of elements in array : "))
for i in range(0,n):
    print("enter element element on index",i," : ")
    A.append(int(input()))
print(A)
'''