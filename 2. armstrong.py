for i in range(1,1001):
    sum = 0
    string = str(i)
    dig = len(string)

    for j in string:
        sum += int(j) ** dig

    if sum == i:
        print(i)
