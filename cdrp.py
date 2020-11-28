__author__ = 'jkelol111'
__copyright__ = 'Copyright (C) 2020-present jkelol111.'
__license__ = 'GNU General Public License Version 3'
__version__ = '1.0.1'

import os
import pathlib
import json
import pypresence
import time
import colorama

colorama.init(autoreset=True)

print(f"{colorama.Style.BRIGHT}{colorama.Fore.GREEN}CustomDiscordPresence v{__version__}. {__copyright__}")
print(f"{colorama.Fore.YELLOW}Licenced to you under the {__license__}.")
print("")
print("Searching for cdrpcfg.json...")

CONFIG_FILE_PATH = os.path.join(pathlib.Path(__file__).parent, "cdrpcfg.json")
config = {}
if os.path.isfile(CONFIG_FILE_PATH):
    with open(CONFIG_FILE_PATH, "r") as CONFIG_FILE:
        config = json.load(CONFIG_FILE)
    print(f"{colorama.Fore.GREEN}Found and loaded the config file!")
else:
    print(f"{colorama.Fore.RED}Config file not found! Exiting...")
    exit()

print("Starting the Rich Presence RPC...")
RPC = pypresence.Presence(config["client_id"])
RPC.connect()

def update_rpc():
    RPC.update(state=config["state"]["state"], 
            details=config["state"]["details"], 
            start=config["state"]["timestamps"]["start"], 
            end=config["state"]["timestamps"]["end"],
            large_image=config["images"]["large"]["name"],
            large_text=config["images"]["large"]["tooltip"],
            small_image=config["images"]["small"]["name"],
            small_text=config["images"]["small"]["tooltip"])
    print(f"{colorama.Fore.GREEN}Rich Presence RPC connected and updated!")

def quit_rpc():
    RPC.clear()
    RPC.close()
    exit()

update_rpc()

try:
    while True:
        try:
            with open(CONFIG_FILE_PATH, "r") as CONFIG_FILE:
                new_config = json.load(CONFIG_FILE)
                if config != new_config:
                    config = new_config
                    print(f"{colorama.Fore.YELLOW}Change in config file detected, reloading!")
                    update_rpc()
        except Exception as e:
            print(f"{colorama.Fore.RED}Failed to reload config file! Exception:")
            print(str(e))
            print(f"{colorama.Fore.RED}Couldn't continue, quitting!")
            quit_rpc()
        time.sleep(15)
except KeyboardInterrupt:
    print(f"\n{colorama.Fore.YELLOW}Keyboard interrupt caught, exiting...")
    quit_rpc()