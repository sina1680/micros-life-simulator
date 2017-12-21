import os
import time
from random import randint
import threading
import uuid
from os.path import expanduser

# World Status
Hours=0
Minutes=0
Seconds=0
Day=1
Mounth=1
Year=0
Population=randint(0,100)
#==========================

#World Settings
timeSpeed=0.0001
MaxYearsLife=110
MinYearsLife=2
#==========================

MaleNames=["Alexandre","Andre","Carlos","Miguel","Joao","Pedro","Diogo","Jose","Jorge","Fabio","Filipe"]
FemaleNames=["Ana","Mariana","Sofia","Carolina","Susana","Sonia","Adriana","Mara","Marta","Cassandra","Maria"]

def micLife():
	lastSecond=-0
	lastYear=-1
	time.sleep(randint(0,1000))
	# Creation ===============================================
	money=0
	work=""
	digitalID=str(uuid.uuid4())
	myBody=digitalID+".micro"
	currentPath=home = expanduser("~")+"/MicroVile"
	home=""
	life=randint(MinYearsLife,MaxYearsLife)
	age=0
	energy=randint(10,100)
	eat=randint(0,100)
	studyLevel=0
	birthday=str(Day)+"/"+str(Mounth)+"/"+str(Year)
	
	# 0 - Alive
	# 1 - Sleep
	# 2 - Dead
	currentLifeState=0

	# 0 - Male
	# 1 - Female
	sex=(randint(0,1))
	if sex==0:
		name=MaleNames[randint(0,len(MaleNames)-1)]
	else:
		name=FemaleNames[randint(0,len(FemaleNames)-1)]
	print(name+" nasceu!")
	
	f=open(currentPath+"/"+digitalID+".micro","w")
	f.write(name+"\n"+digitalID+"\n"+str(age)+"\n"+str(sex)+"\n"+work+"\n"+home)
	f.close()
	#===================================================================

	while(currentLifeState!=2):
		if life==0:
			currentLifeState=2
			os.remove(currentPath+"/"+myBody)
			print(name+" Morreu!")
			break
		if lastSecond!=Seconds:
			lastSecond=Seconds
			energy=energy-1
			if energy<1:
				currentLifeState=1
			if currentLifeState==1:
				energy=energy+1
				if energy>99:
					currentLifeState=0
		if lastYear!=Year:
			lastYear=Year
			life=life-1
			
			
	
for i in range(0,randint(1,Population)):
	mic = threading.Thread(target=micLife)
	mic.start()

while(True):
	#os.system("clear")
	# TIME
	Seconds=Seconds+1
	if Seconds>59:
		Seconds=0
		Minutes=Minutes+1
	if Minutes>59:
		Seconds=0
		Minutes=0
		Hours=Hours+1
	if Hours>23:
		Seconds=0
		Minutes=0
		Hours=0
		Day=Day+1
	if Day>31:
		Second=0
		Minutes=0
		Hours=0
		Day=0
		Mounth=Mounth+1
	if Mounth>12:
		Seconds=0
		Minutes=0
		Hours=0
		Day=0
		Mounth=1
		Year=Year+1
	
	#RENDER
	#print("TIME:"+str(Hours)+":"+str(Minutes)+":"+str(Seconds)+"    DATE:"+str(Day)+"/"+str(Mounth)+"/"+str(Year))
	time.sleep(timeSpeed)