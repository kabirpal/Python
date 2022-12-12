name = input("Please enter your name: ")
print("Welcome", name)
target = float(input("Please enter your monthly target"))
achieved = float(input("Please enter your achieved target"))
if target>achieved:
    per =float(((target-achieved)/target)*100)
    print("You have achieved " +str(per)+ "% of your target")
else:
    per =float((((achieved-target)/target)*100)+100)
    print("You have achieved " +str(per)+ "% of your target")

if (per <= 50):
    print("5,000 is your bonus")
elif(50 < per < 80):
    print("10,000 is your bonus")
elif 80< per <=100:
    print("15,000 is your bonus")
else:
    print("25000 is your bonus")