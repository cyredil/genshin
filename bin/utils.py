

# --- Importing packages ---
import configparser
import genshin
from dash import html


# --- Defining utils base functions ---

def load_credentials(filename):
    """load credential of the user, saved in bin/credentials.ini

    Args:
        filename (str): Complete file path string.

    Returns:
        str: User Username.
        str: User password.
        str: The 'save_username' boolean value
        str: The 'save_password' boolean value
        str: User default browser boolean value
        str: User default game boolean value
        str: User default region boolean value
    """
    config = configparser.ConfigParser()

    # Checking and reading if filename does exist and isn't empty
    not config.read(filename)
    
    # Loading every useful credentials
    username = config.get('Credentials', 'username', fallback='')
    password = config.get('Credentials', 'password', fallback='')
    save_username = config.get('Settings', 'save_username',
                               fallback='')
    save_password = config.get('Settings', 'save_password',
                               fallback='')
    browser = config.get('Settings', 'browser', fallback='')
    game = config.get('Settings', 'game', fallback='')
    region = config.get('Settings', 'region', fallback='')

    # Returning as a tuple
    return (username, password, save_username, save_password, browser,
            game, region)

def save_credentials(filename, credentials):
    """Save new credentials at filename path

    Args:
        filename (str): Complete file path string
        credentials (list): List of credentials to save with following
            indexes:
                0 - User Username.
                1 - User password.
                2 - The 'save_username' boolean value
                3 - The 'save_password' boolean value
                4 - User default browser boolean value
                5 - User default game boolean value
                6 - User default region boolean value
    """
    # Set config as a configParser object
    config = configparser.ConfigParser()

    # Saving user credentials
    config['Credentials'] = {
        'username': credentials[0],
        'password': credentials[1]
    }

    # Saving user settings
    config['Settings'] = {
        'save_username': credentials[2],
        'save_password': credentials[3],
        'browser': credentials[4],
        'game' : credentials[5],
        'region' : credentials[6]
    }

    # Saving them in filename config file
    with open(filename, 'w') as configfile:
        config.write(configfile)


def set_middle(master):
    """Set a Tk type object in the middle position of the screen

    Args:
        master (Tk): Tk object to center
    """
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
    """Function to call to claim daily calendar rewards

    Args:
        client (genshin.client): genshin.client object with cookies setted
    
    Returns:
        str: String stating if the reward was already claimed or not
    """
    # Trying to claim rewards
    try:
        reward = await client.claim_daily_reward()

    # If not possible, assumes the reward was already claimed
    except genshin.AlreadyClaimed:
        return "BOT: Daily reward already claimed"
    
    # If possible, states the reward amout and reward name
    else:
        return f"BOT: Claimed {reward.amount}x {reward.name}"

async def get_record_cards(client):
    """List of all game acounts of the currently logged in user"""
    return await client.get_record_cards(client.hoyolab_id)

def formating_bot_message(message):
    """Formating message for good css diferentiation
    
    Args:
        message (str): String starting either with 'BOT :' or with 'USER :'
    
    Returns:
        dash.html.Div: Returning a dash.html.Div with the message
            stripped out of the bot or user info and with an correct
            className"""
    if message[:3]=='BOT':
        return html.Div(message[5:], className='Bot_message')
    elif message[:4]=='USER':
        return html.Div(message[6:], className='User_message')