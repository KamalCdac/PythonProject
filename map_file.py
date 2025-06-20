import json
import requests
import pandas as pd
import numpy as np
import plotly.express as px


# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                   dtype={"fips": int})
polygons = requests.get(
    "https://raw.githubusercontent.com/isellsoap/deutschlandGeoJSON/main/4_kreise/2_hoch.geo.json"
).json()


# generate some data for each region defined in geojson...
df = pd.DataFrame(
    {"fips": range(1, 434, 1), "unemp": np.random.uniform(0.4, 10.4, 433)}
)

fig = px.choropleth(
    df,
    geojson=polygons,
    locations="fips",
    featureidkey="properties.ID_3",
    color="unemp",
    color_continuous_scale="Viridis",
    range_color=(0, 12),
    # scope="europe",
    labels={"unemp": "unemployment rate"},
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_geos(fitbounds="locations", visible=True)
fig.show()