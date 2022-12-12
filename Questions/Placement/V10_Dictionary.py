d1={"Ramesh":"5","Suresh":"13","Harry":{"K":"500","bj":"90"}}
print(d1["Harry"]["K"])

##updating a dictionary

d1["Sam"] = 467
print(d1)
del(d1["Sam"])
print(d1)

d1.update({"Leena":"789"})
print(d1)