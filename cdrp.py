__author__ = 'jkelol111'
__copyright__ = 'Copyright (C) 2020-present jkelol111.'
__license__ = 'Public Domain'
__version__ = '1.0.0'

import os
import pathlib
import json
import pypresence
import time
import colorama

colorama.init(autoreset=True)

print(f"{colorama.Style.BRIGHT}{colorama.Fore.GREEN}CustomDiscordPresence v{__version__}. {__copyright__}")
print("Searching for cdrpcfg.json...")

CONFIG_FILE_PATH = os.path.join(pathlib.Path(__file__).parent, "cdrpcfg.json")
CONFIG = {}
if os.path.isfile(CONFIG_FILE_PATH):
    with open(CONFIG_FILE_PATH, "r") as CONFIG_FILE:
        CONFIG = json.load(CONFIG_FILE)
    print(f"{colorama.Fore.GREEN}Found and loaded the config file!")
else:
    print(f"{colorama.Fore.RED}Config file not found! Exiting...")
    exit()

print("Starting the Rich Presence RPC...")
RPC = pypresence.Presence(CONFIG["client_id"])
RPC.connect()

RPC.update(state=CONFIG["state"]["state"], 
           details=CONFIG["state"]["details"], 
           start=CONFIG["state"]["timestamps"]["start"], 
           end=CONFIG["state"]["timestamps"]["end"],
           large_image=CONFIG["images"]["large"]["name"],
           large_text=CONFIG["images"]["large"]["tooltip"],
           small_image=CONFIG["images"]["small"]["name"],
           small_text=CONFIG["images"]["small"]["tooltip"])

try:
    print(f"{colorama.Fore.GREEN}Rich Presence RPC connected and updated!")
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    print(f"\n{colorama.Fore.YELLOW}Keyboard interrupt caught, exiting...")
    RPC.clear()
    RPC.close()
    exit()