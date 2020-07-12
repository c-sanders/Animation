# ==================================================================================================
# Filename : ./slides/pdf/Makefile
# --------------------------------
#
# - Create the PDF file from the LaTeX files.
#
# ==================================================================================================
#
# Notes 
#
# 1) The pdf rule should execute latex from within the following directory;
#
#      ${abs_srcdir}/../latex directory.
#
#    If it doesn't, then the TeX files which are listed in ${tex_files}, won't be incorporated into
#    the resulting pdf output file.
#
# ==================================================================================================
#
# TeX settings.
#
# /usr/share/texmf/tex/latex/beamer/beamer.cls  : Version 3.06
#
# ==================================================================================================


SUBDIRS    =

EXTRA_DIST =

CLEANFILES = *.aux \
             *.log \
             *.nav \
             *.out \
             *.pdf \
             *.snm \
             *.toc \
             latex_iterations.txt


tex_main_file     = ${abs_srcdir}/../latex/Eulers_formula_animation_slides.tex

tex_slide_files   = ${tex_main_file} \
                    ${abs_srcdir}/../latex/Slide_1.tex  \
                    ${abs_srcdir}/../latex/Slide_2.tex  \
                    ${abs_srcdir}/../latex/Slide_3.tex  \
                    ${abs_srcdir}/../latex/Slide_4.tex  \
                    ${abs_srcdir}/../latex/Slide_7.tex  \
                    ${abs_srcdir}/../latex/Slide_8.tex  \
                    ${abs_srcdir}/../latex/Slide_9.tex  \
                    ${abs_srcdir}/../latex/Slide_10.tex \
                    ${abs_srcdir}/../latex/Slide_11.tex \
                    ${abs_srcdir}/../latex/Slide_12.tex

image_slide_files = ${abs_srcdir}/../latex/images/png/Leonhard_Euler.png

tex_files         = ${abs_srcdir}/../latex/${tex_main_file}   \
                    ${tex_slide_files} \
                    ${image_slide_files}

pdf_file          = Eulers_formula_animation_slides.pdf


all             : pdf


# Refer to note 1 above.

pdf             : ${pdf_file}
${pdf_file}     : ${tex_files}

	@printf "================================================================================\n"
	@printf "================================================================================\n"
	@printf "Makefile : ./slides/pdf/Makefile                                                \n"
	@printf "Target   : pdf                                                                  \n"
	@printf "Status   : Enter                                                                \n"
	@printf "================================================================================\n"
	@printf "================================================================================\n"
	@printf "Deps A = $@                                                                     \n"
	echo "0" > latex_iterations.txt
	@printf "Current directory = %s                                                          \n" ${PWD}
	@printf "abs_srcdir = ${abs_srcdir}                                                      \n"
	@printf "================================================================================\n"
	@printf "================================================================================\n"
	@printf "Running latex for the 1st time          \n"
	@printf "========================================\n"
	@printf "========================================\n"
	cd ${abs_srcdir}/../latex && latex -halt-on-error -output-format=pdf -output-directory ${abs_builddir} ${tex_main_file}
	echo "1" > latex_iterations.txt
	@printf "================================================================================\n"
	@printf "================================================================================\n"
	@printf "Running latex for the 2nd time                                                  \n"
	@printf "                                                                                \n"
	@printf "This is being done to correct the cross-references of any labels which may have \n"
	@printf "changed.                                                                        \n"
	@printf "================================================================================\n"
	@printf "================================================================================\n"
	cd ${abs_srcdir}/../latex && latex -halt-on-error -output-format=pdf -output-directory ${abs_builddir} ${tex_main_file}
	@printf "mv -v ${pdf_file} $@\n"
	echo "2" > latex_iterations.txt
	@printf "================================================================================\n"
	@printf "================================================================================\n"
	@printf "Makefile : ./slides/pdf/Makefile                                                \n"
	@printf "Target   : pdf                                                                  \n"
	@printf "Status   : Exit                                                                 \n"
	@printf "================================================================================\n"
	@printf "================================================================================\n"


displaySettings :

	${MAKE} -f ./Makefile_displaySettings

