import plotly.graph_objects as go
import pandas as pd 

df = pd.read_csv('kalmanFilter_ENU.txt', sep='\t', lineterminator='\n', header=None)

mapbox_access_token = open(".mapbox_token").read()

fig = go.Figure()

fig.add_trace(
        go.Scattermapbox(
        lat=df[0].values,
        lon=df[1].values,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9, color='rgb(255, 0, 0)'
        ),
        text=[],
        name='Filtered'
    ))

fig.add_trace(go.Scattermapbox(
        lat=df2[0].values,
        lon=df2[1].values,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9, color='rgb(0, 255, 0)'
        ),
        text=[],
        name='Raw data'
    ))


fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=38.92,
            lon=-77.07
        ),
        pitch=0,
        zoom=10
    ),
)

fig.write_html("ENUFilter.html")
fig.show()