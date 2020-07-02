SUBDIRS         = slides \
                  frames \
                  videos

EXTRA_DIST      = python \
                  gnuplot

ACLOCAL_AMFLAGS = -I m4


all :

	${MAKE} -C videos


slides :

	${MAKE} -C slides


frames :

	${MAKE} -C frames


videos :

	${MAKE} -C videos


.PHONY: displaySettings
displaySettings:

	@echo "tex_main_file         = ${tex_main_file}"
	@echo "pdf_file              = ${pdf_file}"
	@echo "tex_slide_files       = ${tex_slide_files}"
	@echo "image_slide_files     = ${image_slide_files}"
	@echo "tex_files             = ${tex_files}"
	@echo ""
	@echo "MAKE                  = ${MAKE}"
	@echo "MAKE                  = @MAKE@"
	@echo "srcdir                = ${srcdir}"
	@echo "abs_srcdir            = ${abs_srcdir}"
	@echo "builddir              = ${builddir}"
	@echo "abs_builddir          = ${abs_builddir}"
	@echo "FFMPEG                = ${FFMPEG}"
	@echo "GNUPLOT               = ${GNUPLOT}"
	@echo "FRAME_RATE_ANIMATION  = ${FRAME_RATE_ANIMATION}"
	@echo "RESOLUTION_ANIMATION  = ${RESOLUTION_ANIMATION}"
