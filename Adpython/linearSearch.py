class Linearsearch:
    def searching(arr,x):
        j = len(arr)
        for i in range(0,j):
            if arr[i] == x:
                return i
        return -1
        

arr = [34,5,61,12,56,89,90,56,23]
x = int(input('Enter any number'))
print(Linearsearch.searching(arr, x))

# def searching(arr,x):
#     j = len(arr)
#     for i in range(0,j):
#         if arr[i] == x:
#             return i
#     return -1

# arr = [34,5,61,12,56,89,90,56,23]
# x = 12
# print(searching(arr,x))