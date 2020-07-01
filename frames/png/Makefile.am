SUBDIRS = animation_1 \
          animation_2


vpath %.gp  ../../gnuplot


all : png_animationFrames_1


png_animationFrames_1 : Eulers_formula.gp

	${MAKE} -C ./animation_1


png_animationFrames_2 : Eulers_formula.gp

	${MAKE} -C ./animation_2


.PHONY: displaySettings
displaySettings:

	@echo "srcdir               = ${srcdir}"
	@echo "abs_srcddir          = ${abs_srcdir}"
	@echo "builddir             = ${builddir}"
	@echo "abs_builddir         = ${abs_builddir}"
	@echo "FFMPEG               = ${FFMPEG}"
	@echo "GNUPLOT              = ${GNUPLOT}"
	@echo "FRAME_RATE_ANIMATION = ${FRAME_RATE_ANIMATION}"
	@echo "RESOLUTION_ANIMATION = ${RESOLUTION_ANIMATION}"
	@echo ""
	@echo "tex_files            = ${tex_files}"
	@echo "pdf_file             = ${pdf_file}"
