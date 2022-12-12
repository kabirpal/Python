def product(num):
    n = len(num)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                num[first] * num[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    numbers = [int(x) for x in input().split()]
    print(product(numbers))