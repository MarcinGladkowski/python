import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.plot(rw.x_values, rw.y_values, linewidth=2)

    plt.show()

    keep_running = input('Generate a new random chose ? (y/n): ')
    if keep_running == 'n':
        break