import json

def getConfig():
    with open("var/config.json", "r") as configFile:
        config = json.load(configFile)
    return config

config = getConfig()

def getPassword():
    return config["password"]

