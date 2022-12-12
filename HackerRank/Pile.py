import sys
for _ in range(int(input())):    
    n=int(input())
    List=[sys.maxsize]  #Base element of List (for comparison)
    List+=list(map(int,input().split()))        
    i=1         
    j=len(List)-1
    prev=0  #index of previous stacked element
    for _ in range(1,len(List)):
        if List[i]>=List[j] and List[i]<=List[prev]:            
            prev=i
            i+=1
        elif List[j]<=List[prev]:            
            prev=j
            j-=1
        else:
            print('No')
            break
    else:
        print('Yes')