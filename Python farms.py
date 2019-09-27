from fileOperations import *

updateBool = False
debug = True
Settings.MoveMouseDelay = 0.8
counter = 1
minInstance = 1
maxInstance = 12
error = ""

xIcon = Pattern("xicon.png").similar(0.82)
kingdom = "kingdom.png"
estate = "estate.png"
callBack = Pattern("callBack.png").similar(0.65)

class Farm:
    def __init__(self, nb):
        self.number = nb
        self.settings = loadSettings(nb)
        

    def start(self):  
        
        shipment = Pattern("1543352147086.png").similar(0.90)
        fadedIconX = "fadedIconX.png"
        if self.tryClick(shipment, 3):
            wait(12)
        self.tryClick(xIcon, 1)
        wait(3)
        self.honorChallenge()
        self.curiosityCabinet()
        tryClicks(fadedIconX, 2, 3, 5)
        self.tryClick(xIcon, 1)
        wait(4)
        self.tryClick(kingdom, 1)
        wait(2)
        if not self.tryClick(estate, 15):
            self.tryClick(estate, 5)
        wait(2)
           
    def honorChallenge(self):
        #not yet implemented, just clicks to close the popup
        title = "title.png"
        go = "ok.png"
        if exists(title, 5):
            self.tryClick(title, 1)
            wait(5)
            
    def donate(self):
        donation_star = "donation_star.png"
        icon_alliance = "icon_alliance.png"
        
        alliance_donation = "alliance_donation.png"
        donation_btn = Pattern("donation_btn.png").targetOffset(1,39)
        
        self.tryClick(icon_alliance, 10)
        self.tryClick(alliance_donation, 10)
        self.tryClick(donation_star, 10)
        wait(3)
        for i in range(24):
            if self.tryClick(donation_btn, 0.5):
                wait(1)
            else:
                break
        self.tryClick(xIcon, 1)
        wait(1)
        self.tryClick(xIcon, 1)
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
        if self.findOverview("ovGift"):
            if self.tryClick(collect, 5):   
                wait(7)
                writeLog(debug, self.number, "Tribute collected")
        else:
            writeLog(debug, self.number, "No tribute available")
 

    def spiritMines(self):        
        blueYes = "blueYes.png"
        redYes = "redYes.png"
        miningArea = Pattern("miningArea.png").similar(0.65)
        exitBtn = "exitBtn.png"
        stepOut = "stepOut.png"
        emptyMine = Pattern("emptyMine.png").similar(0.90)
        minesOccupy = "minesOccupy.png"        
        if not exists(Pattern("1546086058601.png").similar(0.84), 1):
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
        minTierSelected = Pattern("minTierSelected.png").similar(0.85)
        trainIcon = Pattern("trainIcon.png").similar(0.60)
        troopsTraining = Pattern("troopsTraining.png").similar(0.74)
        center = Pattern("center.png").targetOffset(229,217)
        trainBtn = "trainBtn.png"
        insideBuildRef = Pattern("trainBtn.png").targetOffset(-468,129)
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
                if self.settings["trainMinLevel"] and exists(trainBtn, 1):
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
        center = Pattern("center.png").similar(0.63).targetOffset(230,258)
        try:
            wait(0.5)
            if exists(pattern, 1):
                dragDrop(pattern, center)
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
        ovExchange = Pattern("ovExchange.png").similar(0.80).targetOffset(200,0)
        ovRecruit = Pattern("ovRecruit.png").similar(0.80).targetOffset(200,0)
        ovAcademy = Pattern("ovAcademy.png").similar(0.80).targetOffset(200,0)
        ovDaily = Pattern("ovDaily.png").similar(0.80).targetOffset(200,0)
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
        expandOverview = "expandOverview.png"
        collapseOverview = "collapseOverview.png"
        if self.tryClick(expandOverview, 5):
            for i in range(3):
                self.swipe(Pattern("1557431003983.png").similar(0.80).targetOffset(0,25),Pattern("1557431003983.png").similar(0.80).targetOffset(0,180))
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
        burning = "burning.png"
        wallDamaged = Pattern("wallDamaged.png").similar(0.63)
        underAttack = Pattern("underAttack.png").similar(0.71)
        
        extinguish = "extinguish.png"
        repairWall = "repairWall.png"
        self.navigate([2, 2, 2, 4, 4, 4, 4])
        boolAttack = exists(underAttack, 3)
        if self.tryClick(wallDamaged, 2):
            wait(2)

            if not boolAttack:
                self.tryClick(extinguish, 2)

            if self.tryClick(repairWall, 2):
                writeLog(debug, self.number, "Repairing wall")
                
            wait(0.5)
            self.tryClick(xIcon, 2)


    def navigate(self, moves):
        self.findTopLeft()
        for move in moves:
            self.move(move)


    def upgrade(self):
        center = Pattern("center.png").similar(0.63).targetOffset(245,206)
        tipsBtn = Pattern("tipsBtn.png").similar(0.76)
        getMore = "getMore.png"
        tipsIcon= Pattern("tipsIcon.png").similar(0.77)
        upgradeIcon = Pattern("upgradeIcon.png").similar(0.65)
        helpIcon = "helpIcon.png"
        speedUp = Pattern("speedUp.png").similar(0.65)
        upgradeBtn = Pattern("upgradeBtn.png").exact()
        goTo = Pattern("goTo.png").similar(0.68)
        wait(1)

        if self.tryClick(tipsIcon, 1):
            wait(3)
            self.tryClick(tipsBtn, 2)
            wait(2)

        hover(center)
        wait(1)
        mouseDown(Button.LEFT)
        mouseUp()
        wait(1)  
            
        if not exists(upgradeIcon) and not exists(speedUp):
            writeLog(debug, self.number, "clicking again in center")
            hover(center)
            wait(1)
            mouseDown(Button.LEFT)
            mouseUp()
            wait(1)  

            if not exists(upgradeIcon) and not exists(speedUp):
                writeLog(debug, self.number, "clicking again in center")
                hover(center)
                wait(1)
                mouseDown(Button.LEFT)
                mouseUp()
                wait(1) 
            
        if self.tryClick(upgradeIcon, 2):
            wait(2)
            if self.tryClick(goTo, 1):
                wait(2)
                self.tryClick(goTo, 1)
            
            while self.tryClick(getMore, 5):                
                if not self.openResource(5):
                    break;
                
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
        goldChest = "goldChest.png"
        openBtn = Pattern("openBtn.png").similar(0.75)
        if self.tryClick(goldChest, 5):
            wait(5)
            writeLog(debug, self.number, "Found gold chest")
            counter = 0
            while self.tryClick(openBtn, 2) and counter < 10:              
                wait(3) 
                mouseDown(Button.LEFT)
                wait(0.1)
                mouseUp()
                counter = counter + 1
            wait(1)
            writeLog(debug, self.number, "Opened all chests")
            self.tryClick(xIcon, 2)
            wait(2)
            self.tryClick(xIcon, 2)


    def allianceGather(self):
        center = Pattern("center.png").similar(0.63).targetOffset(230,258)
        alliance = "alliance.png"
        territory = "territory.png"
        alliResources = "alliResources.png"
        gathering = Pattern("gathering.png").similar(0.59).targetOffset(-3,55)
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
    
    def openResource(self, count):
        backIcon = "backIcon.png"  
        largeItem = Pattern("largeItem.png").similar(0.82).targetOffset(264,-9)
        useBtnResource = Pattern("useBtnResource.png").targetOffset(-21,-3)
        useSingleResource = "useSingleResource.png"
        increment = Pattern("1568661593896.png").similar(0.94)
        if not exists(largeItem, 3):
            if self.tryClick(useBtnResource, 3):
                self.swipe(Pattern("1568735495777.png").similar(0.65).targetOffset(0,-2), increment)
                self.tryClick(useSingleResource, 1)
                return self.openResource(count)
            else:
                self.tryClick(backIcon, 1)
                return False                
        else:
            if self.tryClick(largeItem, 1):
                for i in range(count):
                    self.tryClick(increment, 0.3)
                self.tryClick(useSingleResource, 1)
                self.tryClick(backIcon, 1)
                return True
            
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
            center = Pattern("center.png").targetOffset(219,224)
            
            hover(center)
            mouseDown(Button.LEFT)
            wait(delay)
            if direction == 1:
                hover(Pattern("center.png").similar(0.80).targetOffset(219,224+distance))
            elif direction == 2:
                hover(Pattern("center.png").similar(0.80).targetOffset(219,224-distance))
            elif direction == 3:
                hover(Pattern("center.png").similar(0.80).targetOffset(219+distance,224))
            elif direction == 4:
                hover(Pattern("center.png").similar(0.80).targetOffset(219-distance,224))

            mouseUp()
        except:
            self.tryClick(xIcon, 1)


    def findCastle(self):
        castle = Pattern("castle.png").similar(0.61)
        wait(2)
        self.navigate([2, 4])
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
                if self.findOverview("ovSpirit"):
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

    def curiosityCabinet(self):
        msg_cabinet_curiosity = "msg_cabinet_curiosity.png"
        cur_building = Pattern("cur_building.png").similar(0.60)
        if self.tryClick(msg_cabinet_curiosity, 2):
            self.tryClick(cur_building, 6)
            self.tryClick(xIcon, 8)
            return True
        else:
            return False

        
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
        march_moving = "march_moving.png"
        march_stationary = Pattern("march_stationary.png").similar(0.60)
        march_extend = Pattern("march_extend.png").similar(0.59)
        x=0
        self.tryClick(march_extend, 2)
        try:
            mm =  findAll(march_moving)
            while mm.hasNext():
                mm.next()
                #finding troops on the move
                x+=1
        except:
            pass
        try:
            nn = findAll(march_stationary) 
            while nn.hasNext(): # loop as long there is a first and more matches
                #finding troops gathering
                nn.next()
                x+=1
        except:
            pass            
        return self.settings["availableMarch"]-x                   

def updateGame():
    upd_play_store = "upd_play_store.png"
    upd_no = "upd_no.png"
    upd_menu = "upd_menu.png"
    upd_my_apps = "upd_my_apps.png"
    upd_update_all = "upd_update_all.png"
    upd_home_screen = "upd_home_screen.png"
    images = [upd_no, upd_menu, upd_my_apps, upd_update_all, upd_home_screen]
    
    if updateBool:
        tryClick(upd_play_store, 150)
        wait(10)
        for image in images:
            tryClick(image, 5)
        wait(120)
                        
def launchEmu(instance):
    
    tryClicks("1544032444964.png", 1, 2)
    hover(Pattern("1544032444964.png").targetOffset(0,instance*50)) 
     
    mouseDown(Button.LEFT)
    mouseUp()  
    updateGame()    
    if tryClick("1543346082405.png", 150):
        writeLog(debug, counter, "Starting farm")
    wait(xIcon, 250)


def tryClick(pattern, time = 1):
    if exists(pattern, time):
        try:
            click(pattern)
            return True
        except:
            pass
    return False


def tryClicks(pattern, time, repeats, pause = 0):
    i = repeats
    while not tryClick(pattern, time) and i>0:
        i-=1
        wait(pause)


def closeEmu():
    global counter
    if not error == "":
            writeLog(debug, counter, error)
    closeBtn = "closeBtn.png"
    operation = "operations.png"
    messagePopup = Pattern("1544174098594.png").targetOffset(82,1)
    tryClick(messagePopup, 1)
    
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
    farm = Pattern("farm.png").similar(0.63)
    lumberyard = Pattern("lumberyard.png").similar(0.65)
    ironMine = Pattern("ironMine.png").similar(0.64)
    silverMine = Pattern("silverMine.png").similar(0.64)
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
    instance.perfAction("donate")

    #instance.findTopLeft()
    #launchEmu(3)
    #instance.perfAction("gold")
    #instance.miningLoot()
    #writeLog(debug, counter, str(instance.settings))

while not debug:
    try:
        error = "------Unhandled exception------"
        launchEmu(counter)
        instance = Farm(counter)
        if not updateBool:
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

    
