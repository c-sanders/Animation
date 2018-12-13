vpath %.png ../png


# The files listed in ${pdf_file} are the dependencies for the target ${png_file}.

frame_files     = "../frames/Eulers_formula_%d.png"

video_file      = Eulers_formula_animation.mp4


all : create_animation display_message


.PHONY : create_animation
create_animation :

	${FFMPEG} \
	\
	-y \
	-r ${FRAME_RATE_ANIMATION} \
	-s ${RESOLUTION_ANIMATION} \
	-i "../frames/png/Eulers_formula_%06d.png" \
	-aspect "16:9" \
	${video_file}


.PHONY : play_animation
play_animation :
	xine \
	\
	--no-splash \
	--no-logo \
	file:///home/craig/local/build/Eulers_formula/videos/Eulers_formula_animation.mp4


.PHONY : display_message
display_message :

	@echo "================================================================================"
	@echo "To play the animation with xine (/home/craig/local/xine-ui-0.99.9/bin/xine), use"
	@echo "a command similar to the following;                                             "
	@echo "                                                                                "
	@echo "   xine \                                                                       "
	@echo "     --no-splash \                                                              "
	@echo "     --no-logo \                                                                "
	@echo "     file://home/craig/local/Eulers_formula_animation/video/Eulers_formula_animation.mp4"
	@echo "                                                                                "
	@echo "To play the animation with mplayer (/usr/local/bin/mplayer), use a command      "
	@echo "similar to the following;                                                       "
	@echo "                                                                                "
	@echo "   mplayer ./Eulers_formula_animation.mp4                                       "
	@echo "                                                                                "
	@echo "To play the animation with ffplay (/home/craig/local/ffmpeg-3.1.1/bin/ffplay),  "
	@echo "use a command similar to the following;                                         "
	@echo "                                                                                "
	@echo "   ffplay ./Eulers_formula_animation.mp4                                        "
	@echo "================================================================================"


.PHONY : play_animation_using_xine
play_animation_using_xine :

	xine \
	--no-splash \
	--no-logo \
	file:/${abs_builddir}/Eulers_formula_animation.mp4


.PHONY : play_animation_using_ffplay
play_animation_using_ffplay :

	ffplay ./Eulers_formula_animation.mp4
