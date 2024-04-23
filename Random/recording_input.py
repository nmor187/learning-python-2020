file = raw_input("Where would you like to save this data? ")
input = raw_input("What data do you wish to add? ")

saveFile = open(file,"a")
saveFile.write(input +"\n")
saveFile.close()