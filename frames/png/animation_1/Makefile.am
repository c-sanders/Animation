# Filename : frames/png/animation_1/Makefile.am
# =============================================


CLEANFILES   = *.png


# Makefile_AnimationFrames_1 : ${abs_srcdir}/Makefile_AnimationFrames_1.in ../config.status

#	../config.status $@


../config.status : ${abs_srcdir}/../configure

	../config.status -recheck


all : generate \
      process \
      overlay


# Targets : generate

generate : pre_generate \
           actual_generate \
           post_generate


pre_generate :

	${MAKE} -f Makefile_messages pre_generate


actual_generate :

	${MAKE} -f Makefile_generate


post_generate :

	${MAKE} -f Makefile_messages post_generate


# Targets : process

process : pre_process \
          actual_process \
          post_process


pre_process :

	${MAKE} -f Makefile_messages pre_process


actual_process  :

	${MAKE} -f Makefile_process


post_process :

	${MAKE} -f Makefile_messages post_process


# Targets : overlay

overlay : pre_overlay \
          actual_overlay \
          post_overlay


pre_overlay :

	${MAKE} -f Makefile_messages pre_overlay


actual_overlay  :

	${MAKE} -f Makefile_overlay


post_overlay :

	${MAKE} -f Makefile_messages post_overlay


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
