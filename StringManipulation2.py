infoString="Granit,Meghan,blue,tiger,hawks"
commaLocation= infoString.find(",")
infoStringLength= len(infoString)
lastName=infoString[0:commaLocation]

infoString=infoString[commaLocation+1:len(infoString)]
infoStringLength= len(infoString)
commaLocation= infoString.find(",")
firstName=infoString[0:commaLocation]

infoString=infoString[commaLocation+1:len(infoString)]
infoStringLength= len(infoString)
commaLocation= infoString.find(",")
favColor=infoString[0:commaLocation]

infoString=infoString[commaLocation+1:len(infoString)]
infoStringLength= len(infoString)
commaLocation= infoString.find(",")
favAnimal=infoString[0:commaLocation]

infoString=infoString[commaLocation+1:len(infoString)]
favTeam=infoString
favTeam=favTeam.capitalize()

print("My name is "+ firstName+ " "+lastName+", my favorite color is "+favColor+", my favorite animal is a "+favAnimal+", and my favorite team is the "+favTeam)

