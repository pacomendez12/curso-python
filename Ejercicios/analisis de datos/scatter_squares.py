from matplotlib import pyplot

pyplot.style.use("seaborn")


x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]


fig, ax = pyplot.subplots()

# setting a solid color
# ax.scatter(x_values, y_values, c=(0, 0, 0), s=5)

# setting a gradient
ax.scatter(x_values, y_values, c=x_values, cmap=pyplot.cm.Blues, s=5)

ax.set_title("Square Numbers")
ax.set_xlabel("Value")
ax.set_ylabel("Square of value")

ax.tick_params(axis="both")

ax.axis([0, 1100, 0, 1_100_000])

pyplot.savefig('squares_plot.png', bbox_inches='tight')

# pyplot.show()