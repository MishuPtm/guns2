Settings.MoveMouseDelay = 0.8
delay = 0.6
distance = 240
counter = 1
maxInstance = 8
cycleCount = 2

#doubleClick("1543343472864.png")
shipment = Pattern("1543352147086.png").similar(0.90)
xIcon = Pattern("xicon.png").similar(0.80)
barracks = Pattern("barracks.png").similar(0.71)
artillery = Pattern("artillery.png").similar(0.71)
shooting = Pattern("shooting.png").similar(0.71)
stables = Pattern("stables.png").similar(0.71)

castle = Pattern("castle.png").similar(0.43)
kingdom = Pattern("kingdom.png").similar(0.62)
estate = Pattern("estate.png").similar(0.66)
farm = Pattern("farm.png").similar(0.68)
lumberyard = Pattern("lumberyard.png").similar(0.68)
ironMine = Pattern("ironMine.png").similar(0.65)
trainIcon = Pattern("1543349542800.png").similar(0.60)
speedUp = Pattern("speedUp.png").similar(0.50)
upgradeIcon = Pattern("upgradeIcon.png").similar(0.58)
helpIcon = Pattern("helpIcon.png").similar(0.61)
helpAllies = Pattern("helpAllies.png").similar(0.72)
trainedTroops = "trainedTroops.png"
trainBtn = Pattern("1543350408501.png").similar(0.96)
goTo = Pattern("goTo.png").similar(0.68)
equalizeBtn = Pattern("equalizeBtn.png").similar(0.80)
upgradeBtn = Pattern("upgradeBtn.png").exact()
marchBtn = Pattern("marchBtn.png").similar(0.60).targetOffset(-1,13)
tipsBtn = Pattern("tipsBtn.png").similar(0.76)
tipsIcon= Pattern("tipsIcon.png").similar(0.77)
activateVip = Pattern("activateVip.png").similar(0.80)
marchFull = Pattern("marchFull.png").similar(0.68)
notEnough = Pattern("notEnough.png").similar(0.63)
wood = Pattern("wood.png").similar(0.80)
food = Pattern("food.png").similar(0.80)
quit = Pattern("quit.png").similar(0.81).targetOffset(79,65)
troopsTraining = Pattern("troopsTraining.png").similar(0.74)
resourceBusy = Pattern("resourceBusy.png").similar(0.68)
callBack = Pattern("callBack.png").similar(0.65)
occupy = "occupy.png"
insideBuildRef = Pattern("insideBuildRef.png").similar(0.65).targetOffset(-175,419)
minTierSelected = Pattern("minTierSelected.png").similar(0.85)
goldChest = Pattern("goldChest.png").similar(0.89)
openBtn = Pattern("openBtn.png").similar(0.75)
gunsIcon = "gunsIcon.png"
freeWeapons = "1545083917425.png"
munitionFood = "munitionFood.png"

currentRess = farm
import datetime
logFilename = "logs\\" + unicode(datetime.datetime.now()).replace(':', '-')+".txt"
#logFilename = "textLog.txt"
def writeLog(message):
    if True:
        f = open(logFilename, "a+")
        f.write("[" + str(datetime.datetime.now()) + "][Farm " + str(counter) + "]"+ message + "\n")
        f.close()

def makeNumberIfNumber(numberString):
    try:
        number = float(numberString)
        return number if '.' in numberString else int(number)
    except:
        return numberString

def loadSettings():
    try:
        return importSettings(str(counter)+".txt")
    except:
        return importSettings("default.txt")
    
def importSettings(fileName):
    print 'Reading settings'
    f = open(fileName, "r")
    settingsLines = f.read().split("\n")
    f.close()
    settings = {}
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
def stringToPattern(text):
    switcher = {
        "lumberyard":lumberyard,
        "farm":farm,
        "ironMine":ironMine,
        "barracks":barracks,
        "artillery":artillery,
        "shooting":shooting,
        "stables":stables,
        "castle":castle
        }
    return switcher.get(text, None)
class Farm:
    def __init__(self, number):
        self.number = number
        self.army = [shooting, barracks, stables, artillery]
        self.settings = loadSettings()
        
    def start(self):
        if exists(shipment):
            
            self.tryClick(shipment, 1)
            wait(12)
        self.tryClick(xIcon, 1)
        wait(3)
        self.tryClick(xIcon, 1)
            
    def scan(self):
        #self.tryClick(trainedTroops, 1)
        #self.tryClick(wood, 1)
        #self.tryClick(food, 1)
        i = len(self.army)-1
        while i>=0:
            
            if exists(self.army[i]):
                self.train(self.army[i])
                    
            print(len(self.army))
            i-=1
    def train(self, building):
        
        #writeLog(str(resource))
        self.center(building)
        self.tryClick(building, 2)
        wait(1)
        if exists(trainIcon, 2):
            self.tryClick(trainIcon, 2)
        else:
            self.tryClick(building, 2)
            wait(1)
        self.tryClick(trainIcon, 2) 
        wait(2)
        if exists(troopsTraining):
            wait (1)
            self.tryClick(xIcon, 0.5)
        
        if self.settings["trainMinLevel"] and exists(insideBuildRef, 2):
            i = 0
            while not exists(minTierSelected, 1):
                self.tryClick(insideBuildRef, 0.5)
                
                if i>12:
                    break
                i += 1
            
        if self.tryClick(trainBtn, 4):
            wait(1)
            self.tryClick(xIcon, 2)
            

    def tryClick(self, pattern, period):
        if exists(pattern, period):
            click(pattern)
            return True
    
    def center(self, pattern):
        if exists(pattern, 4):
            dragDrop(pattern, Pattern("1543427171194.png").similar(0.80).targetOffset(290,162))

    def upgrade(self): 
        wait(1)
        if self.tryClick(tipsIcon, 2):
            wait(3)
            self.tryClick(tipsBtn, 2)
            wait(2)

        hover(Pattern("1543427171194.png").similar(0.80).targetOffset(283,208))
        wait(1)
        mouseDown(Button.LEFT)
        mouseUp()
        wait(1)  
            
        if not exists(upgradeIcon) and not exists(speedUp):
            hover(Pattern("1543427171194.png").similar(0.80).targetOffset(283,208))
            wait(1)
            mouseDown(Button.LEFT)
            mouseUp()
            wait(1)  
            
        if self.tryClick(upgradeIcon, 2):
            wait(2)
            if self.tryClick(goTo, 1):
                wait(2)
                self.upgrade()
            else:
                if self.tryClick(upgradeBtn, 2):
                    if self.tryClick(helpIcon, 2):
                        writeLog("Building upgraded")
                wait(1)
                self.tryClick(xIcon, 1)
                wait(1)
                self.tryClick(xIcon, 1)
                writeLog("Not enough resources to upgrade")
                    
        else:
           if exists(speedUp):
               writeLog("Upgrade already in progress")
               self.tryBuild = False
            #if upgrade icon not available#
             
        
    def openGoldChest(self):
        if self.tryClick(goldChest, 5):
            wait(5)
            writeLog("Found gold chest")
            while self.tryClick(openBtn, 2):              
                wait(3)  
            wait(1)
            writeLog("Opened all chests")
            self.tryClick(xIcon, 2)
            wait(2)
            self.tryClick(xIcon, 2)

        
    def gather(self, resources):
        dir1 = self.settings["gatherDir"][0]
        dir2 = self.settings["gatherDir"][1]
        if not self.tryClick(kingdom, 1):
            self.tryClick(kingdom, 2)
        wait(10)    
        steps = 1
        marches = self.getAvailableMarch()
        if marches > 0:
            writeLog("Gathering " + str(self.settings["gatherRess"]))
        else: 
            writeLog("No available marches")  
                   
            
        while steps < 100 and marches > 0:
            if steps % 10 == 0:
                self.move(dir2)
                self.move(dir2)
                self.move(dir2)
                if dir1 == 1:
                    dir1 = 2
                elif dir1 == 2:
                    dir1 = 1
                elif dir1 == 3:
                    dir1 = 4
                elif dir1 == 4:
                    dir1 = 3
            else:
                self.move(dir1)

            steps += 1
            for resource in resources:
                if exists(resource):
                    self.center(resource)
                    self.tryClick(resource, 1)
                    if not exists(resourceBusy) and not exists(occupy):
                        self.tryClick(resource, 2)
                    
                    if exists(occupy):
                        if self.tryClick(occupy, 1):
                            
                            wait(2)
                            if exists(marchFull):
                                marches = 0
                                wait(2)
                                
                                self.tryClick(xIcon, 1)
                                wait(1)
                            self.tryClick(equalizeBtn, 1)
                            wait(1)
                            if not self.tryClick(marchBtn, 1):
                                self.tryClick(xIcon, 1)
                                marches = 0
                            else:
                                marches -= 1
                                self.move(dir1)
                                self.move(dir1)
                                break
                                
                                
                    elif exists(resourceBusy) or exists(callBack):
                        self.move(dir1)
                        self.move(dir1)
        self.tryClick(estate, 2)     
                
    def move(self, direction):
        #1 up, 2 down, 3 left, 4, right
        center = Pattern("1543427171194.png").similar(0.80).targetOffset(288,211)
        
        hover(center)
        mouseDown(Button.LEFT)
        wait(delay)
        if direction == 1:
            hover(Pattern("1543427171194.png").similar(0.80).targetOffset(290,182+distance))
        elif direction == 2:
            hover(Pattern("1543427171194.png").similar(0.80).targetOffset(290,182-distance))
        elif direction == 3:
            hover(Pattern("1543427171194.png").similar(0.80).targetOffset(290+distance,182))
        elif direction == 4:
            hover(Pattern("1543427171194.png").similar(0.80).targetOffset(290-distance,182))

        mouseUp()

    def findCastle(self):
        wait(2)
        self.findTopLeft()
        self.move(2)
        self.move(4)
        self.move(4)
        if exists(castle, 2):
            self.center(castle)
            wait(1)
            return True
        else:
            return False
    #def base(self):

    def munitionExchange(self, ress):
        wait(2)
        self.findTopLeft()
        self.move(2)
        self.move(2)
        self.move(4)
        self.move(4)
        if self.tryClick(gunsIcon, 2):
            writeLog("Found munition exchange")
            wait(4)
            x=0
            while exists(freeWeapons) and x < 20:
                self.tryClick(ress, 1)
                wait(2)
            self.tryClick(xIcon, 1)
        else:
            writeLog("No free weapons")
        if self.tryClick(helpAllies, 2):
            writeLog("Helped allies")
            wait(2)
    def findTopLeft (self):
        if exists(kingdom, 1): 
            steps = 0
            while not exists(Pattern("1544040185056.png").similar(0.62), 1) and steps < 20:
                self.move(1)
                self.move(3)
                steps += 1
                
        return exists(Pattern("1544040185056.png").similar(0.62), 1)
             
    def findBottomRight (self):
        if exists(kingdom, 1):
            while not exists(Pattern("1544040235407.png").similar(0.68), 1):
                self.move(2)
                self.move(4)
                self.move(2)
                self.move(4)
                self.move(2)
                self.move(4)
        return True

    
    def perfActions(self):
        for action in self.settings["actions"]:
            wait(3)
            if action == "train":
                for troop in self.settings["troopsToTrain"]:
                    writeLog("Training " + troop)
                    self.train(stringToPattern(troop))
            elif action == "gather":
                
                test = []
                for ress in self.settings["gatherRess"]:
                    if not ress == None:
                        test.append(stringToPattern(ress))
                self.gather(test)
            elif action == "upgrade":
                writeLog("Upgrading")
                self.findCastle()
                self.upgrade()
            elif action == "gold":
                self.openGoldChest()   
            elif action == "munition":
                self.munitionExchange(munitionFood)
    def recover(self):
        writeLog("Attempting recovery")
        wait(1)
        self.tryClick(xIcon, 1)
        wait(1)
        self.tryClick(estate, 1)
        wait(1)
        self.tryClick(tipsBtn, 1)
        
    def getAvailableMarch(self):
        x=0
        self.tryClick(Pattern("1545166899288.png").similar(0.57), 2)
        try:
            mm =  findAll(Pattern("1544560966058.png").similar(0.69))
            while mm.hasNext():
                mm.next()
                #finding troops on the move
                x+=1
        except:
            pass
        try:
            nn = findAll(Pattern("1544560981707.png").similar(0.57)) 
            while nn.hasNext(): # loop as long there is a first and more matches
                #finding troops gathering
                nn.next()
                x+=1
        except:
            pass
            
        return self.settings["availableMarch"]-x
                
        

                        

                        
                        
def launchEmu(instance):
    click("1544032444964.png")
    hover(Pattern("1544032444964.png").targetOffset(0,instance*50)) 
     
    mouseDown(Button.LEFT)
    mouseUp()  
    wait("1543346082405.png", 120)
    click("1543346082405.png")
    writeLog("Starting farm")
    wait(xIcon, 120)

def closeEmu():
    if exists(Pattern("1544174098594.png").targetOffset(82,1)):
    	click(Pattern("1544174098594.png").targetOffset(82,1))
    click("1544032444964.png")
    wait(1)
    global counter
    global cycleCount
    global currentRess
    click(Pattern("1543446303461.png").targetOffset(34,0))
    wait(6)
    if counter<maxInstance:
        counter+=1
    else:
        
        counter = 1
        cycleCount += 1
        writeLog("....")
        writeLog("....")
        
        if cycleCount % 300 == 0:
            if currentRess == farm:
                currentRess = lumberyard
            else:
                currentRess = farm


#launchEmu(counter)
#instance = Farm(1)
#instance.start()
#instance.perfActions()

while True:
    try:
        launchEmu(counter)
        instance = Farm(1)
        instance.start()
        instance.perfActions()
        writeLog("Actions finished, closing instance")
        closeEmu()
    except:
        #writeLog("[WARNING]Action failed, closing instance")
        closeEmu()
    wait(5)

    