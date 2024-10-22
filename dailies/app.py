import plotly
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash
from bin.login import login
from bin.credentials import credentials_gui

def main_app():

    cred, client, account_infos = login()

    # Initialize the app
    app = Dash(__name__,
               assets_folder=('assets'))

    # App layout
    app.layout = html.Div([
        html.Header([
            html.Div(id="form", children=[
                    html.Div()]),
            html.Div(children="Tigh Sensei")
        ]),

        html.Article(children=[
             
            html.Button('Change Credentials and settings',
                        id='credentials_btn',
                        n_clicks=0),
             
            html.Button('Login',
                        id='login_btn',
                        n_clicks=0),
             
            html.Button('Collect Daily rewards',
                        id='claim_rewards_btn',
                        n_clicks=0)
        ]),

       html.Div(children=[
            html.Img(src='assets/tigh_sensei.png', alt='Tighnari Sensei',
                     id='tigh_sensei_img'),
            html.P(children="", id='update')
       ], id='tigh_sensei'),

       html.Div(children=[
           html.Div(style={'display': 'none'}, id='None1'),
           html.Div(style={'display': 'none'}, id='None2'),
           html.Div(style={'display': 'none'}, id='None3'),
           html.Div(style={'display': 'none'}, id='None4')
       ], style={'display': 'none'}),

        html.Div(children=[html.P([
        "Powered by ", 
        html.A("plotly", href="https://plotly.com/", target="_blank")
    ])], id='footer')
        
    ], id="bodytype")
    
    @callback (
        Output(component_id='update',
               component_property='children',
               allow_duplicate=True),
        Input(component_id='credentials_btn',
              component_property='n_clicks'),
        Input('None1', 'children'),
        prevent_initial_call=True
    )
    def run_credentials(n_clicks, none):
        credentials_gui()
        return "Tes informations ont été changées!"
    
    @callback (
        Output(component_id='update',
               component_property='children',
               allow_duplicate=True),
        Input(component_id='credentials_btn',
              component_property='n_clicks'),
        Input('None2', 'children'),
        prevent_initial_call=True
    )
    def run_credentials_waiting(n_clicks, none):
        return "Chargement des nouvelles informations..."
    
    @callback (
        Output(component_id='update',
               component_property='children',
               allow_duplicate=True),
        Input(component_id='login_btn',
              component_property='n_clicks'),
        Input('None3', 'children'),
        prevent_initial_call=True
    )
    def run_login(n_clicks, none):
        try :
            global cred, client, account_infos
            cred, client, account_infos = login()
            return f'Connection reussie! Bienvenu {account_infos.nickname}, \
                voyageur.se de Tayvat!'
        except:
            return f'Connection echouée...'
    
    @callback (
        Output(component_id='update',
               component_property='children'),
        Input(component_id='login_btn',
              component_property='n_clicks'),
        Input('None4', 'children'),
        prevent_initial_call=True
    )
    def run_login_waiting(n_clicks, none):
        return "Connection en cours..."

    # Run the app
    if __name__ == '__main__':
        app.run(debug=True, port=8050)

if __name__ == '__main__':
        main_app()