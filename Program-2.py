# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse(A,i,j):
	while i < j:
		A[i], A[j] = A[j], A[i]
		i+= 1
		j-= 1
		
print("Original list is ",end=" ")
A = [1, 2, 3, 4, 5, 6]
print(A)
reverse(A, 0, 5)
print("Reversed list is",end=" ")
print(A)