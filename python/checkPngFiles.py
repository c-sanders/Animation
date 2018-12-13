import sys

from PIL import Image


def testImage(filenameImage, displayAdditionalInformation) :

	returnValue = None

	try :

		testImage = Image.open(filenameImage)

		if displayAdditionalInformation :

			print("Some basic information about the Image file :")
			print("  Format     : %s" %      testImage.format)
			print("  Dimensions : %d x %d" % (testImage.size[0], testImage.size[0]))
			print("  Mode       : %s" %      testImage.mode)

		try :

			testImage.verify()

			print("Image file is valid : %s" % filenameImage)

		except :

			print("Image file is INVALID : %s" % filenameImage)

			returnValue = filenameImage


	except :

		print("Unable to open image file : %s" % filenameImage)

		returnValue = filenameImage


	return returnValue


listProblemFiles = []

filenameStem   = sys.argv[1]

indexFilenames = int(sys.argv[2])
# indexFilenames = 2000000

displayAdditionalInformation = bool(False)

if sys.argv[4].lower == False :

	displayAdditionalInformation = bool(False)

print("Display additional information = %s" % str(displayAdditionalInformation))

print("Filename stem = %s" % filenameStem)

while indexFilenames <= int(sys.argv[3]) :

	filenameImage = "%s%06d.png" % (filenameStem, indexFilenames)

	# print("%s" % filenameImage)

	returnValue = testImage(filenameImage, displayAdditionalInformation)

	if returnValue != None :

		listProblemFiles.append(returnValue)

	indexFilenames = indexFilenames + 1

if len(listProblemFiles) > 0 :

	print listProblemFiles

else :

	print(">>>>>>>>>>")
	print("No problem files were detected.")
	print("<<<<<<<<<<")
