def reversing_A(A,start,end):
    while start<end:
        A[start], A[end] = A[end],A[start]
        start +=1
        end -= 1

def reverse_A(A,start,end):
    while start<end:
        A[start], A[end] = A[end], A[start]
        reverse_A(A, start+1, end-1)
        return A

A =['kabir','is','studing']
print(A)
n = int(len(A))
reversing_A(A,0,n-1)
print("After reversing",A)
reverse_A(A,0,n-1)
print('After reverse',A)




