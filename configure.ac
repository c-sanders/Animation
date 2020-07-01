AC_INIT([Eulers_formula_animation], [0.1], [craig@gravitas-toolworks.com])
AC_CONFIG_SRCDIR([python/AnimationGenerator.py])
AM_INIT_AUTOMAKE
LT_INIT

m4_include([m4/ax_gimp_plugin.m4])
m4_include([m4/ax_python.m4])
m4_include([m4/ax_gnuplot.m4])
m4_include([m4/ax_ffmpeg.m4])
m4_include([m4/ax_colour_profile.m4])
m4_include([m4/ax_animation_settings.m4])

AC_CONFIG_MACRO_DIR([m4])

AX_GIMP_PLUGIN_SET_IMAGE_COLOUR_PROFILE()
AX_PYTHON()
AX_GNUPLOT()
AX_FFMPEG()
AX_COLOUR_PROFILE([/usr/share/color/icc/colord/sRGB.icc])
AX_FRAME_RATE_ANIMATION
AX_RESOLUTION_ANIMATION

AC_MSG_NOTICE([PYTHON        = \"${PYTHON}\"])
AC_MSG_NOTICE([PYTHON_BIN    = \"${PYTHON_BIN}\"])
AC_MSG_NOTICE([GNUPLOT       = \"${GNUPLOT}\"])
AC_MSG_NOTICE([FFMPEG        = \"${FFMPEG}\"])
AC_MSG_NOTICE([COLOURPROFILE = \"${COLOURPROFILE}\"])

# AC_MSG_NOTICE([About to check whether gnuplot resides within PATH])
# AC_CHECK_PROG([FFMPEG], [ffmpeg], [yes], [no])

# AM_CONDITIONAL([TEST_RESULT], [test "x${FFMPEG}" = "x"])
# AC_MSG_NOTICE([TEST_RESULT = ${TEST_RESULT}])
# AM_COND_IF(
#
#   [TEST_RESULT],
#   [
# 	AC_MSG_NOTICE([A value wasn't specified for --with-ffmpeg])
# 	AC_MSG_NOTICE([About to check whether ffmpeg resides within PATH])
#
# 	AC_CHECK_PROG(
#
# 	  [FFMPEG],
# 	  [ffmpeg],
# 	  [yes],
# 	  [no]
# 	)
#   ]
# )

dnl AC_MSG_CHECKING([whether ffmpeg resides within PATH])
dnl AC_MSG_RESULT([yes])

dnl AS_IF([test "x${FFMPEG}" = "xyes"],

dnl		  AC_MSG_ERROR["Could not find ffmpeg in PATH])

AC_PROG_MKDIR_P([slides/temp \
                 slides/pdf \
                 frames/png/animation_1 \
                 frames/png/animation_2])

AC_OUTPUT([runConfigure.sh \
           Makefile \
           message_b.txt \
           testScript.sh \
           slides/Makefile \
           slides/temp/Makefile \
           slides/pdf/Makefile \
           slides/png/Makefile \
           python/LaTeXGenerator.py \
           python/FilenameFormatter.py \
           gnuplot/Eulers_formula.gp \
           gnuplot/Eulers_formula_2.gp \
           frames/Makefile \
           frames/png/Makefile \
           frames/png/animation_1/Makefile \
           frames/png/animation_1/Makefile_generate \
           frames/png/animation_1/Makefile_process \
           frames/png/animation_1/Makefile_set_colour_profile \
           frames/png/animation_1/Makefile_set_image_mode \
           frames/png/animation_1/Makefile_overlay \
           frames/png/animation_1/Makefile_messages \
           frames/png/animation_2/Makefile \
           videos/Makefile \
           videos/Makefile_play_animation])

# Autoconf complains that slides/png/Makefile is already registered with AC_CONFIG_FILES

# AC_OUTPUT([slides/png/Makefile])
