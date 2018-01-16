import os
import time
from random import randint
import threading
import uuid
from os.path import expanduser

# World Status
Hours=0
Minutes=0
Day=1
Mounth=1
Year=0
Population=0
#==========================

#World Settings
timeSpeed=0.0001
MaxYearsLife=110
MinYearsLife=4
StartPopulation=randint(2,100)
CityName="MicroVile"
#==========================

STOP=False;

MaleNames=["Alexandre","Andre","Carlos","Miguel","Joao","Pedro","Diogo","Jose","Jorge","Fabio","Filipe"]
FemaleNames=["Ana","Mariana","Sofia","Carolina","Susana","Sonia","Adriana","Mara","Marta","Cassandra","Maria"]

def writeLog(text):
	f=open(expanduser("~")+"/log.txt","a+")
	f.write("TIME:"+str(Hours)+":"+str(Minutes)+":"+str(Minutes)+"    DATE:"+str(Day)+"/"+str(Mounth)+"/"+str(Year)+" | "+text+"\n")
	f.close()

def micLife():
	global Population
	deadMotif="";
	lastMinute=-0
	lastYear=-1
	Population=Population+1
	# Creation ===============================================
	money=0
	work=""
	digitalID=str(uuid.uuid4())
	myBody=digitalID+".micro"
	currentPath=expanduser("~")+"/"+CityName
	home=""
	life=randint(MinYearsLife,MaxYearsLife)
	age=0
	energy=randint(60,60*24)
	eat=randint(10,(60*24)*7)
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
	writeLog(name+" nasceu!")
	
	f=open(currentPath+"/"+digitalID+".micro","w")
	f.write(name+"\n"+digitalID+"\n"+str(age)+"\n"+str(sex)+"\n"+work+"\n"+home)
	f.close()
	#===================================================================

	while(currentLifeState!=2):
		if(STOP):
			break
		if life==0:
			# DEAD
			currentLifeState=2
			os.remove(currentPath+"/"+myBody)
			writeLog(name+" Morreu! MOTIVO:"+deadMotif)
			Population=Population-1
			break
		if lastMinute!=Minutes:
			lastMinute=Minutes
			if energy<1:
				currentLifeState=1
			if currentLifeState==1:
				energy=energy+1
				eat=eat-1;
				if energy>99:
					currentLifeState=0
			if currentLifeState==0:	
				lastMinute=Minutes
				energy=energy-1
				eat=eat-8;
		if lastYear!=Year:
			lastYear=Year
			life=life-1
		if(eat<1):
			life=0
			deadMotif="Fome"
			
			
writeLog("Inicio da simulacao")
print("Inicio da simulacao")
writeLog("A Criar Cidade")
print("A Criar Cidade")
cityPath=expanduser("~")+"/"+CityName
os.makedirs(cityPath)
for i in range(1,randint(1,500)):
	os.makedirs(cityPath+"/Home_"+str(i))
os.makedirs(cityPath+"/Farm")
os.makedirs(cityPath+"/cemetery")
os.makedirs(cityPath+"/hospital")
print("A criar Micros")
writeLog("A criar Micros")
for i in range(2,StartPopulation):
	mic = threading.Thread(target=micLife)
	mic.start()

while(True):
	os.system("clear")
	# TIME
	Minutes=Minutes+1
	if Minutes>59:
		Minutes=0
		Hours=Hours+1
	if Hours>23:
		Minutes=0
		Hours=0
		Day=Day+1
	if Day>31:
		Minutes=0
		Hours=0
		Day=0
		Mounth=Mounth+1
	if Mounth>12:
		Minutes=0
		Hours=0
		Day=0
		Mounth=1
		Year=Year+1
	
	#RENDER
	print("TIME:"+str(Hours)+":"+str(Minutes)+"    DATE:"+str(Day)+"/"+str(Mounth)+"/"+str(Year)+"   POPULATION:"+str(Population))
	time.sleep(timeSpeed)
	if(Population==0):
		writeLog("FIM da simulacao, Todos morreram")
		STOP=True
		break
		
