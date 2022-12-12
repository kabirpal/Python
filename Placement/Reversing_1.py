

def reverse_A(A,start,end):
    while start<end:
        A[start], A[end] = A[end], A[start]
        
        #first approac
        # start+=1
        # end-=1

        reverse_A(A, start+1, end-1)
        return A

A = ['Kabir','is','my','name',"ty"]
print(A)
reverse_A(A,0,len(A)-1)
print("After Reversing",A)

