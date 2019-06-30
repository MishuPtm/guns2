import datetime


def writeLog(debug, counter, message):
    logFilename = "logs\\" + unicode(datetime.datetime.now().date()).replace(':', '-')+".txt" 
    if debug:
        logFilename = "debug.txt"
    if message == ".":
        f = open(logFilename, "a+")
        f.write("=============================================================\n")
        f.close()
    else:
        f = open(logFilename, "a+")
        f.write("[" + str(datetime.datetime.now().time()) + "][Farm " + str(counter) + "]"+ message + "\n")
        f.close()
def makeNumberIfNumber(numberString):
    try:
        number = float(numberString)
        return number if '.' in numberString else int(number)
    except:
        return numberString

def loadSettings(counter):
    default = importSettings("default.txt")
    try:
        return importSettings(str(counter)+".txt", default)
    except:
        return importSettings("default.txt")


def importSettings(fileName, settings = {}):
    f = open(fileName, "r")
    settingsLines = f.read().split("\n")
    f.close()
    for line in settingsLines:
        if len(line.strip()) == 0:
            continue
        splitted = line.split(":")
        settingName = splitted[0].strip()
        settingValue = splitted[1].strip()
        if settingValue.lower() in ["true", "false"]:
            settingValue = settingValue == "true"
        elif "," in settingValue:
            #this means setting is an array
            settingValue = [makeNumberIfNumber(x.strip()) for x in settingValue.split(',')]
            
        settings[settingName] = makeNumberIfNumber(settingValue)
    return  settings

