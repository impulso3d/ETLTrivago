import sys
#opening of rejected records file
file = open('rejectedRecords.csv','w')
file.write ('Rejected Records:')
file.close

#execution parameters reading
inputFile = str(sys.argv[1])
outputFile = str(sys.argv[2])
delimiter = str(sys.argv[3])
outputFileType = str(sys.argv[4])

print('Processing '+ inputFile +' input file...')
num_lines = sum(1 for line in open(inputFile))

myfile=open(inputFile, 'r')

#here it begins the construction of the array with column names
headerArray = []

header = myfile.readline().replace('\n','')
countColumns = header.count(delimiter, 0, len(header))+1

iniPos = 0
columnPos = 0
for x in range(1, countColumns):

	columnPos = header.find(delimiter, iniPos, len(header))
	if iniPos > columnPos:
		headerArray.append(header[iniPos:len(header)])
		lineToInsert =  '\t\tCoso" : \"' + header[iniPos:len(header)] + '\",\n'
		
	else:
		headerArray.append(header[iniPos:columnPos])
		lineToInsert =  '\t\tCoso" : \"' + header[iniPos:columnPos] + '\",\n'
	
	iniPos = columnPos+1
	

headerArray.append(header[iniPos:len(header)])	

hotelNumber = 1
columnPos = 0
iniPos = 0
delimiterHotelName = '"'+delimiter #this is the delimiter for the address field, since it´s inside ""
	
import writeOutputFile
import validations
writeOutputFile.writeHeader(outputFile, outputFileType) #write header for output file

for line in range(1, num_lines):
	
	fileLine = myfile.readline().replace('\n','')
	countColumnsLinea = len(fileLine)
	if countColumnsLinea > 0:
	
		hotelNumber = hotelNumber +1
		
		validationReturn = validations.validateLine(fileLine, delimiter, delimiterHotelName, countColumns) #validates the record
		if validationReturn == 0: #if validation is OK then it writes the outputfile body
			writeOutputFile.writeHotelInfo(num_lines, line, fileLine, outputFile, outputFileType, hotelNumber, headerArray, delimiter, delimiterHotelName, countColumns)
		
writeOutputFile.writeEnd(outputFile, outputFileType) #writing output file ending

print('File Processing is finished. Output can be found in ' + outputFile)