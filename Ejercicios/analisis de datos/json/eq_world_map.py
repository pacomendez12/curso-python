from matplotlib import markers
from eq_explore_data import read_eq_data
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


mags, longs, lats = read_eq_data()

# data = [Scattergeo(lon=longs, lat=lats)]
data = [{
    "type": "scattergeo",
    "lon": longs,
    "lat": lats,
    "marker": {
        "size": [7 * mag for mag in mags],
        "color": mags,
        "colorscale": "Viridis",
        "colorbar": {
            "title": "Magnitude"
        },
        "reversescale": True
    }
}]

my_layout = Layout(title = "Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="Ejercicios/analisis de datos/json/global_eq.html")