AC_DEFUN(

  [AX_FRAME_RATE_ANIMATION],

  [
	AC_ARG_WITH(

	  [frame_rate_animation],
	  [AS_HELP_STRING(

		  [--with-frame_rate_animation=@<:@ARG@:>@],
		  [Set the Frame rate for the animation to @<:@ARG@:>@ frames per second (fps).]
		)
	  ],
	  [FRAME_RATE_ANIMATION=${withval}],
	  [FRAME_RATE_ANIMATION=""]
	)

	AC_SUBST(FRAME_RATE_ANIMATION)
  ]
)


AC_DEFUN(

  [AX_RESOLUTION_ANIMATION],

  [
	AC_ARG_WITH(

	  [resolution_animation],
	  [AS_HELP_STRING(

		  [--with-resolution_animation=@<:@ARG@:>@],
		  [Set the Resolution for the animation to @<:@ARG@:>@.]
		)
	  ],
	  [RESOLUTION_ANIMATION=${withval}],
	  [RESOLUTION_ANIMATION=""]
	)

	AC_SUBST(RESOLUTION_ANIMATION)
  ]
)
