import genshin
import tkinter as tk

def credentials_gui():

    ## Creating widget
    master = tk.Tk()

    master.title('Credentials.exe')

    explication = tk.Message(master, text="BONJOUR", width=250)
    explication.grid(row=0,columnspan=2)

    tk.Label(master, text="email :").grid(row=1)
    tk.Label(master, text="password").grid(row=2)

    mail = tk.Entry(master)
    mail.grid(row=1, column=1)
    password = tk.Entry(master)
    password.grid(row=2, column=1)

    def on_send():
        credentials = f'{mail.get()}:{password.get()}'
        with open('dailies/credentials.txt', 'w') as file:
            file.write(credentials)
        master.destroy()

    save_and_exit_button = tk.Button(master, text='Send', width=25, 
                                    command=on_send)
    save_and_exit_button.grid(row=3, columnspan=2)

    master.mainloop()

if __name__ == "__main__":
    credentials_gui()