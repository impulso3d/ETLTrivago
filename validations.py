def validateHotelName(hotelName):
	chequeoUTF = bytes(hotelName, 'utf-8')
	strchequeoUTF=str(chequeoUTF)
	strchequeoUTF=strchequeoUTF[2:len(strchequeoUTF)-1]
	if  hotelName == strchequeoUTF:	
		validated = 0
	else:
		validated = 1
			
	return validated
	
def validateNegNumbers(field):

	if (field < 0) :
		validated = 1
	else: 
		validated = 0
		
	return validated

def validateHotelRatings(hotelRating):
	hotelRating = int(hotelRating)
	if (hotelRating >= 0) or (hotelRating <= 5):
		validated = 0
	else: 
		validated = 1
		
	return validated

def validateValidURL(hotelURI):
	import re

	pattern = re.compile('https?://+')
	cadena=str(pattern.search(hotelURI))
	columnPos = cadena.find('http',0, len(cadena))
	columnPos2 = cadena.find('\'>',0, len(cadena))
	checkString=cadena[columnPos:columnPos2]
	if checkString == '':
		validated = 1
	else:
		validated = 0
		
	URL=hotelURI
	
	pattern = re.compile('.*[a-z]/?')
	URLEnd=URL[len(URL)-2:len(URL)]
	cadena=str(pattern.match(URLEnd))
	columnPos = cadena.find('match=\'',0, len(cadena))
	columnPos2 = cadena.find('\'>',0, len(cadena))
	checkString=cadena[columnPos+7:columnPos2]
	if checkString[len(checkString)-2:len(checkString)] == URLEnd:
		validated = validated + 0
	else:
		validated = validated + 1
		
	if int(URL.find('$',0,len(URL))) > 0 or int(URL.find('|',0,len(URL))) > 0 or int(URL.find('°',0,len(URL))) > 0 or int(URL.find('#',0,len(URL))) > 0 or int(URL.find('\'',0,len(URL))) > 0 or int(URL.find('*',0,len(URL))) > 0 or int(URL.find('+',0,len(URL))) > 0 or int(URL.find('[',0,len(URL))) > 0 or int(URL.find('}',0,len(URL))) > 0 or int(URL.find(']',0,len(URL))) > 0 or int(URL.find('{',0,len(URL))) > 0 or int(URL.find(';',0,len(URL))) > 0 or int(URL.find(',',0,len(URL))) > 0 or int(URL.find('^',0,len(URL))) > 0:
		validated = validated + 1
	else:
		validated = validated + 0	
		
	return validated
	
def validateLine(fileLine, delimiter, delimiterHotelName, countColumns):
	
	iHotelNamePos = 0
	iStarsPos = 2
	iURIPos = 5

	fieldsArray = []

	iniPos = 0
	columnPos = 0

	for x in range(1, countColumns):

		if x == 2:
			columnPos = fileLine.find(delimiterHotelName, iniPos, len(fileLine))
			fieldsArray.append(fileLine[iniPos:columnPos+1])
			iniPos = columnPos+2
		else:
			columnPos = fileLine.find(delimiter, iniPos, len(fileLine))
			if iniPos > columnPos:
				fieldsArray.append(fileLine[iniPos:len(fileLine)])
			else:
				fieldsArray.append(fileLine[iniPos:columnPos])
				iniPos = columnPos+1
		
	fieldsArray.append(fileLine[iniPos:len(fileLine)])	
	validationValue = 0
	validationValue = validateHotelName(fieldsArray[iHotelNamePos])
	validationValue = validationValue + validateHotelRatings(fieldsArray[iStarsPos])
	validationValue = validationValue + validateValidURL(fieldsArray[iURIPos])
	
	if validationValue > 0:
		file = open('rejectedRecords.csv','a')
		file.write (fileLine+'\n')
		file.close
	
	return validationValue