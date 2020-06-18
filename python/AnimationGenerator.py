# import SinusoidGenerator

import sys
import os
import subprocess
import shutil
import collections


# LaTeX Beamer files are located in the following directory;
#
#   - ${package_dir}/latex/
#
# PDF files are located in the following directory;
#
#   - ${package_dir}/pdf/
#
# Frames for the animation are located in the following directory;
#
#   - ${package_dir}/images/png/


class AnimationGenerator :

	#> Documentation for a class.
	#- ================================================================================
	#- Class : AnimationGenerator
	#-
	#- This class is responsible for creating a number of animation frames and then using them to make an animation.
	#<

	nameClass                = "AnimationGenerator"

	fileHandle               = None

	plotAll                  = 0

	gnuplot                  = "/home/craig/local/gnuplot-5.0.5/bin/gnuplot"
	file_gp                  = "Eulers_formula.gp"

	frameRateAnimation       = 25
	resolutionAnimation      = "1920x1080"
	aspectRatioAnimation     = "16:9"
	filenameAnimation        = "../../videos/Eulers_formula.mp4"

	gnuplotCodeDirectory     = ""
	outputDirectory          = ""
	slidesDirectory          = ""

	frameNumber              = 1

	slideFilenames           = {"0":"/Eulers_formula_animation_slides-0.png",
								"1":"/Eulers_formula_animation_slides-1.png",
								"2":"/Eulers_formula_animation_slides-2.png",
								"3":"/Eulers_formula_animation_slides-3.png",
								"4":"/Eulers_formula_animation_slides-4.png",
								"5":"/Eulers_formula_animation_slides-5.png",
								"6":"/Eulers_formula_animation_slides-6.png",
								"7":"/Eulers_formula_animation_slides-7.png",
								"8":"/Eulers_formula_animation_slides-8.png",
								"9":"/Eulers_formula_animation_slides-9.png"}

	# The following values denote the time in seconds.

	displayTime_Slide_Title  = 5
	displayTime_Slide_1      = 10
	displayTime_Slide_2      = 10
	displayTime_Slide_3      = 10

	displayTimes             = {"0":5,
								"1":10,
								"2":10,
								"3":10,
								"4":10,
								"5":10,
								"6":10,
								"7":10,
								"8":10,
								"9":10
							   }

	# 250 iterations over 720 degrees : 720 / 250 = 2.88 degrees per iteration

	maxIteration             = 250
	index                    = 0

	# view_x_increment_stage_1 = 0.48387097
	view_x_increment_stage_1 = 0.584416
	view_x_increment_stage_2 = 0
	view_x_increment_stage_3 = -0.405405

	# view_x_increment_stage_1 = 0
	# view_x_increment_stage_2 = 0
	# view_x_increment_stage_3 = 0

	view_y_increment         = 2.88

	# Co-ordinates for the starting view

	view_x_initial           = 45
	view_y_initial           = 48.24   # 90 degrees is front on, i.e. looking straight at the y-z plane.

	view_x                   = 0
	view_y                   = 0


	#> Documentation for a method.
	#- ================================================================================
	#- Method : AnimationGenerator::__init__
	#-
	#- Constructor for the class.
	#<

	def __init__(self) :

		self.displayStartupMessage()

		self.fileHandle = open("fileList.txt", "w")


	#> Documentation for a method.
	#- ================================================================================
	#- Method : AnimationGenerator::destroy
	#-
	#- Destructor for the class.
	#<

	def destroy(self) :

		self.fileHandle.close()


	#> Documentation for a method.
	#- ================================================================================
	#- Method : AnimationGenerator::displayStartupMessage
	#-
	#- Display a startup message.
	#<

	def displayStartupMessage(self) :

		sys.stderr.write("")
		sys.stderr.write("================================================================================")
		sys.stderr.write("================================================================================")
		sys.stderr.write("x-axis : Goes into and out of the screen.")
		sys.stderr.write("y-axis : Goes left to right across the screen, i.e. horizontal")
		sys.stderr.write("z-axis : Goes up and down the screen, i.e. vertical.")
		sys.stderr.write("")
		sys.stderr.write("x-view : The angle made with the x-y plane.")
		sys.stderr.write("")
		sys.stderr.write("y-view : The angle made with the y-z plane.")
		sys.stderr.write("")
		sys.stderr.write("Altering the value of the x-view causes the view to rotate about the x-axis.")
		sys.stderr.write("")
		sys.stderr.write("Altering the value of the y-view causes the view to rotate about the z-axis.")
		sys.stderr.write("================================================================================")
		sys.stderr.write("================================================================================")


	#> Documentation for a method.
	#- ================================================================================
	#- Method : AnimationGenerator::setUtilities
	#-
	#- Set some attributes.
	#<

	def setUtilities(self, nfnFile, frameNumber, gnuplot) :

		nameMethod = self.nameClass + "::setUtilities"

		self.nfnFile     = nfnFile
		self.frameNumber = int(frameNumber)
		self.gnuplot     = gnuplot


	#> Documentation for a method.
	#- ================================================================================
	#- Method : AnimationGenerator::setDirectories
	#-
	#- Set some attributes.
	#<

	def setDirectories(self, slidesDirectory, gnuplotCodeDirectory, outputDirectory) :

		nameMethod = self.nameClass + "::setDirectories"


		self.slidesDirectory      = os.path.normpath(slidesDirectory)      + "/"
		self.gnuplotCodeDirectory = os.path.normpath(gnuplotCodeDirectory) + "/"
		self.outputDirectory      = os.path.normpath(outputDirectory)      + "/"

		self.file_gp = self.gnuplotCodeDirectory + self.file_gp

		sys.stderr.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		sys.stderr.write("gnuplot code directory = %s" % self.gnuplotCodeDirectory)
		sys.stderr.write("Output directory       = %s" % self.outputDirectory)
		sys.stderr.write("")
		sys.stderr.write("gnuplot script file    = %s" % self.file_gp)
		sys.stderr.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


	#> Documentation for a method.
	#- ================================================================================
	#- Method : AnimationGenerator::generateFrames_Slides
	#-
	#- ### This method may be obsolete. ###
	#<

	def __generateFrames_Slides(self) :

		# Use the LaTeX file to create the Title frame as a PDF file.

		sys.stderr.write("About to create file : ../pdf/Eulers_formula_animation_slides.pdf")

		subprocess.call(
		  [
		   "pdflatex",
		   "-output-directory=../pdf",
		   "../latex/Eulers_formula_animation_slides.tex"
		  ]
		)

		sys.stderr.write("Have created file : ../pdf/Eulers_formula_animation_slides.pdf")

		# Use the PDF version of the Title frame to create a PNG version of it.

		sys.stderr.write("About to create file : ../animation/png/title.png")

		subprocess.call(
		  [
		   "convert",
		   "-density", "300",
		   "-quality", "90",
		   "../pdf/Eulers_formula_animation_slides.pdf",
		   "../images/png/slides/Eulers_formula_animation_slides.png"
		  ]
		)

		# sys.stderr.write("Have created file : ../animation/png/title.png")

		#

		index = 1

		while (index <= (self.displayTime_Slide_Title * self.frameRateAnimation)) :

			filename = "../images/png/Eulers_formula_" + str(self.frameNumber) + ".png"

			sys.stderr.write("About to create file : %s" % filename)

			shutil.copyfile("../images/png/slides/1920x1080/Eulers_formula_animation_slides-0.png", filename)

			sys.stderr.write("Have created file    : %s" % filename)

			index            += 1
			self.frameNumber += 1


	#  <method>
	#- ================================================================================
	#- Method : AnimationGenerator::generateFramesForSlide
	#-
	#- Generate a frame for a given the slide.
	#-
	#- This method is used by the following methods;
	#-
	#-   - generateFramesForSlides
	#  </method>

	def __generateFramesForSlide(self, slideNumber, slideFilename) :

		index = 1

		sys.stderr.write("slideNumber            = %d" % slideNumber)
		sys.stderr.write("self.displayTimes[%03d] = %d" % (slideNumber, self.displayTimes[str(slideNumber)]))
		sys.stderr.write("slideFilename          = %s" % slideFilename)
		sys.stderr.write("index                  = %d" % index)

		while (index <= (self.displayTimes[str(slideNumber)] * self.frameRateAnimation)) :

			# filenameSource      = "../png/Eulers_formula_animation_slides-" + slideNumber + ".png"
			# filenameDestination = self.outputDirectory + "/Eulers_formula_" + str(self.frameNumber) + ".png"

			# filenameSource      = inputDirectory  + "/Eulers_formula_animation_slides-" + slideNumber + ".png"
			# filenameDestination = outputDirectory + "/Eulers_formula_"                  + str(self.frameNumber) + ".png"
			filenameDestination = "%s/Eulers_formula_%06d.png" % (self.outputDirectory, self.frameNumber)

			sys.stderr.write("Source file      = %s" % slideFilename)
			sys.stderr.write("Destination file = %s" % filenameDestination)

			shutil.copyfile(slideFilename, filenameDestination)

			sys.stderr.write("    Have created file : %s" % filenameDestination)

			self.fileHandle.write(filenameDestination + "\n")

			index            += 1
			self.frameNumber += 1


	#  <method>
	#- ================================================================================
	#- Method : AnimationGenerator::generateFrame
	#-
	#- Generate a frame.
	#-
	#- This method is used by the following methods;
	#-
	#-   - generateFrames_Stage1
	#-   - generateFrames_Stage2
	#  </method>

	def __generateFrame(self) :

		nameMethod = "generateFrame"

		view_x = self.view_x
		view_y = self.view_y

		if ((view_x / 360) >= 1) :

			view_x = view_x - ((view_x // 360) * 360)

		if ((view_y / 360) >= 1) :

			view_y = view_y - ((view_y // 360) * 360)

		# FIXME

		# filename            = "../../frames/Eulers_formula_" + str(self.frameNumber) + ".png"
		filenameDestination = "%sEulers_formula_%06d.png" % (self.outputDirectory, self.frameNumber)
		# self.file_gp        = self.gnuplotCodeDirectory + "/" + self.file_gp
		filename_arg        = "filename='"           + filenameDestination + "'"
		index_arg           = "index="               + str(self.index)
		view_x_arg          = "view_x="              + str(view_x)
		view_y_arg          = "view_y="              + str(view_y)
		maxIteration_arg    = "maxIteration="        + str(self.maxIteration)
		title_arg           = "myTitle=\""           + str(self.index) + " : (" + str(self.view_x) + ", " + str(self.view_y) + ")\""
		plotAll_arg         = "plotAll="             + str(self.plotAll)

		sys.stderr.write("++++++++++++++++++++++++++++++++++++++++\n")
		sys.stderr.write("%s::%s : \n" % (self.nameClass, nameMethod))
		sys.stderr.write("Index                  = %d\n" % self.index)
		sys.stderr.write("filenameDestination    = %s\n" % filenameDestination)
		sys.stderr.write("Title                  = %s\n" % title_arg)
		sys.stderr.write("\n")
		sys.stderr.write("gnuplot script file    = %s\n" % self.file_gp)
		sys.stderr.write("gnuplot code directory = %s\n" % self.gnuplotCodeDirectory)
		sys.stderr.write("Filename arg           = %s\n" % filename_arg)
		sys.stderr.write("\n")
		sys.stderr.write("View = (%f, %f)\n" % (self.view_x, self.view_y))
		sys.stderr.write("\n")
		sys.stderr.write("self.gnuplot     = %s\n" % (self.gnuplot))
		sys.stderr.write("filename_arg     = %s\n" % (filename_arg))
		sys.stderr.write("title_arg        = %s\n" % (title_arg))
		sys.stderr.write("maxIteration_arg = %s\n" % (maxIteration_arg))
		sys.stderr.write("index_arg        = %s\n" % (index_arg))
		sys.stderr.write("view_x_arg       = %s\n" % (view_x_arg))
		sys.stderr.write("view_y_arg       = %s\n" % (view_y_arg))
		sys.stderr.write("plotAll_arg      = %s\n" % (plotAll_arg))
		sys.stderr.write("self.file_gp     = %s\n" % (self.file_gp))
		sys.stderr.write("++++++++++++++++++++++++++++++++++++++++\n")

		subprocess.call(
		  [
		   self.gnuplot,
		   "-e", "verbose=0",
		   "-e", filename_arg,
		   "-e", title_arg,
		   "-e", maxIteration_arg,
		   "-e", index_arg,
		   "-e", view_x_arg,
		   "-e", view_y_arg,
		   "-e", plotAll_arg,
		   self.file_gp
		  ]
		)

		# The image that was just generated by gnuplot will need to be scaled vertically so that it doesn't look "squashed".

		self.fileHandle.write(filenameDestination + "\n")


	#> Documentation for a method.
	#- ================================================================================
	#- Method : AnimationGenerator::writeFrameNumberToFile
	#-
	#- Write the current value of the Frame number into a file.
	#<

	def writeFrameNumberToFile(self) :

		frameNumber_file = open(self.nfnFile, "w")

		frameNumber_file.write(str(self.frameNumber))

		frameNumber_file.close()


	#> Documentation for a method.
	#- ================================================================================
	#- Method : AnimationGenerator::generateFramesForSlides
	#-
	#- Generate frames for the slides.
	#<

	def generateFramesForSlides(self) :

		# Slide 0 : Title

		for key in sorted(self.slideFilenames) :

			slideFilename = self.slidesDirectory + self.slideFilenames[key]

			sys.stderr.write("Key            = %s" % key)
			sys.stderr.write("Slide filename = %s" % slideFilename)

			self.__generateFramesForSlide(int(key), slideFilename)

		# Save the current value of the Frame number by writing it into a file.

		self.writeFrameNumberToFile()


	#  <method>
	#- ================================================================================
	#- Method : AnimationGenerator::generateFrames_Stage1
	#-
	#- Generate all the frames which are required for Stage 1.
	#  </method>

	def generateFrames_Stage1(self) :

		self.plotAll = 1
		self.view_x  = self.view_x_initial
		self.view_y  = self.view_y_initial

		# self.setupTitle()

		# Mid point view should be 90, 90
		#
		# End view should be something like 50, 145
		#
		# set view 50, 140

		while self.index <= self.maxIteration :

			if (self.view_y < 270) :

				# Descend from the stating view point whilst rotating counter clockwise around the z-axis.

				view_x_increment = self.view_x_increment_stage_1

			if (self.view_y >= 270) and (self.view_y <= 450) :

				# Rotate counter clockwise around the z-axis at a height of z = 0

				self.view_x      = 90
				view_x_increment = self.view_x_increment_stage_2

			if (self.view_y > 450) :

				# Ascend back up to the original starting point whilst rotating counter clockwise around the z-axis.

				view_x_increment = self.view_x_increment_stage_3

			self.view_x +=  view_x_increment

			# Generate the frame using the variables which were just calculated.

			self.__generateFrame()

			# if (self.view == 270) :

			# 	counter = 0

			# 	while (counter < 10) :

			# Update all of the necessary variables.

			self.frameNumber += 1
			self.index       += 1

			self.view_y = (self.index * self.view_y_increment) + self.view_y_initial

		# Save the current value of the Frame number by writing it into a file.

		self.writeFrameNumberToFile()


	#  <method>
	#- ================================================================================
	#- Method : AnimationGenerator::generateFrames_Stage2
	#-
	#- Generate all the frames which are required for Stage 2.
	#  </method>

	def generateFrames_Stage2(self) :

		self.plotAll = 0

		index        = 1
		self.index   = 250

		self.view_x  = self.view_x_initial + self.view_x_increment_stage_1
		self.view_y  = (index * self.view_y_increment) + self.view_y_initial

		# Mid point view should be 90, 90
		#
		# End view should be something like 50, 145
		#
		# set view 50, 140

		while index <= self.maxIteration :

			if (self.view_y < 270) :

				# Descend from the stating view point whilst rotating counter clockwise around the z-axis.

				view_x_increment = self.view_x_increment_stage_1

			if (self.view_y >= 270) and (self.view_y <= 450) :

				# Rotate counter clockwise around the z-axis at a height of z = 0

				self.view_x      = 90
				view_x_increment = self.view_x_increment_stage_2

			if (self.view_y > 450) :

				# Ascend back up to the original starting point whilst rotating counter clockwise around the z-axis.

				view_x_increment = self.view_x_increment_stage_3

			self.view_x +=  view_x_increment

			# Generate the frame using the variables which were just calculated.

			self.generateFrame()

			# if (self.view == 270) :

			# 	counter = 0

			# 	while (counter < 10) :

			# Update all of the necessary variables.

			self.frameNumber += 1
			index            += 1

			self.view_y = (index * self.view_y_increment) + self.view_y_initial

		# Save the current value of the Frame number by writing it into a file.

		self.writeFrameNumberToFile()


	#  <method>
	#- ================================================================================
	#- Method : AnimationGenerator::generateAnimation
	#-
	#- Generate an animation from the frames.
	#  </method>

	def generateAnimation(self) :

		# Create the animation using all of the frames.
		#
		#   -y      : Overwrite output files
		#   -aspect : Set the aspect ratio for the output file
		#   -s      : Set the frame size
		#   -r      : Set the frame rate
		#   -i      : Set the input files (either audio or video)

		subprocess.call(
		  [
		   "ffmpeg",
		   "-y",
		   "-r", str(self.frameRateAnimation),
		   "-s", self.resolutionAnimation,
		   "-i", "../images/png/Eulers_formula_%d.png",
		   "-aspect", self.aspectRatioAnimation,
		   self.filenameAnimation
		  ]
		)


	# Method : AnimationGenerator::generateAnimationWithAudio

	def generateAnimationWithAudio(self) :

		# Create the animation using all of the frames.

		subprocess.call(
		  [
		   "ffmpeg",
		   "-y",
		   "-r", str(self.frameRateAnimation),
		   "-s", self.resolutionAnimation,
		   "-i", "../images/png/Eulers_formula_%d.png",
		   "-i", "../output.wav",
		   self.filenameAnimation
		  ]
		)
