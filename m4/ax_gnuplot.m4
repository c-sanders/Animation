# -----------------------------------------------------------------------------
# Macro : AX_GNUPLOT
# ==================
#
# This macro can be used to inform the Autotools about the gnuplot program.
# -----------------------------------------------------------------------------


AC_DEFUN(

  [AX_GNUPLOT],

  [
	AC_ARG_WITH(

	  [gnuplot],
	  [
		AS_HELP_STRING(

		  [--with-gnuplot=@<:@ARG@:>@],
		  [Instruct the Build process to use the instance of gnuplot which is installed at @<:@ARG@:>@. Note that the value which is specified, will not be tested to see if it actually exists.]
		)
	  ],
	  [GNUPLOT=${withval}],
	  [GNUPLOT=""]
	)

	AS_CASE(

	  [${withval}],
	  [yes], [GNUPLOT="gnuplot"],
	  [no],  [GNUPLOT=""],
	  [GNUPLOT="${withval}"]
	)

	AC_SUBST(GNUPLOT)
  ]
)
