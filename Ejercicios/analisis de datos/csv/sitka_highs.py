import csv
import matplotlib.pyplot as plt
from datetime import datetime


# filename = "Ejercicios/analisis de datos/csv/data/sitka_weather_07-2018_simple.csv"
filename = "Ejercicios/analisis de datos/csv/data/sitka_weather_2018_simple.csv"

with open(filename) as file:
    reader = csv.reader(file)
    next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[-2])
        highs.append(high)
        low = int(row[-1])
        lows.append(low)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)


    ax.set_title("Daily high and low temperatures 2018", fontsize=24)
    ax.set_xlabel("")
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=15)

    plt.show()
