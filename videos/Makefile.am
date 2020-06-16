# vpath %.png ../slides/png/


video_filename             = Eulers_formula_presentation.mp4

slide_set_1_video_filename = Eulers_formula_slide_set_1.mp4

animation_1_video_filename = Eulers_formula_animation_1.mp4


# The make utility will be able to determine the location within which the following files should
# reside.
#
# It does this by referring to the appropriate (%.png) vpath directive above.

# Note that the full relative path and filename is specified for each of the following files. If
# however, just the filename was specified, then an appropriate vpath directive would need to be set
# above in order to tell the make utility where to find the files.

slide_set_1_files          = ../slides/png/Eulers_formula_animation_slides-000000.png \
                             ../slides/png/Eulers_formula_animation_slides-000001.png \
                             ../slides/png/Eulers_formula_animation_slides-000002.png \
                             ../slides/png/Eulers_formula_animation_slides-000003.png \
                             ../slides/png/Eulers_formula_animation_slides-000004.png

animation_1_files          = ../frames/png/animation_1/Eulers_formula_000001.png


all : slide_set_1 \
      animation_1 \
      final


slide_set_1                   : ${slide_set_1_video_filename}
${slide_set_1_video_filename} : ${slide_set_1_files}

	${FFMPEG} \
	\
	-y \
	-f concat \
	-safe 0 \
	-i ${abs_builddir}/fileList_slide_set_1.txt \
	-aspect "16:9" \
	-pix_fmt yuv444p \
	$@


# Rule : animation_1
# ==================
#
# Note 1
#
# -r ${FRAME_RATE_ANIMATION}

animation_1                   : ${animation_1_video_filename}
${animation_1_video_filename} : ${animation_1_files}

	${FFMPEG} \
	\
	-y \
	-r 5 \
	-s ${RESOLUTION_ANIMATION} \
	-i "${abs_builddir}/../frames/png/animation_1/Eulers_formula_%06d.png" \
	-aspect "16:9" \
	-pix_fmt yuv444p \
	$@


final :

	${FFMPEG} \
	\
	-y \
	-f concat \
	-safe 0 \
	-i fileList_final.txt \
	-c copy \
	${video_filename}


# Rule : Pattern rule - Slides png
# ================================
#
# Note 2

../slides/png/%.png :

	@echo "Rule : %.png : %.pdf :"
	@echo "Rule target     = $@"
	@echo ""
	${MAKE} -C ../slides


# Rule : Pattern rule - Frames png
# ================================
#
# Note 2

../frames/png/%.png :

	${MAKE} -C ../frames


# ${slide_set_1_file} :
#
#	${MAKE} -C ../slides


.PHONY: displaySettings
displaySettings:

	@echo "video_filename             = ${video_filename}"
	@echo "slide_set_1_file           = ${slide_set_1_file}"
	@echo "slide_set_1_files          = ${slide_set_1_files}"
	@echo "slide_set_1_video_filename = ${slide_set_1_video_filename}"
	@echo "animation_1_files          = ${animation_1_files}"
	@echo "animation_1_video_filenme  = ${animation_1_video_filename}"
	@echo "MAKE                       = ${MAKE}"
	@echo "MAKE                       = @MAKE@"
	@echo "srcdir                     = ${srcdir}"
	@echo "abs_builddir               = ${abs_builddir}"
	@echo "builddir                   = ${builddir}"
	@echo "FFMPEG                     = ${FFMPEG}"
	@echo "GNUPLOT                    = ${GNUPLOT}"
	@echo "FRAME_RATE_ANIMATION       = ${FRAME_RATE_ANIMATION}"
	@echo "RESOLUTION_ANIMATION       = ${RESOLUTION_ANIMATION}"

