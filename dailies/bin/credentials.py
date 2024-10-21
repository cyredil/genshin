import tkinter as tk

from .utils import load_credentials, save_credentials, set_middle

def credentials_gui():

    cred = list(load_credentials('bin/credentials.ini'))

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

    password = tk.Entry(master, show='*')
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

    game = tk.IntVar(value=cred[5])
    game1 = tk.Radiobutton(master, text='Genshin Impact',
                           variable=game, value=0)
    game1.grid(row=6, column=0)
    game2 = tk.Radiobutton(master, text='Honkai: Star Rail',
                           variable=game, value=1)
    game2.grid(row=6, column=1)
    game2 = tk.Radiobutton(master, text='Honkai Impact 3rd',
                           variable=game, value=2)
    game2.grid(row=6, column=2)

    region = tk.IntVar(value=cred[6])
    regi1 = tk.Radiobutton(master, text='Not China',
                           variable=region, value=0)
    regi1.grid(row=7, column=0)
    regi2 = tk.Radiobutton(master, text='China',
                           variable=region, value=1)
    regi2.grid(row=7, column=1)

    def on_send():
        cred = [mail.get(),
                password.get(),
                mail_save_var.get(),
                password_save_var.get(),
                browser.get(),
                game.get(),
                region.get()]
        save_credentials('bin/credentials.ini', cred)
        master.destroy()


    save_and_exit_button = tk.Button(master, text='Send', width=25, 
                                    command=on_send)
    save_and_exit_button.grid(row=8, columnspan=2)

    set_middle(master)

    master.mainloop()

if __name__ == "__main__":
    credentials_gui()