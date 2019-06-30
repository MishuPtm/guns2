from fileOperations import *

debug = True
Settings.MoveMouseDelay = 0.8
counter = 2
minInstance = 1
maxInstance = 5
error = ""

xIcon = Pattern("xicon.png").similar(0.82)
kingdom = Pattern("kingdom.png").similar(0.62)
estate = Pattern("estate.png").similar(0.66)
callBack = Pattern("callBack.png").similar(0.65)

class Farm:
    def __init__(self, nb):
        self.number = nb
        self.settings = loadSettings(nb)
        

    def start(self):   
        shipment = Pattern("1543352147086.png").similar(0.90)
        if self.tryClick(shipment, 3):
            wait(12)
        self.tryClick(xIcon, 1)
        wait(3)
        self.tryClick(xIcon, 1)
        wait(4)
        self.tryClick(kingdom, 1)
        wait(2)
        if not self.tryClick(estate, 15):
            self.tryClick(estate, 5)
        wait(2)
           

    def donate(self):
        allianceIcon = Pattern("allianceIcon.png").similar(0.74)
        donations = "donations.png"
        star = "star.png"
        donateBtn = Pattern("donateBtn.png").similar(0.77).targetOffset(65,278)
        stopDonate = Pattern("stopDonate.png").similar(0.97)
        abort = "abort.png"
        xBtn = Pattern("xBtn.png").similar(0.92)
        self.tryClick(allianceIcon, 1)
        wait(2)
        self.tryClick(donations, 1)
        wait(5)
        self.tryClick(star, 1)
        wait(2)
        backupCounter = 0
        while not exists(stopDonate, 0.5) and backupCounter <27:
            self.tryClick(donateBtn, 1)
            backupCounter +=1
        self.tryClick(xBtn, 1)
        wait(1)
        self.tryClick(xBtn, 1)
        wait(1)
        self.tryClick(xIcon, 1)
        wait(1)
        self.tryClick(xIcon, 1)
        wait(1)
        

    def doc(self):        
        greenCollect="1545382999591.png"
        if self.findOverview("ovDoc.png"):
            if self.tryClick(greenCollect, 5):
                writeLog(debug, self.number, "Doc delivery collected")
                wait(7)
        else:
            writeLog(debug, self.number, "No doc delivery available")


    def tribute(self):  
        collect = "collect.png"
        if self.findOverview("gift"):
            if self.tryClick(collect, 5):   
                wait(7)
                writeLog(debug, self.number, "Tribute collected")
        else:
            writeLog(debug, self.number, "No tribute available")
 

    def spiritMines(self):        
        blueYes = "blueYes.png"
        redYes = "redYes.png"
        miningArea = Pattern("miningArea.png").similar(0.60)
        exitBtn = "exitBtn.png"
        stepOut = "stepOut.png"
        emptyMine = Pattern("emptyMine.png").similar(0.90)
        minesOccupy = "minesOccupy.png"        
        if not exists(Pattern("1546086058601.png").similar(0.84), 10):
            self.miningLoot()
            wait(4)
            self.tryClick("1546084467085.png", 1)
            if self.tryClick("1546086423732.png", 1):
                self.tryClick(blueYes, 5) 
                wait(5)
            tryClicks(miningArea, 5,2)
            self.tryClick(redYes, 5)
            wait(7)            
            self.tryClick(emptyMine, 1)
            wait(3)
            self.tryClick(minesOccupy, 1)
            wait(5)
            if self.sendTroops():
                writeLog(debug, self.number, "Gathering crystals")
            wait(1)
            self.tryClick(exitBtn, 1)
            wait(1)
            self.tryClick(stepOut, 1)
            wait(4)
            self.tryClick(kingdom, 1)
            wait(2)
            self.tryClick(estate, 1)
            wait(2)        
        

    def miningLoot(self):
        redeem = "redeem.png"
        reference = Pattern("reference.png").similar(0.75).targetOffset(-42,335)
        refA = Pattern("refB.png").targetOffset(-40,348)
        refB = Pattern("refB.png").similar(0.74).targetOffset(-41,121)
        increment = "increment.png"
        notAvailable = Pattern("notAvailable.png").similar(0.75)
        purchase = Pattern("purchase.png").similar(0.85).targetOffset(6,157)
        backIcon = "backIcon.png"        
        items = []

        try:
            print(self.settings["loot"])
            for item in self.settings["loot"]:
                items.append(Pattern("images\\"+ item +".png").similar(0.80).targetOffset(75,15))   
        except:
            items = [
                Pattern("images\\spiritFood.png").similar(0.80).targetOffset(72,17), 
                Pattern("images\\spiritWood.png").similar(0.80).targetOffset(72,17)]        
        if self.tryClick(redeem, 15):
            wait(2)
            for abc in range(25):     
                x = len(items) -1                
                while x >=0:
                    if self.tryClick(items[x], 1):
                        if exists(notAvailable):
                            self.tryClick(xIcon, 1)
                        else:
                            if not self.swipe(Pattern("1549656503851.png").similar(0.91), Pattern("1549656515423.png").similar(0.92)):
                                items = []
                                break
                            self.tryClick(purchase, 1)
                            wait(5)                        
                        items.pop(x)
                        wait(1)
                    x-=1
                self.swipe(refA, refB)                
                wait(1)
                if len(items) == 0:
                    break                
            self.tryClick(backIcon, 1)
            wait(1)
            self.tryClick(backIcon, 1)
        else:
            writeLog(debug, self.number, "Cannot click redeem")


    def swipe(self, refA, refB):
        try:
            dragDrop(refA, refB)
            return True
        except:
            return False
            
        
    def train(self, troop):          
        insideBuildRef = Pattern("insideBuildRef.png").similar(0.65).targetOffset(-175,419)
        minTierSelected = Pattern("minTierSelected.png").similar(0.85)
        trainIcon = Pattern("trainIcon.png").similar(0.62)
        troopsTraining = Pattern("troopsTraining.png").similar(0.74)
        center = Pattern("center.png").targetOffset(282,184)
        trainBtn = Pattern("1543350408501.png").similar(0.96)
        if self.findOverview(troop):                
            wait(5)
            if not exists(trainIcon, 2):
                self.tryClick(center, 1)
                wait(2)
            if self.tryClick(trainIcon, 2):
                wait(2)
                if exists(troopsTraining):
                    wait (2)
                    self.tryClick(xIcon, 1)                
                if self.settings["trainMinLevel"] and exists(insideBuildRef, 2):
                    i = 0
                    while not exists(minTierSelected, 1):
                        self.tryClick(insideBuildRef, 0.5)
                        
                        if i>12:
                            break
                        i += 1                    
                if self.tryClick(trainBtn, 4):
                    if not exists("1559069415235.png", 5):
                        writeLog(debug, self.number, "Training " + troop)
                        wait(3)
                        self.tryClick(xIcon, 2)
                    else:
                        if self.openFood():
                            self.train(troop)


    def tryClick(self, pattern, period):
        if exists(pattern, period):
            setFindFailedResponse(SKIP)
            click(pattern)
            setFindFailedResponse(ABORT)
            return True

    
    def center(self, pattern):
        try:
            wait(0.5)
            if exists(pattern, 1):
                dragDrop(pattern, Pattern("1543427171194.png").similar(0.80).targetOffset(290,162))
            return True
        except:
            return False


    def findOverview(self, item):
        ovBarracks = Pattern("ovBarracks.png").similar(0.80).targetOffset(200,0)
        ovStables = Pattern("ovStables.png").similar(0.80).targetOffset(197,0)
        ovArtillery = Pattern("ovArtillery.png").similar(0.80).targetOffset(195,0)
        ovShooting = Pattern("ovShooting.png").similar(0.80).targetOffset(200,0)
        ovSpirit = Pattern("ovSpirit.png").similar(0.81).targetOffset(194,0)
        ovGift = Pattern("ovGift.png").similar(0.80).targetOffset(200,0)
        ovDoc = Pattern("ovDoc.png").similar(0.80).targetOffset(200,0)
        image = ovDoc
        try:
            image = Pattern("images\\"+item).similar(0.80).targetOffset(200,0)
        except:
            pass
        if item == "barracks" or item == "inf":
            image = ovBarracks
        elif item == "stables" or item == "cav":
            image = ovStables
        elif item == "artillery" or item == "art":
            image = ovArtillery
        elif item == "shooting" or item == "dist":
            image = ovShooting
        elif item == "spirit":
            image = ovSpirit
        elif item == "gift":
            image = ovGift
        elif item == "doc":
            image = ovDoc        
        expandOverview = Pattern("expandOverview.png").similar(0.80)  
        collapseOverview = Pattern("collapseOverview.png").similar(0.80)
        if self.tryClick(expandOverview, 5):
            scrolls = 6
            wait(Pattern("1557431003983.png").similar(0.80).targetOffset(0,180),10)
            while scrolls>0:
                if not self.tryClick(image, 0.5):
                    self.swipe(Pattern("1557431003983.png").similar(0.80).targetOffset(0,180), Pattern("1557431003983.png").similar(0.80).targetOffset(0,10))
                    scrolls-=1
                    wait(0.5)
                else:
                    scrolls=0
                    wait(1.5)
                    if exists(Pattern("1557431003983.png").similar(0.80).targetOffset(0,10),0.5):
                        writeLog(debug, self.number, "Unable to click " + str(image))
                    else:    
                        return True
        else:
            if self.recover():
                self.findOverview(item)
        self.tryClick(collapseOverview, 2) 
        return False  


    def wall(self):
        burning = Pattern("burning.png").similar(0.66)
        wallDamaged = Pattern("wallDamaged.png").similar(0.60)
        underAttack = Pattern("underAttack.png").similar(0.71)
        boolAttack = exists(underAttack, 3)
        extinguish = "extinguish.png"
        repairWall = "repairWall.png"
        self.navigate([2, 2, 2, 2, 4, 4, 4, 4, 4])

        if self.tryClick(wallDamaged, 2):
            wait(2)

            if not boolAttack:
                self.tryClick(extinguish, 2)
                writeLog(debug, self.number, "Extinguising fire")

            if self.tryClick(repairWall, 2):
                writeLog(debug, self.number, "Repairing wall")
                
            wait(0.5)
            self.tryClick(xIcon, 2)


    def navigate(self, moves):
        self.findTopLeft()
        for move in moves:
            self.move(move)


    def upgrade(self):
        tipsBtn = Pattern("tipsBtn.png").similar(0.76)
        tipsIcon= Pattern("tipsIcon.png").similar(0.77)
        upgradeIcon = Pattern("upgradeIcon.png").similar(0.58)
        helpIcon = Pattern("helpIcon.png").similar(0.61)
        speedUp = Pattern("speedUp.png").similar(0.60)
        upgradeBtn = Pattern("upgradeBtn.png").exact()
        goTo = Pattern("goTo.png").similar(0.68)
        wait(1)

        if self.tryClick(tipsIcon, 1):
            wait(3)
            self.tryClick(tipsBtn, 2)
            wait(2)

        hover(Pattern("1543427171194.png").similar(0.80).targetOffset(283,208))
        wait(1)
        mouseDown(Button.LEFT)
        mouseUp()
        wait(1)  
            
        if not exists(upgradeIcon) and not exists(speedUp):
            writeLog(debug, self.number, "clicking again in center")
            hover(Pattern("1543427171194.png").similar(0.80).targetOffset(283,208))
            wait(1)
            mouseDown(Button.LEFT)
            mouseUp()
            wait(1)  

            if not exists(upgradeIcon) and not exists(speedUp):
                writeLog(debug, self.number, "clicking again in center")
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
                        writeLog(debug, self.number, "Building upgraded")
                wait(1)
                self.tryClick(xIcon, 1)
                wait(1)
                self.tryClick(xIcon, 1)
                writeLog(debug, self.number, "Not enough resources to upgrade")
                
        else:
           if exists(speedUp):
               writeLog(debug, self.number, "Upgrade already in progress")
               self.tryBuild = False
            #if upgrade icon not available#
             
        
    def openGoldChest(self):
        goldChest = Pattern("goldChest.png").similar(0.89)
        openBtn = Pattern("openBtn.png").similar(0.75)
        if self.tryClick(goldChest, 5):
            wait(5)
            writeLog(debug, self.number, "Found gold chest")
            while self.tryClick(openBtn, 2):              
                wait(3)  
            wait(1)
            writeLog(debug, self.number, "Opened all chests")
            self.tryClick(xIcon, 2)
            wait(2)
            self.tryClick(xIcon, 2)


    def allianceGather(self):
        center = Pattern("center.png").similar(0.63).targetOffset(306,248)
        alliance = "alliance.png"
        territory = "territory.png"
        alliResources = "alliResources.png"
        gathering = Pattern("gathering.png").similar(0.59).targetOffset(-3,55)
        bookmark = "bookmark.png"
        callBack = "callBack.png"
        gather = "gather.png"
        
        if self.tryClick(alliance, 1):
            if self.tryClick(territory, 5):
                self.tryClick(alliResources, 5)
                self.tryClick(gathering, 5)
                wait(12)
                self.tryClick(center,1)
                wait(4)
                if not exists(callBack,1) and not exists(gather,1): 
                    self.tryClick(center,1)
                    wait(2)
                if exists(callBack, 1):
                    writeLog(debug, self.number, "Already gathering alliance mine")
                elif self.tryClick(gather, 2):
                    wait(4)    
                    if self.sendTroops():
                        writeLog(debug, self.number, "Gathering alliance mine")
                        wait(3)   
            
            self.tryClick(xIcon, 1)
            wait(2)
            self.tryClick(estate, 1)
            wait(1)


    def sendTroops(self):
        equalizeBtn = Pattern("equalizeBtn.png").similar(0.80)
        marchBtn = Pattern("marchBtn.png").similar(0.60).targetOffset(-1,13)
        equalize = True
        try:
            equalize = self.settings["equalize"] 
        except:
            equalize = True
        if equalize:
            self.tryClick(equalizeBtn, 1)
            wait(1)
        return self.tryClick(marchBtn, 8)
    

    def openFood(self):
        items = "items.png"
        resources = "resources.png"
        foodItem = "foodItem.png"
        useBtn = "useBtn.png"
        bigUseBtn = "bigUseBtn.png"
        
        if self.tryClick(xIcon, 2):
            wait(1)
            self.tryClick(xIcon, 2)
        if self.tryClick(items, 2):
            self.tryClick(resources, 5)
            self.tryClick(foodItem, 5)
            if self.tryClick(useBtn, 5):
                if self.tryClick(bigUseBtn, 5):
                    wait(1)
                    self.tryClick(xIcon, 2)
                    wait(2)
                    return True        
        if self.tryClick(xIcon, 2):
            wait(2)
            self.tryClick(xIcon, 2)
            wait(2)
        writeLog(debug, self.number, "Failed to open Food item")
        return False
    

    def gather(self, resources):
        resourceBusy = Pattern("resourceBusy.png").similar(0.68)
        marchFull = Pattern("marchFull.png").similar(0.68)
        occupy = "occupy.png"
        maxSteps = 8
        dir1 = self.settings["gatherDir"][0]
        dir2 = self.settings["gatherDir"][1]
        if not self.tryClick(kingdom, 1):
            self.tryClick(kingdom, 2)
        wait(10)    
        steps = 1
        marches = self.getAvailableMarch()
        if marches > 0:
            writeLog(debug, self.number, str(marches) + " marches available, gathering " + str(self.settings["gatherRess"]))
        else: 
            writeLog(debug, self.number, "No available marches")                     
            
        while steps < maxSteps*maxSteps and marches > 0:
            if steps % maxSteps == 0:
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
                if exists(resource, 0.5):
                    self.center(resource)
                    self.tryClick(resource, 1)
                    if not exists(resourceBusy, 1) and not exists(occupy, 1):
                        self.tryClick(resource, 2)
                    
                    if exists(occupy, 1):
                        if self.tryClick(occupy, 1):
                            
                            wait(2)
                            if exists(marchFull):
                                marches = 0
                                wait(2)
                                
                                self.tryClick(xIcon, 1)
                                wait(1)
                            if not self.sendTroops():
                                self.tryClick(xIcon, 1)
                                marches = 0
                            else:
                                marches -= 1
                                writeLog(debug, self.number, "Found " + str(resource))
                                wait(2)
                                self.move(dir1)
                                self.move(dir1)
                                break
                                
                                
                    elif exists(resourceBusy) or exists(callBack):
                        self.move(dir1)
                        self.move(dir1)
        self.tryClick(estate, 2)     
                

    def move(self, direction, distance = 240):
        delay = 0.6
        #1 up, 2 down, 3 left, 4, right
        try:
            center = Pattern("1543427171194.png").similar(0.80).targetOffset(288,211)
            
            hover(center)
            mouseDown(Button.LEFT)
            wait(delay)
            if direction == 1:
                hover(Pattern("1543427171194.png").similar(0.80).targetOffset(290,211+distance))
            elif direction == 2:
                hover(Pattern("1543427171194.png").similar(0.80).targetOffset(290,211-distance))
            elif direction == 3:
                hover(Pattern("1543427171194.png").similar(0.80).targetOffset(290+distance,211))
            elif direction == 4:
                hover(Pattern("1543427171194.png").similar(0.80).targetOffset(290-distance,211))

            mouseUp()
        except:
            self.tryClick(xIcon, 1)


    def findCastle(self):
        castle = Pattern("castle.png").similar(0.43)
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


    def munitionExchange(self, ress):
        gunsIcon = "gunsIcon.png"
        helpAllies = Pattern("helpAllies.png").similar(0.72)
        freeWeapons = "1545083917425.png"
        wait(2)
        self.findTopLeft()
        self.move(2)
        self.move(2)
        self.move(2)
        self.move(4)
        self.move(4)
        if self.tryClick(gunsIcon, 2):
            writeLog(debug, self.number, "Found munition exchange")
            wait(4)
            x=0
            while exists(freeWeapons) and x < 12:
                self.tryClick(ress, 1)
                x+=1
                wait(2)
            self.tryClick(xIcon, 1)
        else:
            writeLog(debug, self.number, "No free weapons")
        if self.tryClick(helpAllies, 2):
            writeLog(debug, self.number, "Helped allies")
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

    
    def perfAction(self, action):
            munitionFood = Pattern("munitionFood.png").targetOffset(235,3)
            wait(3)
            if action == "train":
                for troop in self.settings["troopsToTrain"]:                    
                    self.train(troop)
            elif action == "gather":                
                test = []
                for ress in self.settings["gatherRess"]:
                    if not ress == None:
                        test.append(stringToPattern(ress))
                self.gather(test)
            elif action == "upgrade":
                writeLog(debug, self.number, "Upgrading")
                self.findCastle()
                self.upgrade()
            elif action == "gold":
                self.openGoldChest()   
            elif action == "munition":
                self.munitionExchange(munitionFood)
            elif action == "doc":
                self.doc()
            elif action == "tribute":
                self.tribute()
            elif action == "spirit":
                if self.findOverview("spirit"):
                    writeLog(debug, self.number, "Can gather crystal")
                    self.spiritMines()
                else:
                    writeLog(debug, self.number, "Gathering crystals already")
            elif action == "donate":
                self.donate()
            elif action == "allianceGather":
                self.allianceGather()
            elif action == "wall":
                self.wall()


    def recover(self):
        writeLog(debug, self.number, "Attempting recovery")
        wait(1)
        succes = False
        if self.tryClick(xIcon, 1):
            success = True
        wait(1)
        if self.tryClick(estate, 1):
            success = True
        wait(1)
        return succes

    
    def getAvailableMarch(self):
        x=0
        self.tryClick(Pattern("1550403558215.png").similar(0.55), 2)
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
    tryClicks("1544032444964.png", 1, 2)
    hover(Pattern("1544032444964.png").targetOffset(0,instance*50)) 
     
    mouseDown(Button.LEFT)
    mouseUp()  
    if tryClick("1543346082405.png", 150):
        writeLog(debug, counter, "Starting farm")
    wait(xIcon, 150)


def tryClick(pattern, time):
    if exists(pattern, time):
        try:
            click(pattern)
            return True
        except:
            pass
    return False


def tryClicks(pattern, time, repeats):
    i = repeats
    while not tryClick(pattern, time) and i>0:
        i-=1


def closeEmu():
    if not error == "":
            writeLog(debug, counter, error)
    closeBtn = "closeBtn.png"
    operation = "operations.png"
    messagePopup = Pattern("1544174098594.png").targetOffset(82,1)
    tryClick(messagePopup, 1)
    global counter
    tryClicks(operation, 1, 3)
    tryClicks(closeBtn, 1, 2)
    while exists(closeBtn, 0.5): 
        wait(0.2)
    if counter<maxInstance:
        counter+=1
    else:        
        counter = minInstance
        writeLog(debug, counter, ".")
        writeLog(debug, counter, ".")


def stringToPattern(text):
    farm = Pattern("farm.png").similar(0.68)
    lumberyard = Pattern("lumberyard.png").similar(0.68)
    ironMine = Pattern("ironMine.png").similar(0.65)
    silverMine = Pattern("silverMine.png").similar(0.65)
    switcher = {
        "lumberyard":lumberyard,
        "farm":farm,
        "ironMine":ironMine,
        "wood":lumberyard,
        "food":farm,
        "iron":ironMine,
        "silver":silverMine,
        }
    return switcher.get(text, None)

def getLength(image):
    x=0
    try:
        
        mm =  findAll(image)
        while mm.hasNext():
            mm.next()
            #finding existing patterns
            x+=1
    except:
        pass
    return x


if debug:    
    instance = Farm(counter)
    #launchEmu(3)
    #instance.perfAction("gold")
    instance.miningLoot()

while not debug:
    try:
        error = "------Unhandled exception------"
        launchEmu(counter)
        instance = Farm(counter)
        instance.start()
        for action in instance.settings["actions"]:
            instance.perfAction(action)
        error = ""
        closeEmu()
        writeLog(debug, instance.number, ".")
    except FindFailed, e:
        error = str(e)
        closeEmu()
    except:
        closeEmu()

    
