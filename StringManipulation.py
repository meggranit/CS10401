infoString="Meghan,Granit,blue,tiger,Hawks"
commaLocation= infoString.find(",")
infoStringLength= len(infoString)
firstName=infoString[0:commaLocation]
infoString=infoString[commaLocation+1:len(infoString)]
infoStringLength= len(infoString)
lastName=infoString[0:commaLocation]
infoString=infoString[commaLocation+1:len(infoString)]
infoStringLength= len(infoString)
favColor=infoString[0:commaLocation-1]
infoString=infoString[commaLocation-1:len(infoString)]
infoStringLength= len(infoString)
favAnimal=infoString[0:commaLocation]
infoString=infoString[commaLocation:len(infoString)]
favTeam=infoString
print("My name is "+ firstName+ " "+lastName+", my favorite color is "+favColor+" my favorite animal is a "+favAnimal+" and my favorite team is the "+favTeam)

