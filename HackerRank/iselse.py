# n = int(input("Enter any number from 1 to 100\n"))

# if n%2!=0:
#     print("Weird")
# elif n%2==0:
#     if 2<=n<=5:
#         print("Not weird")
#     elif 6<=n<=20:
#         print("Weird")
#     elif 100>n>20:
#         print("Not weird")

n = int(input())
if n % 2 == 0:
    if n in range(2,6):
        print("Not Weird")

    elif n in range(6,21):
        print("Weird")

    elif n > 20:
        print("Not Weird")
else:
    print("Weird")