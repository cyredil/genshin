
import configparser

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

    return username, password, save_username, save_password, browser

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
        'browser': credentials[4]
    }

    with open('dailies/credentials.ini', 'w') as configfile:
        config.write(configfile)


def set_middle(master):
    # Set the desired size for the window
    width = 300   # Width of the window
    height = 200  # Height of the window

    # Get the screen width and height
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the geometry of the window
    master.geometry(f"{width}x{height}+{x}+{y}")