class Carfuel:
    def solution(dis,capa,rf,sdis):
        sdis.append(dis)
        cf = capa
        count = 0
        for i in range(len(sdis)):
            if i<len(sdis) and sdis[i+1] - sdis[i] <= capa:
                if (cf-sdis[i])>0:#3-2=1
                    i+=1
                    continue
                if (cf-sdis[i]) <= 0:
                    i-=1
                    count+=1
                    cf += 400
            else:
                count = -1
        return count

if __name__ == "__main__":
    distance = int(input("Enter the distance"))
    capacity = int(input("enter the capacity"))
    refuel = int(input("Fuel stations"))
    sdis = list(map(int,input().split(" ")))
    print(Carfuel.solution(distance,capacity,refuel,sdis))
