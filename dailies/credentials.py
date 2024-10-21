import genshin
import tkinter as tk
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

def credentials_gui():

    cred = list(load_credentials('dailies/credentials.ini'))

    ## Creating widget
    master = tk.Tk()

    master.title('Credentials.exe')

    explication = tk.Message(master, text="BONJOUR", width=250)
    explication.grid(row=0,columnspan=2)

    tk.Label(master, text="email :").grid(row=1)
    tk.Label(master, text="password").grid(row=2)

    mail = tk.Entry(master)
    mail.insert(0, cred[0])
    mail.grid(row=1, column=1)

    password = tk.Entry(master)
    password.insert(0, cred[1])
    password.grid(row=2, column=1)

    mail_save_var = tk.IntVar(value=cred[2])
    mail_save = tk.Checkbutton(master, text='Save mail',
                               variable=mail_save_var)
    mail_save.grid(row=3, sticky='W')

    password_save_var = tk.IntVar(value=cred[3])
    password_save = tk.Checkbutton(master, text='Save password',
                               variable=password_save_var)
    password_save.grid(row=4, sticky='W')

    browser = tk.IntVar(value=cred[4])
    brow1 = tk.Radiobutton(master, text='Chrome',
                           variable=browser, value=0)
    brow1.grid(row=5, column=0)
    brow2 = tk.Radiobutton(master, text='FireFox',
                           variable=browser, value=1)
    brow2.grid(row=5, column=1)
        
    def on_send():
        cred = [mail.get(),
                password.get(),
                mail_save_var.get(),
                password_save_var.get(),
                browser.get()]
        save_credentials('dailies/credentials.ini', cred)
        master.destroy()


    save_and_exit_button = tk.Button(master, text='Send', width=25, 
                                    command=on_send)
    save_and_exit_button.grid(row=6, columnspan=2)

    set_middle(master)

    master.mainloop()

if __name__ == "__main__":
    credentials_gui()