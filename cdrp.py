import tkinter as tk
import tkinter.ttk as ttk
import os
import pypresence
import time
import threading


class DiscordPresence:
    def __init__(self):
        self.DISCORD_CLIENT_ID = "621589019129544718"
        self.rpc_connected = False
        self.presence_enabled = False
        self.presence_stopped = True
        self.rpc = pypresence.Presence(self.DISCORD_CLIENT_ID)
        self.ac = pypresence.Activity(self.rpc)

    def set_presence(self, state):
        if not self.rpc_connected:
            self.rpc.connect()
        self.ac.state = state
        self.presence_enabled = True;
        while self.presence_enabled:
            pass
        self.presence_stopped = True
        return True

    def cancel_presence(self):
        self.presence_enabled = False;
        while not self.presence_stopped:
            pass
        return True


class Application:
    def start_presence(self):
        pass

    def __init__(self):
        self.APPLICATION_NAME = "Custom Discord Presence"
        self.APPLICATION_VERSION = "0.1"
        self.dp = DiscordPresence()
        self.root = tk.Tk()
        self.root.title(self.APPLICATION_NAME)
        self.root.iconbitmap(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                          "favicon.ico"))
        self.root["bg"] = "#2c2f33"
        self.dp_status = tk.StringVar(self.root)
        self.set_button_label = tk.StringVar(self.root)
        tk.Label(self.root, 
                 text=self.APPLICATION_NAME, 
                 font=("Uni Sans Heavy Italic CAPS", 24), 
                 bg="#2c2f33",
                 fg="#ffffff",
                 justify=tk.CENTER).pack(padx=14, 
                                         pady=6,
                                         side=tk.TOP)
        tk.Label(self.root,
                 text="set your own Discord Rich Presence",
                 font=("Uni Sans Thin CAPS", 11),
                 bg="#2c2f33",
                 fg="#ffffff",
                 justify=tk.CENTER).pack(side=tk.TOP)
        ttk.Separator(self.root, 
                      orient='horizontal').pack(side=tk.TOP,
                                                fill=tk.BOTH)
        tk.Label(self.root,
                 text="Client ID",
                 font=("Uni Sans Thin CAPS", 14),
                 bg="#2c2f33",
                 fg="#ffffff",
                 justify=tk.LEFT).pack(side=tk.TOP)
        ttk.Entry(self.root,
                  font=("Helvetica Bold", 16),
                  justify=tk.CENTER).pack(pady=6,
                                          side=tk.TOP)
        tk.Label(self.root,
                 text="Presence",
                 font=("Uni Sans Thin CAPS", 14),
                 bg="#2c2f33",
                 fg="#ffffff",
                 justify=tk.LEFT).pack(side=tk.TOP)
        ttk.Entry(self.root,
                  font=("Helvetica Bold", 16),
                  justify=tk.CENTER).pack(pady=6,
                                          side=tk.TOP)
        tk.Button(self.root,
                  textvariable=self.set_button_label,
                  font=("Uni Sans Heavy CAPS", 14),
                  bg="#7289da",
                  fg="#ffffff").pack(pady=10,
                                     side=tk.TOP)
        self.set_button_label.set("Set Rich Presence")
        ttk.Separator(self.root, 
                      orient='horizontal').pack(side=tk.TOP,
                                                fill=tk.BOTH)
        tk.Label(self.root,
                 textvariable=self.dp_status,
                 font=("Uni Sans Heavy CAPS", 11),
                 bg="#2c2f33",
                 fg="#ffffff",
                 justify=tk.CENTER).pack(side=tk.TOP)
        self.dp_status.set("Status: "+"Not set")
        tk.Label(self.root,
                 text="{0} v {1}. Made with <) by jkelol111".format(self.APPLICATION_NAME, self.APPLICATION_VERSION),
                 font=("Uni Sans Thin CAPS", 10),
                 bg="#2c2f33",
                 fg="#ffffff",
                 justify=tk.CENTER).pack(pady=6,
                                         side=tk.TOP)
        self.root.mainloop()

if __name__ == "__main__":
    # test = DiscordPresence()
    # def testrpc():
    #     test.set_presence("Custom Presence!")
    # threading.Thread(target=testrpc).start()
    # time.sleep(15)
    # test.cancel_presence()
    Application()