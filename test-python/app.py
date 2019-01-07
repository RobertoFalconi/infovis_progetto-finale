import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from sklearn.decomposition import PCA
import plotly.graph_objs as go

app = dash.Dash()

# df = pd.read_csv(
#    'https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv')

df = pd.read_csv('AccessPoint.csv')

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values
x = StandardScaler().fit_transform(x)
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)


app.layout = html.Div([
    html.H1('Acccess Point Roma'),
    html.Div(id='text-content'),
    dcc.Graph(id='map', figure={
        'data': [{
            'lat': df['Latitudine'],
            'lon': df['Longitudine'],
            'marker': {
                'color': df['Tipologia'],
                'size': 8,
                'opacity': 0.6
            },
            'customdata': df['Denominazione'],
            'type': 'scattermapbox'
        }],
        'layout': {
            'mapbox': {
                'accesstoken': 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw',
                'center': {
                    'lat': 41.9,
                    'lon': 12.5
                },
                'pitch': 0,
                'zoom': 10,
                'style': 'light'
            },
            'hovermode': 'closest',
            'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
        }
    })
])


@app.callback(
    dash.dependencies.Output('text-content', 'children'),
    [dash.dependencies.Input('map', 'hoverData')])
def update_text(hoverData):
    s = df[df['Denominazione'] == hoverData['points'][0]['customdata']]
    return html.H3(
        'Indirizzo: {}'.format(
            s.iloc[0]['Indirizzo']
        )
    )

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)