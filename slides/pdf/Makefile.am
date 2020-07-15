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
# 1) The run_latex_1 and run_latex_2 rules should execute latex from within the following directory;
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

SUBDIRS           =

EXTRA_DIST        =

CLEANFILES        = *.aux \
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

tex_files         = ${tex_slide_files} \
                    ${image_slide_files}

pdf_file          = ./Eulers_formula_animation_slides.pdf


all             : pdf


pdf             : ${pdf_file}
${pdf_file}     : ${tex_files}

	${MAKE} generate_pdf


generate_pdf    : pre_latex_1 \
                  run_latex_1 \
                  messages_pre_2 \
                  run_latex_2 \
                  messages_post


pre_latex_1     : messages_pre_1

	echo "0" > latex_iterations.txt


messages_pre_1  :

	${MAKE} -f ./Makefile_messages pre_1a
	@printf "Deps A = $@                                                                     \n"
	${MAKE} -f ./Makefile_messages pre_1b


messages_pre_2  :

	${MAKE} -f ./Makefile_messages pre_2


messages_post   :

	${MAKE} -f ./Makefile_messages post


# Refer to Note 1 at the top of this file.

run_latex_1     : ${tex_files}

	cd ${abs_srcdir}/../latex && \
	latex -halt-on-error -output-format=pdf -output-directory ${abs_builddir} ${tex_main_file}
	echo "1" > latex_iterations.txt


# Refer to Note 1 at the top of this file.

run_latex_2     :

	cd ${abs_srcdir}/../latex && \
	latex -halt-on-error -output-format=pdf -output-directory ${abs_builddir} ${tex_main_file}
	echo "2" > latex_iterations.txt


displaySettings :

	${MAKE} -f ./Makefile_displaySettings

