SUBDIRS    = pdf \
             png

EXTRA_DIST = latex


all             :


# The slides target is no longer required anymore as make will recurse into the two sub-dirs which
# are listed above.

slides          :

	${MAKE} -C ./png


displaySettings :

	${MAKE} -f Makefile_displaySettings
