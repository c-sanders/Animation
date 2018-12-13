import os

from ArgumentProcessor  import ArgumentProcessor
from AnimationGenerator import AnimationGenerator


print("Current working directory = %s" % os.getcwd())


# Create the necessary objects.

argumentProcessor  = ArgumentProcessor()

animationGenerator = AnimationGenerator()


# Process the command line arguments.

argumentProcessor.processArguments()

argumentProcessor.printArgumentValues()

animationGenerator.setUtilities(

  argumentProcessor.args.nfnFile,
  argumentProcessor.args.nextFrameNumber,
  argumentProcessor.args.gnuplot
)

animationGenerator.setDirectories(

  argumentProcessor.args.slidesDirectory,
  argumentProcessor.args.gnuplotCodeDirectory,
  argumentProcessor.args.outputDirectory
)


# animationGenerator.generateFrames_Slides()

if argumentProcessor.args.generateSlideFrames == "true" :

	animationGenerator.generateFramesForSlides()

	# Slide 0 : Title

	# slideFilename = argumentProcessor.args.slidesDirectory + "/Eulers_formula_animation_slides-0.png"

	# animationGenerator.generateFramesForSlide("0", slideFilename, argumentProcessor.args.outputDirectory)

	# Slide 1 : Leonhard Euler

	# slideFilename = argumentProcessor.args.slidesDirectory + "/Eulers_formula_animation_slides-1.png"

	# animationGenerator.generateFramesForSlide("1", slideFilename, argumentProcessor.args.outputDirectory)

	# Slide 2 : Definition of Euler's formula

	# slideFilename = args.slidesDirectory + "/Eulers_formula_animation_slides-2.png"

	# animationGenerator.generateFramesForSlide("2", slideFilename, args.outputDirectory)

	# Slide 3 : Plotting Euler's formula

	# slideFilename = args.slidesDirectory + "/Eulers_formula_animation_slides-3.png"

	# animationGenerator.generateFramesForSlide("3", slideFilename, args.outputDirectory)

	# Slide 4 : Description of the plot

	# slideFilename = args.slidesDirectory + "/Eulers_formula_animation_slides-4.png"

	# animationGenerator.generateFramesForSlide("4", slideFilename, args.outputDirectory)

if argumentProcessor.args.generateStage1Frames == "true" :

	# Stage 1 frames

	print("About to begin generating Stage 1 frames")

	animationGenerator.generateFrames_Stage1()

# animationGenerator.generateFrames_Stage2()
# animationGenerator.generateFrames_Slide_7()
# animationGenerator.generateAnimation()

# animationGenerator.generateAnimationWithAudio()

animationGenerator.destroy()
