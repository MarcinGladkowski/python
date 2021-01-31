import matplotlib.pyplot as plt

x_values = range(5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', cmap=plt.cm.Blues, s=1)

plt.show()
