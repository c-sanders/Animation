# The following Environment variables are used by this Makefile but should be
# set externally by the Autoconf configure script ;
#
#   - FRAME_RATE_ANIMATION   = "25"
#   - RESOLUTION_ANIMATION   = "1920x1080"
#   - ASPECT_RATIO_ANIMATION = "16:9"


SUBDIRS = pdf png


all    : slides


slides :

	${MAKE} -C ./png png


.PHONY : displaySettings
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
