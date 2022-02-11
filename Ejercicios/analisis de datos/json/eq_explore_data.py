import json


def read_eq_data():
    filename = "Ejercicios/analisis de datos/json/data/eq_data_30_day_m1.json"

    with open(filename) as open_file:
        eq_data = json.load(open_file)


    eq_dicts = eq_data["features"]

    mags, longs, lats = [], [], []
    for eq in eq_dicts:
        mag = eq["properties"]["mag"]
        lon = eq["geometry"]["coordinates"][0]
        lat = eq["geometry"]["coordinates"][1]

        mags.append(mag)
        longs.append(lon)
        lats.append(lat)
    
    return (mags, longs, lats)
