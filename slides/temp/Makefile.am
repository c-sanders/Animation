# Virtual paths informing make where it can find files of particular types.

vpath %.tex ${abs_srcdir}/../latex/
vpath %.png ${abs_srcdir}/../latex/images/png/


# Directories and files.

tex_main_file           = Eulers_formula_animation_slides.tex
pdf_file                = Eulers_formula_animation_slides.pdf

tex_slide_files         = Slide_1.tex  \
                          Slide_2.tex  \
                          Slide_3.tex  \
                          Slide_4.tex  \
                          Slide_7.tex  \
                          Slide_8.tex  \
                          Slide_9.tex  \
                          Slide_10.tex \
                          Slide_11.tex

image_slide_files       = Leonhard_Euler.png

tex_files               = ${tex_main_file}   \
                          ${tex_slide_files} \
                          ${image_slide_files}


# Build targets.

all         : ../pdf/${pdf_file}


# The following rule should execute latex from within the ${abs_srcdir}/../latex directory. If it
# doesn't, then the TeX files which are listed in ${tex_slide_files}, won't be incorporated into the
# resulting output.

../pdf/${pdf_file} : ${tex_files}

	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : ${abs_builddir}/Makefile     \n"
	@printf "Target   : ../pdf/${pdf_file}           \n"
	@printf "Status   : Enter                        \n"
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Deps A = $@                             \n"
	echo "0" > latex_iterations.txt
	@printf "Current directory = %s                  \n" ${PWD}
	@printf "abs_srcdir = ${abs_srcdir}              \n"
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Running latex for the 1st time          \n"
	@printf "========================================\n"
	@printf "========================================\n"
	cd ${abs_srcdir}/../latex && latex -halt-on-error -output-format=pdf -output-directory ${abs_builddir} $<
	echo "1" > latex_iterations.txt
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Running pdflatex for the 2nd time       \n"
	@printf "                                        \n"
	@printf "This is to get the cross-references     \n"
	@printf "right for any labels which may have     \n"
	@printf "changed.                                \n"
	@printf "========================================\n"
	@printf "========================================\n"
	cd ${abs_srcdir}/../latex && latex -halt-on-error -output-format=pdf -output-directory ${abs_builddir} $<
	mv -v ${pdf_file} $@
	echo "2" > latex_iterations.txt
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : ${abs_builddir}/Makefile     \n"
	@printf "Target   : ../pdf/${pdf_file}           \n"
	@printf "Status   : Exit                        \n"
	@printf "========================================\n"
	@printf "========================================\n"


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
