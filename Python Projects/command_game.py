def getinput():
    """
    Accepts input from user and performs appropiate function calls according to command header
    """
    command=input(": ")
    if command=="RunAway...":
        exit()
    elif command=="LookAround...":
        lookaround()
        return
    command=command.split()
    verb=command[0]
    if verb in command_list:
        func=command_list[verb]
    else:
        print("Unknown Command {}".format(verb))
        return
    if len(command)>=2:
        func(command)
    else:
        print("...No Command Line Arguments...")

def say(words):
    """
    returns a string consisting of all the words after the command "say"
    """
    string=""
    for word in range(1,len(words)):
        string=string+words[word]+' '
    print(string,'\n')

def add(numbers):
    """
    returns the additon of all the numbers after the command "add"
    """
    sum_=0.0
    for i in range(1,len(numbers)):
        sum_+=int(numbers[i])
    print("Addition: "+str(sum_)+'\n')

def examine(mons):
    """
    Gets the name and description of the creature mentioned after the command "examine"
    """
    for i in range(1,len(mons)):
        if mons[i] in creature.monsters:
            print(creature.monsters[mons[i]].getdesc())
        else:
            print("No description available for {}".format(mons[i]))

def hit(mons):
    """
    Reduces the hitpoints count by 1 for the monster mentioned after the command "hit"
    """
    for i in range(1,len(mons)):
        if mons[i] in creature.monsters:
            mon=creature.monsters[mons[i]]
            mon.health-=1
            print("**HIT**")
            if mon.health<=0:
                msg="The {} is dead".format(mon.type_name)
            else:
                msg="{} health:: {}".format(mon.type_name,mon.health)
            print(msg)
        else:
            print("No {} in sight...".format(mons[i]))
    print()

def lookaround():
    """
    Displays the list of prevailing monsters and health conditions when the command "LookAround..." is entered
    """
    string="Monsters sighted::\n"
    for mon in creature.monsters:
        string+=creature.monsters[mon].type_name+"\tMax_Health: "+str(creature.monsters[mon].max_health)
        if creature.monsters[mon].health==creature.monsters[mon].max_health:
            string+="\tNo Previous Encounter\n"
        else:
            string+="\tCurrent Health:: "+str(creature.monsters[mon].health)+'\n'
    print(string)

#Creature Definitions
class creature:
    type_name=""
    description=""
    monsters={}
    def __init__(self):
        creature.monsters[self.type_name]=self
    def getdesc(self):
        return self.type_name+':\n'+self.description+'\n'
    @property
    def description(self):
        if self.health/self.max_health==1:
            return "No description avaible yet\nNo previous encounters..."
        elif self.health/self.max_health>0.8:
            health_line="\nHealthy"
        elif self.health/self.max_health>0.5:
            health_line="\nInjured"
        elif self.health/self.max_health>0.2:
            health_line="\nGravely Injured"
        else:
            health_line="\nThe {} is Dead".format(self.type_name)
        return self._desc + health_line

#Creatures in the game
class Goblin(creature):
    type_name="Goblin"
    _desc="Green in color, Gold hungry drawf monsters"
    max_health,health=3,3
goblin=Goblin()

class Bigfoot(creature):
    type_name="Bigfoot"
    _desc="Furry, man-sized creature leaving behind large footprints"
    max_health,health=9,9
bigfoot=Bigfoot()

class Vampire(creature):
    type_name="Vampire"
    _desc="Creature that subsists by feeding on the vital essence (Blood) of the living"
    max_health,health=7,7
vampire=Vampire()

#Add More Monsters Here...

#List of Functions available for execution
command_list={"say":say,"add":add,"examine":examine,"hit":hit}

#Driver Code
while True:
    getinput()
