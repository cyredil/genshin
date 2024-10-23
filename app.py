import io
import sys
import pandas as pd
import plotly
from dash import Dash, html, dcc, callback, Output, Input, State
from bin.login import login
from bin.credentials import credentials_gui
from bin.utils import claim_reward, formating_bot_message
from bin.promo_codes import scrap_promo_codes, test_promo_codes
import asyncio

def main_app():

    # Initialize the app
    app = Dash(__name__,
               assets_folder=('assets'))

    output_buffer = io.StringIO()
    sys.stdout = output_buffer


    # App layout
    app.layout = html.Div([
        html.Header([
            html.Div(id="form", children=[
                    html.Div()]),
            html.Div(children="Tigh Sensei")
        ]),

        html.Article(children=[
             
            html.Button('Credentials & Settings',
                        id='credentials_btn',
                        n_clicks=0),
             
            html.Button('Login',
                        id='login_btn',
                        n_clicks=0),
             
            html.Button('Collect Daily Calender Rewards',
                        id='claim_reward_btn',
                        n_clicks=0),
             
            html.Button('Collect Genshin Promo Codes',
                        id='claim_genshin_codes_btn',
                        n_clicks=0)
        ]),

       html.Div(children=[
            html.Img(src='assets/tigh_sensei.png', alt='Tighnari Sensei',
                     id='tigh_sensei_img'),
            dcc.Interval(id='interval-messages', interval=1000, n_intervals=0),
            html.Div(children=[html.Div(children=[html.Button('Send', id='chat-send-button', n_clicks=0),
                               dcc.Textarea(id='chat-box', value='Talk with tighnari!')],
                               id='chat'),
                               html.Div(id='update', className='chat-container')],
                     id='outerupdatediv'),
       ], id='tigh_sensei'),

       html.Div(style={'display': 'none'},
                id='hidden_output'),

        html.Div(children=[html.P([
        "Powered by ", 
        html.A("plotly", href="https://plotly.com/", target="_blank")
    ])], id='footer')
        
    ], id="bodytype")
    
    @callback (
        Output('update', 'children'),
        Input('interval-messages', 'n_intervals')
    )
    def print_formated_messages(n):
        messages = output_buffer.getvalue().strip().split('\n')
        formatted_messages = []
        
        for i in messages:
            formatted_messages.append(formating_bot_message(i))
        return formatted_messages

    @callback (
        Output('chat-box', 'value'),
        Output('hidden_output', 'children', allow_duplicate=True),
        Input('chat-send-button', 'n_clicks'),
        State('chat-box', 'value'),
        prevent_initial_call=True
    )
    def talk_with_tigh(n_clicks, value):
        print(f'USER: {value}')
        return 'Talk with tighnari!', None

    @callback (
        Output('hidden_output', 'children', allow_duplicate=True),
        Input('credentials_btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def run_credentials(n_clicks):
        print("BOT: Asking for new credentials...")
        credentials_gui()
        print("BOT: Credentials succesfully changed!")
    
    @callback (
        Output('hidden_output', 'children', allow_duplicate=True),
        Input('login_btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def run_login(n_clicks):
        print("BOT: Connectiong...")
        try :
            global cred, client, cards
            cred, client, cards = login()
            print(f'BOT: Connection established! Welcome {cards[0].nickname},',
                  'Teyvat traveler!')
        except:
            print('BOT: Cannot log in...')

    @callback (
        Output('hidden_output', 'children', allow_duplicate=True),
        Input('claim_reward_btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def run_claim_reward(n_clicks):
        print('BOT: Claiming rewards...')
        if 'client' in globals():
            print(asyncio.run(claim_reward(client)))
        else:
            print("BOT: You didn't log in!")
    
    @callback (
        Output('hidden_output', 'children'),
        Input('claim_genshin_codes_btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def run_claim_genshin_codes(n_clicks):
        if n_clicks==1:
            print('BOT: Searching all available promo codes')
            scrap_promo_codes()
            print('BOT: Done!')
        print(test_promo_codes(pd.read_csv('bin/promo_codes.csv'), client))


    # Run the app
    if __name__ == '__main__':
        app.run(debug=True, port=8050)

if __name__ == '__main__':
        main_app()