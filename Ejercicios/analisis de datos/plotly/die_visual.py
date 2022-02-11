from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


#the 6 sides die
die = Die()

results = [die.roll() for _ in range(100)]

frequencies = []
for value in range(die.num_sides):
    frequency = results.count(value + 1)
    frequencies.append(frequency)


x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of result'}

layout = Layout(title='Results of rolling one die 100 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': layout}, filename='dieFrequencies.html')