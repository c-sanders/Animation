# -----------------------------------------------------------------------------
# Macro : AX_COLOUR_PROFILE
# =========================
#
# This macro can be used to inform the Autotools about the Colour Profile file
# which should be used by GIMP.
# -----------------------------------------------------------------------------


AC_DEFUN(

  [AX_COLOUR_PROFILE],

  [
	AC_ARG_WITH(

	  [colour_profile],
	  [
		AS_HELP_STRING(

		  [--with-colour_profile=@<:@ARG@:>@],
		  [Instruct the Build process to use the Colour Profile which is stored in the file @<:@ARG@:>@. Note that the argument which is specified, will not be tested to see if it actually exists. @<:@default=$1@:>@]
		)
	  ],
	  [COLOURPROFILE=${withval}],
	  [COLOURPROFILE=""]
	)

	AS_CASE(

	  [${withval}],
	  [yes], [COLOURPROFILE=$1],
	  [no],  [COLOURPROFILE=""],
	  [COLOURPROFILE="${withval}"]
	)

	AC_SUBST(COLOURPROFILE)
  ]
)
