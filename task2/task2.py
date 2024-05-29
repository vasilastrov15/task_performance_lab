result = []

circle_path = input('Введите путь файла с информацией об окружность:')
dot_path = input('Введите путь файла с информацией о точках:')

with open(circle_path) as f_circle:
    data_circle = f_circle.readlines()
    
x_0 = int(data_circle[0].split()[0])
y_0 = int(data_circle[0].split()[1])
R = int(data_circle[1].split()[0])

with open(dot_path) as f_dot:
    for line in f_dot:
        x = int(line.split()[0])
        y = int(line.split()[1])
        if (x - x_0)**2 + (y - y_0)**2 < R**2:
            result.append(1)
        elif (x - x_0)**2 + (y - y_0)**2 == R**2:
            result.append(0)
        else:
            result.append(2)
for i in result:
    print(i)

