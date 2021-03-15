import plotly.graph_objects as go
import numpy as np
import pandas as pd
import csv

dups = pd.read_csv('duplications.csv', sep=r'\s*,\s*')

loc = pd.read_csv('loc.csv')

loc = loc.sort_index(ascending=False)

versions = loc.iloc[:,0].values.tolist()
sizes = loc.iloc[:,1].values.tolist()

newsizes = []
prev = 0
for s in sizes:
    newsize = s + prev
    prev = newsize
    newsizes.append(newsize)

z= []
for v in versions:
    newlist = []
    for w in versions:
        val = dups.loc[(dups['v1'] == v) & (dups['v2'] == w)]
        if not val.empty:
            newlist.append(val.iloc[0]['measure'])
        else:
            newlist.append(0)
    z.append(newlist)

fig = go.Figure(data=go.Heatmap(
          x = newsizes,
          y = newsizes,
          z = z,
          type = 'heatmap',
          colorscale = 'Viridis'))

axis_template = dict(autorange = True,
             showgrid = True, zeroline = False,
             linecolor = 'black', showticklabels = False,
             ticks = '' )

fig.update_layout(margin = dict(t=200,r=200,b=200,l=200),
    xaxis = axis_template,
    yaxis = axis_template,
    showlegend = False,
    width = 700, height = 700,
    autosize = False )

fig.show()