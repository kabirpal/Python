def two_sum(arr):
    target = int(input('Enter your desired number'))
    output = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            k = []
            if arr[i]+arr[j] == target:
                k.append(arr[i])
                k.append(arr[j])
                output.append(k)
            else:
                j += 1
        i += 1
    return output


arr = [2,3,4,5]
print(two_sum(arr))