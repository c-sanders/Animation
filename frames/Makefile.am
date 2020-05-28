 # The following Environment variables are used by this Makefile but should be
# set externally by the Autoconf configure script ;
#
#   - FRAME_RATE_ANIMATION   = "25"
#   - RESOLUTION_ANIMATION   = "1920x1080"
#   - ASPECT_RATIO_ANIMATION = "16:9"
#
# ==================================================================================================
# Directory : ./Eulers_formula/frames/
#
#   - Create frames from the 1920 x 1080 PNG Slide files.
#
#   - Create the animation frames.
# ==================================================================================================
#
# This Makefile contains a number of targets;
#
#   - png_slideFrames_1
#   - png_animationFrames_1
#   - png_slideFrames_2
#   - png_animationFrames_2
#
# Target : png_slideFrames_1
#
#     Create the 1st set of Slide frames by copying and renaming - as appropriate, the 1st set of Slides.
#
# Target : png_animationFrames_1
#
#     Create the 1st set of Animation frames by running gnuplot.
#
# Target : png_slideFrames_2
#
#     Create the 2nd set of Slide frames by copying and renaming - as appropriate, the 2nd set of Slides.
#
# Target : png_animationFrames_2
#
#     Create the 2nd set of Animation frames by running gnuplot.


SUBDIRS = png


vpath %.gp  ../gnuplot


# The files listed in ${pdf_file} are the dependencies for the target ${png_file}.

png_src_file = Eulers_formula_animation_slides-0.png


Makefile : ${abs_srcdir}/Makefile.in ../config.status

	../config.status $@


../config.status : ${abs_srcdir}/../configure

	../config.status -recheck


all : png


png : png_animationFrames_1 \
	  png_animationFrames_2


# png : slide_frames_png \
# 	  animation_stage1_frames_png \
# 	  animation_stage2_frames_png

# gimp    --verbose \
#         --no-interface \
#         --console-messages \
#         --batch-interpreter="plug-in-script-fu-eval" \
#         --batch '(python-fu-scale-and-set-size-noninteractive RUN-NONINTERACTIVE 1920 1080 3 "fileList.txt")' \
#         --batch "(gimp-quit 1)"


png_animationFrames_1 : Eulers_formula.gp

	${MAKE} -f Makefile_AnimationFrames_1 animation_frames_1


png_animationFrames_2 : Eulers_formula.gp

	${MAKE} -f Makefile_AnimationFrames_2 png_animationFrames_2


.PHONY          : stage2_animation_png
stage2_animation_png : animation_stage1_frames_generate_png \
					   animation_stage1_frames_scale_vertically_png \
					   animation_stage1_frames_scale_and_set_size_png

	@printf "========================================\n"
	@printf "========================================\n"
	@printf "<frameSetCreated>                       \n"
	@printf "Stage 1 frames have been created.       \n"
	@printf "</frameSetCreated>                      \n"
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Waiting for 1 minute before proceeding. \n"
	@python ${abs_srcdir}/../python/DisplayTimerTicks.py


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


# Not sure what to do with the following targets.

.PHONY          : animation_stage1_frames_scale_vertically_png
animation_stage1_frames_scale_vertically_png :




.PHONY          : animation_stage1_frames_scale_and_set_size_png
animation_stage1_frames_scale_and_set_size_png :

	gimp --no-interface \
		 --verbose \
		 --console-messages \
		 --batch-interpreter="plug-in-script-fu-eval" \
		 --batch '(python-fu-scale-and-set-size-noninteractive RUN-NONINTERACTIVE 1920 1080 "fileList.txt")' \
		 --batch "(gimp-quit 1)"


.PHONY : runGimpInBatchMode
runGimpInBatchMode :

	gimp -idf \
	     --batch-interpreter python-fu-eval \
	     -b 'import sys; sys.path = ["/home/craig/local/source/gimp/plug-ins"] + sys.path; from scaleAndSetSize import scale_and_set_size_noninteractive; scale_and_set_size_noninteractive("1920", "1080", 3, "./fileList.txt")' \
	     -b "pdb.gimp_quit(1)"


silly_target :

	${PYTHON}  ${srcdir}/../python/createFrames.py \
				--nextFrameNumber      "1" \
				--nfnFile              "nfn_png_slideFrames_1.txt" \
				--sourceDirectory      ${abs_srcdir} \
				--buildDirectory       ${abs_builddir} \
				--frameRate            ${FRAME_RATE_ANIMATION} \
				--resolution           ${RESOLUTION_ANIMATION} \
				--aspectRatio          "16:9" \
				--gnuplot              ${GNUPLOT} \
				--outputDirectory      ${abs_builddir}/png/ \
				--slidesDirectory      ${abs_builddir}/../slides/png/ \
				--gnuplotCodeDirectory ${abs_srcdir}/../gnuplot/ \
				--generateSlideFrames  "true"


.PHONY : pauseUsingBash
pauseUsingBash :

	@printf "About to pause for 1 minute ...\n"
	@{ \
		set -e ; \
		declare -i timer=0 ; \
		while [ $${timer} -lt 60 ] ; \
		do \
			sleep 1 ; \
			printf "." ; \
			timer=timer+1 ; \
		done ;\
		printf "\n" ; \
	}


.PHONY : pauseUsingPython
pauseUsingPython :

	@python ${abs_srcdir}/../python/DisplayTimerTicks.py
