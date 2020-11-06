number = int(input())
minPartitioner = number
i = number
while i != 1:
    if number % i == 0:
        minPartitioner = i
    i -= 1
print(minPartitioner)
