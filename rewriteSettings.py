import string
import re

def changeSettings():

    f = open('settings.toml')
    text = f.read()
    settingsRegex = "'(?:[^']|'')*'"
    newText = re.sub(settingsRegex, "'LMAO'", text)
    f.write(newText)
    f.close()




if __name__ == "__main__":
    changeSettings()