def average(array):
    summ = 0
    sett = set(array)
    m = len(sett)
    summ = float(sum(sett))/m
    return ('%.3f'%summ)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)