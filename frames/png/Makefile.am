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

	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : frames/png/Makefile          \n"
	@printf "Target   : slide_frames                 \n"
	@printf "Status   : Enter                        \n"
	@printf "========================================\n"
	@printf "========================================\n"
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
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : frames/png/Makefile          \n"
	@printf "Target   : slide_frames                 \n"
	@printf "Status   : Exit                        \n"
	@printf "========================================\n"
	@printf "========================================\n"


.PHONY          : animation_stage1_frames
animation_stage1_frames :

	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : frames/png/Makefile          \n"
	@printf "Target   : animation_stage1_frames      \n"
	@printf "Status   : Enter                        \n"
	@printf "                                        \n"
	@printf "sourceDirectory      = ${abs_srcdir}         \n"
	@printf "buildDirectory       = ${abs_builddir}       \n"
	@printf "frameRate            = ${FRAME_RATE_ANIMATION}\n"
	@printf "resolution           = ${RESOLUTION_ANIMATION}\n"
	@printf "aspectRation         = \"16:9\"              \n"
	@printf "gnuplot              = ${GNUPLOT}            \n"
	@printf "outputDirectory      = ${abs_builddir}       \n"
	@printf "slidesDirectory      = ${abs_builddir}/../../slides/png\n"
	@printf "gnuplotCodeDirectory = ${abs_srcdir}/../../gnuplot/"
	@printf "generateStage1Frames = true             \n"
	@printf "========================================\n"
	@printf "========================================\n"
	python  ${srcdir}/../../python/createFrames.py \
			--sourceDirectory      ${abs_srcdir} \
			--buildDirectory       ${abs_builddir} \
			--frameRate            ${FRAME_RATE_ANIMATION} \
			--resolution           ${RESOLUTION_ANIMATION} \
			--aspectRatio          "16:9" \
			--gnuplot              ${GNUPLOT} \
			--outputDirectory      ${abs_builddir} \
			--slidesDirectory      ${abs_builddir}/../../slides/png/ \
			--gnuplotCodeDirectory ${abs_srcdir}/../../gnuplot/ \
			--generateStage1Frames "true"
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : frames/png/Makefile          \n"
	@printf "Target   : animation_stage1_frames      \n"
	@printf "Status   : Exit                         \n"
	@printf "========================================\n"
	@printf "========================================\n"


.PHONY          : animation_stage2_frames
animation_stage2_frames :

	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : frames/png/Makefile          \n"
	@printf "Target   : animation_stage2_frames      \n"
	@printf "Status   : Enter                        \n"
	@printf "========================================\n"
	@printf "========================================\n"
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
			--generateStage2Frames "true"
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : frames/png/Makefile          \n"
	@printf "Target   : animation_stage2_frames      \n"
	@printf "Status   : Exit                         \n"
	@printf "========================================\n"
	@printf "========================================\n"
			

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

