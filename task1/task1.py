n, m = map(int, input('Введите n и m через пробел:').split(" "))
array = list(range(1,n+1))
trace = [1]
i = 0
while (i+(m-1)) % n != 0:
    if (i+(m-1)) % n != 0:
        trace.append(array[(i+(m-1)) % n])
    i = (i+(m-1)) % n
for i in trace:
    print(i, end='')