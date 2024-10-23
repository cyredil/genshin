
import configparser
import genshin
from dash import html

def load_credentials(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    username = config.get('Credentials', 'username', fallback='')
    password = config.get('Credentials', 'password', fallback='')
    save_username = config.get('Settings', 'save_username',
                               fallback='')
    save_password = config.get('Settings', 'save_password',
                               fallback='')
    browser = config.get('Settings', 'browser', fallback='')
    game = config.get('Settings', 'game', fallback='')
    region = config.get('Settings', 'region', fallback='')

    return (username, password, save_username, save_password, browser,
            game, region)

def save_credentials(filename, credentials):
    config = configparser.ConfigParser()
    config.read(filename)

    config['Credentials'] = {
        'username': credentials[0],
        'password': credentials[1]
    }
    config['Settings'] = {
        'save_username': credentials[2],
        'save_password': credentials[3],
        'browser': credentials[4],
        'game' : credentials[5],
        'region' : credentials[6]
    }

    with open(filename, 'w') as configfile:
        config.write(configfile)


def set_middle(master):
    # Set the desired size for the window
    width = 300   # Width of the window
    height = 250  # Height of the window

    # Get the screen width and height
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the geometry of the window
    master.geometry(f"{width}x{height}+{x}+{y}")

async def claim_reward(client):
    try:
        reward = await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        return "BOT: Daily reward already claimed"
    else:
        return f"BOT: Claimed {reward.amount}x {reward.name}"

async def get_record_cards(client):
    # list of all game accounts of the currently logged-in user
    return await client.get_record_cards(client.hoyolab_id)

def formating_bot_message(message):
    if message[:3]=='BOT':
        return html.Div(message[5:], className='Bot_message')
    elif message[:4]=='USER':
        return html.Div(message[6:], className='User_message')