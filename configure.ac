AC_INIT([Eulers_formula_animation], [0.1], [craig@gravitas-toolworks.com])
AC_CONFIG_SRCDIR([python/AnimationGenerator.py])
AM_INIT_AUTOMAKE
LT_INIT

m4_include([m4/ax_ffmpeg.m4])
m4_include([m4/ax_gnuplot.m4])
m4_include([m4/ax_animation_settings.m4])

AC_CONFIG_MACRO_DIR([m4])

AX_FFMPEG()
AX_GNUPLOT()
AX_FRAME_RATE_ANIMATION
AX_RESOLUTION_ANIMATION

AC_MSG_NOTICE([FFMPEG  = \"${FFMPEG}\"])
AC_MSG_NOTICE([GNUPLOT = \"${GNUPLOT}\"])

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

AC_PROG_MKDIR_P([frames/png \
				 frames/jpg \
				 frames/gif])

AC_CONFIG_FILES([Makefile \
				 slides/Makefile \
				 slides/latex/Makefile \
				 slides/png/Makefile \
				 frames/Makefile \
				 videos/Makefile])

# Autoconf complains that slides/png/Makefile is already registered with AC_CONFIG_FILES

# AC_OUTPUT([slides/png/Makefile])
