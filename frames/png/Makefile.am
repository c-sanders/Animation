# The following Environment variables are used by this Makefile but should be
# set externally by the Autoconf configure script ;
#
#   - FRAME_RATE_ANIMATION   = "25"
#   - RESOLUTION_ANIMATION   = "1920x1080"
#   - ASPECT_RATIO_ANIMATION = "16:9"
#
# ==================================================================================================
# Directory : ./Eulers_formula/frames/png/
#
#   - Copy the 1920 x 1080 PNG files into frames.
#
#   - Create the animation frames.
# ==================================================================================================


vpath %.pdf ../../slides/pdf


# The files listed in ${pdf_file} are the dependencies for the target ${png_file}.

pdf_file = Eulers_formula_animation_slides.pdf


all : slide_frames \
	  animation_stage1_frames \
	  animation_stage2_frames


slide_frames : ${pdf_file}

	python  ${srcdir}/../../python/createFrames.py \
			--sourceDirectory      ${abs_srcdir} \
			--buildDirectory       ${abs_builddir} \
			--frameRate            ${FRAME_RATE_ANIMATION} \
			--resolution           ${RESOLUTION_ANIMATION} \
			--aspectRatio          "16:9" \
			--gnuplot              ${GNUPLOT} \
			--outputDirectory      ${abs_builddir} \
			--slidesDirectory      ${abs_builddir}/../../slides/png \
			--gnuplotCodeDirectory ${abs_srcdir}/../../gnuplot/ \
			--generateSlideFrames  "true"



.PHONY          : animation_stage1_frames
animation_stage1_frames :

	python  ${srcdir}/../../python/createFrames.py \
			--sourceDirectory      ${abs_srcdir} \
			--buildDirectory       ${abs_builddir} \
			--frameRate            ${FRAME_RATE_ANIMATION} \
			--resolution           ${RESOLUTION_ANIMATION} \
			--aspectRatio          "16:9" \
			--gnuplot              ${GNUPLOT} \
			--outputDirectory      ${abs_builddir} \
			--slidesDirectory      ${abs_builddir}/../../slides/png \
			--gnuplotCodeDirectory ${abs_srcdir}/../../gnuplot/ \
			--generateStage1Frames "true"


.PHONY          : animation_stage2_frames
animation_stage2_frames :

	python  ${srcdir}/../../python/createFrames.py \
			--sourceDirectory      ${abs_srcdir} \
			--buildDirectory       ${abs_builddir} \
			--frameRate            ${FRAME_RATE_ANIMATION} \
			--resolution           ${RESOLUTION_ANIMATION} \
			--aspectRatio          "16:9" \
			--gnuplot              ${GNUPLOT} \
			--outputDirectory      ${abs_builddir} \
			--slidesDirectory      ${abs_builddir}/../../slides/png \
			--gnuplotCodeDirectory ${abs_srcdir}/../../gnuplot/ \
			--generateStage1Frames "true"


.PHONY          : displaySettings
displaySettings :

	@echo "srcdir               = ${srcdir}"
	@echo "abs_srcdir           = ${abs_srcdir}"
	@echo "builddir             = ${builddir}"
	@echo "abs_builddir         = ${abs_builddir}"
	@echo "FFMPEG               = ${FFMPEG}"
	@echo "GNUPLOT              = ${GNUPLOT}"
	@echo "FRAME_RATE_ANIMATION = ${FRAME_RATE_ANIMATION}"
	@echo "RESOLUTION_ANIMATION = ${RESOLUTION_ANIMATION}"

