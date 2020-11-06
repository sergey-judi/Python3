num = int(input())
maximum = num
while num != 0:
    num = int(input())
    if num != 0 and num > maximum:
        maximum = num
print(maximum)
