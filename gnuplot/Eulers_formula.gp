# ==============================================================================
# Filename : Eulers_formula.gp
# ============================
#
# Purpose
# -------
#
# This file implements a script for the gnuplot language.
#
# Description
# -----------
#
# When executed, this script should generate a 3-D plot of Euler's formula along
# with its 2 components.
#
# Operation
# ---------
#
# The script operates in one of the following two modes ;
#
#   - Plot the 2 components and their resulting summation.
#
#   - Don't plot the 2 components, but plot their resulting summation.
#
# Environment variables
# ---------------------
#
# This script requires that a number of environment variables are set and then
# passed to it on the command line, before it can execute correctly.
#
# These environment variables are ;
#
#   - filename
#   - plotAll
#   - maxIteration
#   - index
#   - view_x
#   - view_y
#   - title
#
# filename :
#
# The name of the file which the resulting 3-D plot should be saved into.
#
# plotAll :
#
# Whether or not to plot both the 2 components and their resulting summation.
#
# maxIteration :
#
# The maximum number of impulses that should be rendered in the plot.
#
#


reset

# Set the title and various labels for the plot.
# ----------------------------------------------

# Uncomment the following line(s) if the generated output is be used by X11.

# set terminal x11
set terminal pngcairo size 1920,1080
set output   filename
set print    "-"

# Uncomment the following line(s) if the generated output is be used by LaTeX.

# set terminal latex
# set output 'Eulers_formula.tex'

# set title "3D visual representation of e^{i{/Symbol q}} = cos({/Symbol q}) + jsin({/Symbol q})"
# set title maxIteration
set title myTitle

set xlabel "x : {/Symbol q} (Radians)"
set ylabel "y : Im"
set zlabel "z : Re"

# Setup the plot parameters.
# --------------------------

set view view_x, view_y

# set num_points maxIteration

set parametric

set xrange [0:4*pi]
set yrange [-2:2]
set zrange [-2:2]

set grid xtics lt 0 lw 2 lc rgb "#AAAAAA"
set grid ytics lt 0 lw 2 lc rgb "#AAAAAA"
set grid ztics lt 0 lw 2 lc rgb "#AAAAAA"

show grid

# Don't raise the plot.

set ticslevel 0

# Define the function which is to be plotted.


# set hidden3d
set isosamples 20,20

set arrow from 0,0,0  to 4*pi,0,0
set arrow from 0,-2,0 to 0,2,0
set arrow from 0,0,-2 to 0,0,2

# Two parameters (u, v) are enough to represent any 3D surface.
#
# splot parameter u is associated with the x-axis.
# splot parameter v is not associated with any axis.

# with impulses     : This will only draws lines vertically.
# with filledcurves : This will only draws lines vertically.

# splot \
# \
# u, 0,       cos(u)           linecolor "red"     notitle with impulses, \
# u, sin(u),  0                linecolor "blue"    notitle, \
# u, sin(u),  cos(u)           linecolor "green"   notitle

# u, 0,              exp(-u)          linecolor "magenta" title 'e^-u', \
# u, -0.707*sin(u),  exp(-u) * cos(u) linecolor "cyan"    title 'e^-u(cos(u) - jsin(u))'

# set samples 200
set samples maxIteration

# Column 1 : x coordinate (Whether or not the plot moves laterally wrt the x-axis depends on Column 2 and 3 values.)
# Column 2 : y coordinate (Whether or not the plot moves laterally wrt the y-axis depends on Column 1 and 3 values.)
# Column 3 : z coordinate (Whether or not the plot moves laterally wrt the z-axis depends on Column 1 and 2 values.)

# unset key

# num_points        = 200
plot_inc          = (4 * pi) / maxIteration
# max_plot_index    = index
max_plot_distance = index * plot_inc

print ">>>>>"
# print "num_points     = ", num_points
print "plot_inc       = ", plot_inc
# print "max_plot_index = ", max_plot_index
print "view_x         = ", view_x
print "view_y         = ", view_y
print "filename       = ", filename
print "maxIteration   = ", maxIteration
print "myTitle        = ", myTitle
print "plotAll        = ", plotAll
print "<<<<<"

# for [max_plot_index = 0:num_points] \
# \

set urange [0:max_plot_distance]

set label 1 "Notice that when viewed end on, the green plot appears as a circle." at -10,-5,150 center

if (plotAll != 0) \
	\
	set \
	\
	for [x_new = 0:index] \
	\
	arrow from (x_new * plot_inc),0,0 to (x_new * plot_inc),0,cos(x_new * plot_inc) linecolor "red"   nohead

if (plotAll != 0) \
	\
	set \
	\
	for [x_new = 0:index] \
	\
	arrow from (x_new * plot_inc),0,0 to (x_new * plot_inc),sin(x_new * plot_inc),0 linecolor "blue"  nohead

set \
\
for [x_new = 0:index] \
\
arrow from (x_new * plot_inc),0,0 to (x_new * plot_inc),sin(x_new * plot_inc),cos(x_new * plot_inc) linecolor "green" nohead

if (plotAll != 0) \
	\
	splot \
	\
	u, 0,      cos(u) linecolor "red"   linewidth 0.5 notitle, \
	u, sin(u), 0      linecolor "blue"  linewidth 0.5 notitle, \
	u, sin(u), cos(u) linecolor "green" linewidth 0.5 notitle; \
else \
	\
	splot \
	\
	u, sin(u), cos(u) linecolor "green" linewidth 0.5 notitle


# Pause indefinately until the user presses the Enter key.

# pause -1 "Please press Enter to continue..."
