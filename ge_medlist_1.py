################################################################################
## Script to read the GE's CPS custom medication lists                        ##  
## and convert them into human readable format                                ##
##                                                                            ## 
## John Barnett   2016-03-08                                                  ##
################################################################################


import os

sourceFilesPath = os.curdir + '/eval/'
resultFilesPath = os.curdir + '/results/'
resultFilesRemove = os.curdir + '/results/*.txt'

sourceFiles = os.listdir(sourceFilesPath)

fileCount = 0
#LoopCount = 0

for source_file in sourceFiles:
	#print(sourceFilesPath + source_file)
	fileCount = fileCount + 1
	LoopCount = 0
	
	open_source_file = open(sourceFilesPath + source_file,'r')
	create_destination_file = open(source_file + '_readable.txt','w')
	
	for line in open_source_file:
		LoopCount = LoopCount + 1
		rplCharLine = line.replace(']','')
		lineList = rplCharLine.split('[')
		if LoopCount != 1:
			
			prescribeBrandName = lineList[1]
			prescribeUnitCost = lineList[2]
			prescribePatInstructions = lineList[3]
			
			prescribeQuantity = lineList[4]
			prescribeRefills = lineList[5]
			prescribeDuration = lineList[6]
			prescribeNDC = lineList[9]
			prescribeGPI = lineList[10]
			prescribeGenericName = lineList[14]
			
			prescribeBMN = lineList[15]
			#print(prescribeBMN)
			#print(str(len(prescribeBMN)))
			if prescribeBMN == 'Y\n':
				prescribeBMN = 'Yes'
			else:
				prescribeBMN = 'No'
									
			#print('Brand Name: ' + prescribeBrandName)
			create_destination_file.write(str(LoopCount-1) + '. Brand Name: ' + prescribeBrandName + '\n')
			
			#print('\tInstructions: ' + prescribePatInstructions)
			create_destination_file.write('\tInstructions: ' + prescribePatInstructions + '\n')
			
			#print('\tQuantity: ' + prescribeQuantity)
			create_destination_file.write('\tQuantity: ' + prescribeQuantity + '\n')
			
			#print('\tRefills: ' + prescribeRefills)
			create_destination_file.write('\tRefills: ' + prescribeRefills + '\n')
			
			#print('\tDuration: ' + prescribeDuration)
			create_destination_file.write('\tDuration: ' + prescribeDuration + '\n')
			
			#print('\tBrand Medically Necessary: ' + prescribeBMN)
			create_destination_file.write('\tBrand Medically Necessary: ' + prescribeBMN + '\n')
			
			#print('\tGeneric Name: '+ prescribeGenericName)
			create_destination_file.write('\tGeneric Name: '+ prescribeGenericName + '\n')
			
			#print()
			create_destination_file.write('\n')
			
	print('Drugs listed in ' +  source_file + ' custom medication list: ' + str(LoopCount-1))	
	create_destination_file.close()

	#print('\n\nFiles found: ' + str(fileCount))

