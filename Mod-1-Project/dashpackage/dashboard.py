from dashpackage import app
import dash_core_components as dcc
import dash_html_components as html
from dashpackage.routes import *
import dash
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from flask import send_from_directory

app.config['suppress_callback_exceptions']=True



app.layout = html.Div(children=[
            html.Div(className="container", children=[
            html.Img(src='/assets/pic10.jpg'),
            html.Div(className="centered", children=[
            html.H1("🤘 Kids Just Want to Dance! 🤘"),
            html.H1("An NYC Concert Database")])]),
            dcc.Tabs(id="tabs", value="tab-1", children=[
        dcc.Tab(label='Top Genres', value='tab-1'),
        dcc.Tab(label='Average Price by Neighborhood', value='tab-2'),
        dcc.Tab(label='Locations of Free Concerts', value='tab-3'),
        dcc.Tab(label='Average Price by Genre', value='tab-4')
    ]),
    html.Div(id='tabs-content')
],)
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def display_content(value):
    if value == 'tab-1':
        return html.Div([dcc.Dropdown(
                id = 'borough-dropdown',
                options =[
                    {'label': 'Manhattan', 'value': 'Manhattan'},
                    {'label': 'Brooklyn', 'value': 'Brooklyn'},
                    {'label': 'Bronx', 'value': 'Bronx'},
                    {'label': 'Queens', 'value': 'Queens'}
                ],
                value='Manhattan'
            ),
        html.Div(id='borough-genre-output-container')])
    elif value == 'tab-2':
        #generate graph for tab2
        return html.Div([dcc.Graph(style= {'height':800}, figure= go.Figure(data = [
            go.Scatter(
                x=[tuples[1] for tuples in avg_price_neighborhood()],
                y=[tuples[0] for tuples in avg_price_neighborhood()],
                mode='markers',
                marker=dict(color='rgb(93, 164, 214)', size=10)
            )
        ],
        layout = go.Layout(
            title='Average Minimum Ticket Price in NYC Neighborhoods'
        )),
        )],
        )
    elif value == 'tab-3':
        #generate map for tab3
        return html.Div([dcc.Graph(style= {'height':800}, figure= go.Figure(data= [
        go.Scattermapbox(
        lat=[location[0] for location in locations_of_free_concerts()],
        lon=[location[1] for location in locations_of_free_concerts()],
        mode='markers',
        text=[location[2] for location in locations_of_free_concerts()]
        )
        ],
        layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
        accesstoken='pk.eyJ1IjoiYnJpYW5zcmVicmVuaWsiLCJhIjoiY2pueHczamFuMDUwejNxcGM1eHRyZm5teSJ9.NIOkbUhPC4alvnd67eRQVA',
        bearing=0,
        center=dict(
            lat=40.7831,
            lon=-73.9712
        ),
        style='dark',
        pitch=0,
        zoom=11
        ),
        )
        ))])
    elif value == 'tab-4':
        #generate graph for tab4
        return html.Div([dcc.Graph(style= {'height':800}, figure= go.Figure(data= [
        go.Bar(
        x=[tuples[1] for tuples in avg_price_by_genre()],
        y=[tuples[0] for tuples in avg_price_by_genre()],
        marker=dict(color='rgba(50, 171, 96, 0.6)', line=dict(color='rgba(50, 171, 96, 1.0)')),
        orientation= 'h'
        )
        ],
        layout = go.Layout(
            title='Average Minimum Ticket Price by Genre'
        )))])

#generate graph for top genres / borough in tab1
@app.callback(
    dash.dependencies.Output('borough-genre-output-container', 'children'),
    [dash.dependencies.Input('borough-dropdown', 'value')])
def update_figure(value):
    all_values = top_genres_borough(value)
    genres = []
    values = []
    for tuples in all_values:
        genres.append(tuples[0])
        values.append(tuples[1])
    return html.Div(dcc.Graph(
    figure=go.Figure(
        data=[
            go.Bar(
                x=genres,
                y=values,
                name='Top Genres',
                marker=go.bar.Marker(
                    color='rgb(55, 83, 109)'
                )
            )
        ],
        layout=go.Layout(
            title='Top Genres in Each Borough')
    ))
    )
