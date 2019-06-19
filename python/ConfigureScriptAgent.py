import sys
import readline
import time
import os

# /home/craig/local/source/GitHub_projects/c-sanders/Animation_build
# ---------|---------|---------|---------|---------|---------|-------


class ConfigureScriptAgent :

	className    = "ConfigureScriptAgent"

	srcDir       = os.path.dirname(__file__)
	scriptMD5    = "26e3fdd4e7876e56f24d7975a954376c"

	buildDir = ""


	def run(

	  self
	) :

		procedureName = self.className + "::run"


		print("%s : Enter" % (procedureName))

		self.displaySettings()

		# self.displayStartMessage()

		self.getBuildDirectory()

		# self.testSettings()

		if os.path.exists(self.buildDir) :

			if not os.path.isdir(self.buildDir) :

				raise Exception("File already exists but it not a directory : %s" % (self.buildDir))

		else : 

			self.createBuildDirectory()

		self.runConfigureScriptInitial()

		self.runConfigureScriptFinal()

		print("%s : Exit" % (procedureName))


	def displaySettings(

	  self
	) :

		procedureName = self.className + "::displaySettings"


		print("%s : Enter" % (procedureName))

		print("Name of this script : %s" % (__file__))
		print("Source dir          : %s" % (self.srcDir))

		print("%s : Exit" % (procedureName))


	def displayStartMessage(

	  self
	) :

		procedureName = self.className + "::displayStartMessage"


		print("%s : Enter" % (procedureName))

		print("============================================================")
		print("============================================================")
		print("Please run this script from the directory within which it   ")
		print("is located.                                                 ")
		print("============================================================")
		print("============================================================")

		print("%s : Exit" % (procedureName))


	def getBuildDirectory(

	  self
	) :

		procedureName = self.className + "::getBuildDirectory"


		print("%s : Enter" % (procedureName))

		print("Please enter the full name of the build directory.")
		print("")
		sys.stdout.write("> ")
		sys.stdout.flush()

		self.buildDir = sys.stdin.readline()
	
		if self.buildDir.endswith("\n") :

			self.buildDir = self.buildDir[:-1]

		if self.buildDir.endswith("/") :

			self.buildDir = self.buildDir[:-1]

		print("Build directory = %s\n" % (self.buildDir))

		print("%s : Exit" % (procedureName))


	def testSettings(

	  self
	) :

		procedureName = self.className + "::testSettings"


		print("%s : Enter" % (procedureName))

		if os.path.isfile(self.scriptN) :

			print("File exists : %s" % (self.scriptNameFQ))

		else :

			print("File does NOT exist : %s" % (self.scriptNameFQ))

		print("%s : Exit" % (procedureName))


	def createBuildDirectory(

	  self
	) :

		procedureName = self.className + "::createBuildDirectory"


		print("%s : Enter" % (procedureName))

		command = "mkdir -p " + self.buildDir

		os.system(command)

		print("%s : Exit" % (procedureName))


	def runConfigureScriptInitial(

	  self
	) :

		procedureName = self.className + "::runConfigureScriptInitial"


		print("%s : Enter" % (procedureName))

		# Perform an initial execution of the configure script from within the Build directory.
		#
		# This will cause the file runConfigure.sh to be created in the Build directory.

		command = "cd " + self.buildDir + " && " + self.srcDir + "/configure"

		print("============================================================")
		print("About to invoke the initial execution of the configure      ")
		print("script.                                                     ")
		print("                                                            ")
		print("The execution will be invoked from within the Build         ")
		print("directory which was just specified.                         ")
		print("                                                            ")
		print("This will commence in 10 seconds.                           ")
		print("============================================================")

		timer = 0

		while timer < 10 :

			sys.stdout.write(".")
			sys.stdout.flush()

			time.sleep(1)

			timer = timer + 1

		print("")

		os.system(command)

		command = "cd " + self.buildDir + " && chmod u+x ./runConfigure.sh"

		os.system(command)

		print("%s : Exit" % (procedureName))


	def runConfigureScriptFinal(
	
	  self
	) :

		procedureName = self.className + "::runConfigureScriptFinal"


		print("%s : Enter" % (procedureName))

		# cd into the Build directory and then execute the configure script from within it.

		print("============================================================")
		print("About to invoke the final execution of the configure        ")
		print("script.                                                     ")
		print("                                                            ")
		print("This execution - just like the initial one, will also be    ")
		print("invoked from within the Build directory.                    ")
		print("                                                            ")
		print("The configure script will be invoked as shown below. If you ")
		print("want to change the way that the configure script will be    ")
		print("invoked, then you should exit out of this installer and     ")
		print("invoke the configure script yourself.                       ")
		print("                                                            ")
		print("This will commence in 30 seconds.                           ")
		print("                                                            ")
		print("Explanation of some of the options                          ")
		print("----------------------------------                          ")
		print("                                                            ")
		print("  --with-gnuplot=/usr/bin/gnuplot                           ")
		print("                                                            ")
		print("The gnuplot program is used to generate all of the          ")
		print("mathematical plots which are used by the animation. As a    ")
		print("consquence, the build process needs to know where it can    ")
		print("find it.                                                    ")
		print("                                                            ")
		print("  --with-ffmpeg=/usr/bin/ffmpeg                             ")
		print("                                                            ")
		print("The ffmpeg program is used to combine all of the animation  ")
		print("frames together to produce the resulting animation. As a    ")
		print("consequence, the build process needs to know where it can   ")
		print("find it.                                                    ")
		print("                                                            ")
		print("  --with-frame_rate_animation=\"25\"                        ")
		print("                                                            ")
		print("The ffmpeg program needs to know what rate (in frames per   ")
		print("second), to generate the animation at.                      ")
		print("                                                            ")
		print("  --with-colour_profile=/usr/share/color/icc/colord/sRGB.icc")
		print("                                                            ")
		print("Unless it is told otherwise, the ImageMagick convert utility")
		print("will convert the PDF files using a ... Colour Profile. This ")
		print("will cause problems when the ...                            ")
		print("============================================================")

		command = "cd " + self.buildDir + " && cat ./runConfigure.sh"

		print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		os.system(command)
		print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
		
		timer = 0
		
		while timer < 30 :
		
			sys.stdout.write(".")
			sys.stdout.flush()
			
			time.sleep(1)
		
			timer = timer + 1
		
		print("")

		os.system(command)

		command = "cd " + self.buildDir + " && ./runConfigure.sh"

		os.system(command)
		
		print("%s : Exit" % (procedureName))
