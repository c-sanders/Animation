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

tex_files       = ${tex_main_file} ${tex_slide_files}


all : 

	echo "0" > latex_iterations.txt
	@printf ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
	@printf "Running pdflatex for the 1st time       \n"
	@printf "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
	pdflatex -output-directory ${abs_builddir}/../pdf/ ${tex_main_file} 
	echo "1" > latex_iterations.txt
	@printf ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
	@printf "Running pdflatex for the 2nd time       \n"
	@printf "                                        \n"
	@printf "This is to get the cross-references     \n"
	@printf "right for any labels which may have     \n"
	@printf "changed.                                \n"
	@printf "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
	pdflatex -output-directory ${abs_builddir}/../pdf/ ${tex_main_file}
	echo "2" > latex_iterations.txt
