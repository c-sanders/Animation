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
#   - Copy the 1920 x 1080 PNG files into frames.
#
#   - Create the animation frames.
# ==================================================================================================


# SUBDIRS = png


vpath %.pdf ../slides/pdf


# The files listed in ${pdf_file} are the dependencies for the target ${png_file}.

pdf_file = Eulers_formula_animation_slides.pdf


all : png


png : png_slideFrames_1     \
	  png_animationFrames_1 \
	  png_slideFrames_2     \
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

png_slideFrames_1 : ${pdf_file}

    @printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : /frames/Makefile             \n"
	@printf "Target   : png_slideFrames_1            \n"
	@printf "Status   : Enter                        \n"
	@printf "========================================\n"
	@printf "========================================\n"
	mkdir -p png
	sleep 5
	echo 1 > nfn_png_slideFrames_1.txt
	sleep 5
	gimp -idf \
	     --batch-interpreter python-fu-eval \
		 -b 'import sys; sys.path = ["/home/craig/local/source/gimp/plug-ins"] + sys.path; from scaleAndSetSize import scale_and_set_size_noninteractive; scale_and_set_size_noninteractive("1920", "1080", 3, "./fileList.txt")' \
		 -b "pdb.gimp_quit(1)"
	python  ${srcdir}/../python/createFrames.py \
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
			@printf "========================================\n"
	@printf "========================================\n"
	@printf "<frameSetCreated>                       \n"
	@printf "Section 1 : Slide frames have been created.\n"
	@printf "</frameSetCreated>                      \n"
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Waiting for 1 minute before proceeding. \n"
	@python ${abs_srcdir}/../python/DisplayTimerTicks.py


silly_target :

	python  ${srcdir}/../python/createFrames.py \
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



.PHONY          : png_animationFrames_1
png_animationFrames_1 :

	rm fileList.txt
	sleep 5
	python  ${srcdir}/../python/createFrames.py \
			--nextFrameNumber      $(shell cat nfn_png_slideFrames_1.txt) \
			--nfnFile              "nfn_png_animationFrames_1.txt"
			--sourceDirectory      ${abs_srcdir} \
			--buildDirectory       ${abs_builddir} \
			--frameRate            ${FRAME_RATE_ANIMATION} \
			--resolution           ${RESOLUTION_ANIMATION} \
			--aspectRatio          "16:9" \
			--gnuplot              ${GNUPLOT} \
			--outputDirectory      ${abs_builddir}/png/ \
			--slidesDirectory      ${abs_builddir}/../slides/png/ \
			--gnuplotCodeDirectory ${abs_srcdir}/../gnuplot/ \
			--generateStage1Frames "true"


.PHONY          : animation_stage1_frames_scale_vertically_png
animation_stage1_frames_scale_vertically_png :

	gimp --no-interface \
		 --verbose \
		 --console-messages \
		 --batch-interpreter="plug-in-script-fu-eval" \
		 --batch '(python-fu-scale-vertically-noninteractive RUN-NONINTERACTIVE 1.6 3 "fileList.txt")' \
		 --batch "(gimp-quit 1)"
	gimp --no-interface \
		 --verbose \
		 --console-messages \
		 --batch-interpreter="plug-in-script-fu-eval" \
		 --batch '(python-fu-scale-and-set-size-noninteractive RUN-NONINTERACTIVE 1920 1080 "fileList.txt")' \
		 --batch "(gimp-quit 1)"


.PHONY          : animation_stage1_frames_scale_and_set_size_png
animation_stage1_frames_scale_and_set_size_png :

	gimp --no-interface \
		 --verbose \
		 --console-messages \
		 --batch-interpreter="plug-in-script-fu-eval" \
		 --batch '(python-fu-scale-and-set-size-noninteractive RUN-NONINTERACTIVE 1920 1080 "fileList.txt")' \
		 --batch "(gimp-quit 1)"


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


.PHONY          : animation_stage2_frames_png
animation_stage2_frames_png :

	python  ${srcdir}/../python/createFrames.py \
			--nextFrameNumber      $(shell cat nextFrameNumber.txt) \
			--sourceDirectory      ${abs_srcdir} \
			--buildDirectory       ${abs_builddir} \
			--frameRate            ${FRAME_RATE_ANIMATION} \
			--resolution           ${RESOLUTION_ANIMATION} \
			--aspectRatio          "16:9" \
			--gnuplot              ${GNUPLOT} \
			--outputDirectory      ${abs_builddir}/png/ \
			--slidesDirectory      ${abs_builddir}/../slides/png/ \
			--gnuplotCodeDirectory ${abs_srcdir}/../gnuplot/ \
			--generateStage2Frames "true"
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "<frameSetCreated>                       \n"
	@printf "Stage 2 frames have been created.       \n"
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
