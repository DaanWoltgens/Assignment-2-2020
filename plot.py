import plotly.graph_objects as go
import numpy as np
import pandas as pd
import csv

dups = pd.read_csv('duplications.csv', sep=r'\s*,\s*')

loc = pd.read_csv('loc.csv')

loc = loc.sort_index(ascending=False)

versions = loc.iloc[:,0].values.tolist()
sizes = loc.iloc[:,1].values.tolist()

highest = max(dups.iloc[:,5].values.tolist())
print('Highest value:', highest)

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
        val = dups.loc[(dups['v1'] == w) & (dups['v2'] == v)]
        if not val.empty:
            newlist.append(val.iloc[0]['measure'] / highest)
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

labelvals = []
labeltext = []
for i in range(len(versions)):
    if versions[i][-1] == '0' or versions[i] in ['1.1', '1.2']:
        labelvals.append(newsizes[i])
        labeltext.append(versions[i])

fig.update_layout(margin = dict(t=200,r=200,b=200,l=200),
    xaxis = dict(
        tickmode = 'array',
        tickvals = labelvals,
        ticktext = labeltext,
        dtick=1000,
        autorange='reversed'
    ),
    yaxis = dict(
        tickmode = 'array',
        tickvals = labelvals,
        ticktext = labeltext,
        dtick=1000
    ),
    showlegend = False,
    width = 1000, height = 1000,
    autosize = False )

fig.show()