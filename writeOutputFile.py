import writeJSON

def writeHeader(outputFile, outputFileType):
	if outputFileType == 'JSON':
		writeJSON.writeHeader(outputFile)
		
def writeHotelInfo(num_lines, line, fileLine, outputFile, outputFileType, hotelNumber, headerArray, delimiter, delimiterHotelName, countColumns):
	if outputFileType == 'JSON':
		writeJSON.writeHotelInfo(num_lines, line, fileLine, outputFile, hotelNumber, headerArray, delimiter, delimiterHotelName, countColumns)
		
def writeEnd(outputFile, outputFileType):
	if outputFileType == 'JSON':
		writeJSON.writeEnd(outputFile)