def writeHeader(outputFile):
	file = open(outputFile,'w')
	file.write ("{\n")
	file.close
	
def writeHotelInfo(num_lines, line, fileLine, outputFile, hotelNumber, headerArray, delimiter, delimiterHotelName, countColumns):
	
	file =open(outputFile, 'a')
	countColumnsLinea = len(fileLine)
	
	if countColumnsLinea > 0:
	
		file.write ("\n\t\"Hotel information " + str(hotelNumber) + "\": {\n")
		hotelNumber = hotelNumber +1
		iniPos = 0
		
		for x in range(0, countColumns-1):
		
			if x == 1:
				columnPos = fileLine.find(delimiterHotelName, iniPos, len(fileLine))
				lineToInsert =  '\t\t\"' + headerArray[x] + '" : ' + fileLine[iniPos:columnPos] + '",\n'
				
				file.write(lineToInsert)
				iniPos = columnPos+2
			else: 
				columnPos = fileLine.find(delimiter, iniPos, len(fileLine))
				lineToInsert =  '\t\t"' + headerArray[x] + '" : "' + fileLine[iniPos:columnPos] + '",\n'
				
				
				
				file.write(lineToInsert)
				iniPos = columnPos+1 
			
		lineToInsert =  "\t\t\"" + headerArray[countColumns-1] + "\" : \"" + fileLine[iniPos:len(fileLine)] + '"\n'
		file.write(lineToInsert)
		if line < num_lines -2:	
			file.write('\t},\n')
		else:
			file.write('\t}\n')

			
def writeEnd(outputFile):
	file = open(outputFile,'a')
	file.write('}')
	file.close