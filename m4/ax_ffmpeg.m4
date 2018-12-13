AC_DEFUN(

  [AX_FFMPEG],

  [
	AC_ARG_WITH(

	  [ffmpeg],
	  [AS_HELP_STRING(

		  [--with-ffmpeg=@<:@ARG@:>@],
		  [Instruct the Build process to use the instance of ffmpeg which is installed at @<:@ARG@:>@. Note that the value which is specified, will not be tested to see if it actually exists.]
		)
	  ],
	  [FFMPEG=${withval}],
	  [FFMPEG=""]
	)

	AS_CASE(

	  [${withval}],
	  [yes], [AC_CHECK_PROG([FFMPEG], [ffmpeg], [ffmpeg], [""])],
	  [no],  [AC_MSG_NOTICE([Variable FFMPEG has not been set.])],
	  [FFMPEG="${withval}"]
	)

	AC_SUBST(FFMPEG)
  ]
)
