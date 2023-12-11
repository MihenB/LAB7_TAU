import matplotlib.pyplot as plt

start = 0
end = 500

# Чтение данных из файла
data = []
with open('P/dataP001L.txt', 'r') as file:
    for line in file:
        data.append(list(map(float, line.split())))

# Разделение данных на отдельные списки
time = [row[0] for row in data]
angle = [row[1] for row in data]
speed = [row[2] for row in data]
end = len(time)
lin_sig = [500*element for element in time]
# Построение графика угла от времени
plt.figure(figsize=(10, 5))
plt.plot(time[start:end], angle[start:end])
plt.plot(time[start:end], lin_sig, '--')
plt.legend('yg')
plt.title('Угол от времени')
plt.xlabel('Время')
plt.ylabel('Угол')
plt.grid(True)
plt.show()

# Построение графика скорости от времени
plt.figure(figsize=(10, 5))
plt.plot(time[start:end], speed[start:end])
plt.title('Скорость от времени')
plt.xlabel('Время')
plt.ylabel('Скорость')
plt.grid(True)
plt.show()
