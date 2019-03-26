# The following Environment variables are used by this Makefile but should be
# set externally by the Autoconf configure script ;
#
#   - FRAME_RATE_ANIMATION   = "25"
#   - RESOLUTION_ANIMATION   = "1920x1080"
#   - ASPECT_RATIO_ANIMATION = "16:9"
#
# ------------------------------------------------------------------------------
#
# TeX settings.
#
# /usr/share/texmf/tex/latex/beamer/beamer.cls  : Version 3.06


vpath %.tex ${srcdir}/../latex
vpath %.pdf ${abs_builddir}


tex_main_file   = Eulers_formula_animation_slides.tex

tex_slide_files = Slide_1.tex  \
				  Slide_2.tex  \
				  Slide_3.tex  \
				  Slide_4.tex  \
				  Slide_7.tex  \
				  Slide_8.tex  \
				  Slide_9.tex  \
				  Slide_10.tex \
				  Slide_11.tex

# The files listed in ${tex_files} are the dependencies for the target ${pdf_file}.

tex_files       = ${tex_main_file} ${tex_slide_files}

pdf_file        = ./Eulers_formula_animation_slides.pdf


all         : ${pdf_file}
${pdf_file} : ${tex_files}

	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : /pdf/Makefile                \n"
	@printf "Target   : pdf_file                     \n"
	@printf "Status   : Enter                        \n"
	@printf "========================================\n"
	@printf "========================================\n"
	@printf ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
	@printf "Running pdflatex for the 1st time       \n"
	@printf "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
	cd ${srcdir}/../latex && \
	pdflatex -output-directory ${abs_builddir} ${tex_main_file} 
	@printf ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
	@printf "Running pdflatex for the 2nd time       \n"
	@printf "                                        \n"
	@printf "This is to get the cross-references     \n"
	@printf "right for any labels which may have     \n"
	@printf "changed.                                \n"
	@printf "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
	cd ${srcdir}/../latex && \
	pdflatex -output-directory ${abs_builddir} ${tex_main_file}
	@printf "========================================\n"
	@printf "========================================\n"
	@printf "Makefile : /pdf/Makefile                \n"
	@printf "Target   : pdf_file                     \n"
	@printf "Status   : Exit                         \n"
	@printf "========================================\n"
	@printf "========================================\n"


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
