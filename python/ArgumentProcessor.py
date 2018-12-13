import argparse


class ArgumentProcessor :

	nameClass = "ArgumentProcessor"


	parser = None
	args   = None


	# ================================================================================
	# Method : ArgumentProcessor::__init__
	#
	# ================================================================================
	# NOTE(S) :
	#
	# - This method is the Constructor for this class.
	# ================================================================================

	def __init__(self) :

		self.parser = argparse.ArgumentParser(description="Create a number of frames, and then use them to generate an animation.")

		self.__addArguments()


	# ================================================================================
	# Method : AnimationGenerator::addArguments
	#
	# ================================================================================

	def __addArguments(self) :

		self.parser.add_argument(

			"--frameRate",
			# metavar='N',
			type    = int,
			default = 25,
			# nargs='+',
			help    = "specify the Frame Rate for the animation"
		)

		self.parser.add_argument(

			"--nfnFile",
			# default = "nextFrameNumber.txt",
			help    = "specify the name of the Next Frame Number (nfn) file"
		)

		self.parser.add_argument(

			"--nextFrameNumber",
			default = "1",
			help    = "specify the value of the next Frame number to be generated"
		)

		self.parser.add_argument(

			"--sourceDirectory",
			default = "./",
			help    = "specify the name of the top-level Source directory"
		)

		self.parser.add_argument(

			"--buildDirectory",
			default = "./",
			help    = "specify the name of the top-level Build directory"
		)

		self.parser.add_argument(

			"--resolution",
			default = "1920 x 1080",
			help    = "specify the Resolution for the animation"
		)

		self.parser.add_argument(

			"--aspectRatio",
			default = "16:9",
			help    = "specify the Aspect Ratio for the animation"
		)

		self.parser.add_argument(

			"--slidesDirectory",
			default = "./",
			help    = "specify the directory which the Slides reside in"
		)

		self.parser.add_argument(

			"--outputDirectory",
			default = "./",
			help    = "specify the Output directory which the animation frames should be saved into"
		)

		self.parser.add_argument(

			"--gnuplot",
			default = "gnuplot",
			help    = "specify the path to the gnuplot program"
		)

		self.parser.add_argument(

			"--gnuplotCodeDirectory",
			default = "./",
			help    = "specify the path to the gnuplot source code"
		)

		self.parser.add_argument(

			"--generateSlideFrames",
			default = "false",
			help    = "specify if Slide frames should be generated"
		)

		self.parser.add_argument(

			"--generateStage1Frames",
			default = "false",
			help    = "specify if Stage 1 frames should be generated"
		)

		self.parser.add_argument(

			"--generateStage2Frames",
			default = "false",
			help    = "specify if Stage 2 frames should be generated"
		)


	# ================================================================================
	# Method : AnimationGenerator::processArguments
	#
	# ================================================================================

	def processArguments(self) :

		self.args = self.parser.parse_args()

		# print args.accumulate(args.integers)


	# ================================================================================
	# Method : AnimationGenerator::printArgumentValues
	#
	# ================================================================================

	def printArgumentValues(self) :

		print("================================================================================")
		print("NFN file             = %s" % self.args.nfnFile)
		print("nextFrameNumber      = %s" % self.args.nextFrameNumber)
		print("sourceDirectory      = %s" % self.args.sourceDirectory)
		print("frameRate            = %s" % self.args.frameRate)
		print("generateSlideFrames  = %s" % self.args.generateSlideFrames)
		print("generateStage1Frames = %s" % self.args.generateStage1Frames)
		print("slidesDirectory      = %s" % self.args.slidesDirectory)
		print("gnuplotCodeDirectory = %s" % self.args.gnuplotCodeDirectory)
		print("================================================================================")
