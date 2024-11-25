# Importing Libraries
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

# Creating an dashboard (webapp)
def main_app():

    # Initialize the app with .css sheet location
    app = Dash(__name__,
               assets_folder=('assets'))

    # Initializing buffer to keep traces of prints and display them
    output_buffer = io.StringIO()
    sys.stdout = output_buffer

    # Try first log in with stored user datas
    print("BOT: Connecting...")

    # Try to login and store user infos
    try :
        global client, cards
        client, cards = login()
        print(f'BOT: Connection established! Welcome {cards[0].nickname},',
            'Teyvat traveler!')
    # Else, print it couldn't log in
    except:
        print("BOT: You aren't logged in, check credentials!")

    # App layout
    app.layout = html.Div([
        ## Header with page name
        html.Header([
            html.Div(id="form", children=[
                    html.Div()]),
            html.Div(children="Tigh Sensei")
        ]),

        ## Main article : All implemented possibilities
        html.Article(children=[
            ### Button handling credentials and settings
            html.Button('Credentials & Settings',
                        id='credentials_btn',
                        n_clicks=0),
             
            ### Button handling login
            html.Button('Login',
                        id='login_btn',
                        n_clicks=0),
            
            ### Button handling daily calendar collect
            html.Button('Collect Daily Calendar Rewards',
                        id='claim_reward_btn',
                        n_clicks=0),
             
            ### Button handlin genshin promo codes collect (new ones only)
            html.Button('Collect Genshin Promo Codes',
                        id='claim_genshin_codes_btn',
                        n_clicks=0)
        ]),

        ## Tighnari Chat Bot
        html.Div(children=[
            html.Img(src='assets/tigh_sensei.png', alt='Tighnari Sensei',
                     id='tigh_sensei_img'),
            ### Adding new prints every seconds
            dcc.Interval(id='interval-messages', interval=500, n_intervals=0),

            ### Chat bot box
            html.Div(children=[html.Div(children=[html.Button('Send', id='chat-send-button', n_clicks=0),
                               dcc.Textarea(id='chat-box',
                                            value='',
                                            placeholder='Chat with Tigh Sensei!')],
                               id='chat'),
                               html.Div(id='update', className='chat-container')],
                     id='outerupdatediv'),
       ], id='tigh_sensei'),

        ## Hiden Div to handle duplacate callback outputs and inputs
        html.Div(style={'display': 'none'},
                id='hidden_output'),

        ## Footer
        html.Div(children=[html.P([
        "Powered by ", 
        html.A("plotly", href="https://plotly.com/", target="_blank")
    ])], id='footer')
        
    ], id="bodytype")
    
    
    # --- Defining callbacks ---

    # Call back handling messages printed
    @callback (
        Output('update', 'children'),
        Input('interval-messages', 'n_intervals')
    )
    def print_formated_messages(n):
        # Exctracting messages
        messages = output_buffer.getvalue().strip().split('\n')
        formatted_messages = []
        
        # Formatting message with `formarting_bot_message`
        for i in messages:
            if len(i) > 6: ## CHANGE FOR A CORRECT MESSAGE FUNCTION
                formatted_messages.append(formating_bot_message(i))
        return formatted_messages

    # Callback allowing user to send message to tignari
    @callback (
        Output('chat-box', 'value'),
        Output('hidden_output', 'children', allow_duplicate=True),
        Input('chat-send-button', 'n_clicks'),
        State('chat-box', 'value'),
        prevent_initial_call=True
    )
    def talk_with_tigh(n_clicks, value):
        # print message as user
        print(f'USER: {value}')
        # reset chat default value
        return '', None

    #Callback handling credential and setting changes
    @callback (
        Output('hidden_output', 'children', allow_duplicate=True),
        Input('credentials_btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def run_credentials(n_clicks):
        print("BOT: Asking for new credentials...")
        credentials_gui()
        print("BOT: Credentials succesfully changed!")
    
    # Callback handling login
    @callback (
        Output('hidden_output', 'children', allow_duplicate=True),
        Input('login_btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def run_login(n_clicks):
        print("BOT: Connecting...")
        # Try to recover login info
        try :
            global client, cards
            client, cards = login()
            print(f'BOT: Connection established! Welcome {cards[0].nickname},',
                  'Teyvat traveler!')
        # Else, print it couldn't log in
        except:
            print('BOT: Cannot log in...')

    # Callback handling the claiming of daily calendar rewards
    @callback (
        Output('hidden_output', 'children', allow_duplicate=True),
        Input('claim_reward_btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def run_claim_reward(n_clicks):
        print('BOT: Claiming rewards...')
        # checking if user did log in, than run claim
        if 'client' in globals():
            print(asyncio.run(claim_reward(client)))
        else:
            print("BOT: You didn't log in!")
    
    # Callback handling genshin code claiming (new ones only)
    @callback (
        Output('hidden_output', 'children'),
        Input('claim_genshin_codes_btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def run_claim_genshin_codes(n_clicks):
        # First, if first time using it, refresh promo codes
        if n_clicks==1:
            print('BOT: Searching all available promo codes')
            scrap_promo_codes()
            print('BOT: Done!')
        # Then testing every new promo code
        # (optional arg new_only=True, see doc)
        print(test_promo_codes(pd.read_csv('bin/promo_codes.csv'), client))

    # Run the app
    if __name__ == '__main__':
        app.run(debug=True, port=8050)

if __name__ == '__main__':
        main_app()