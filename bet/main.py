import pyautogui
import webbrowser
import json


def config():
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)
    return data
config = config()

def bet():
    
