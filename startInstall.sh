#! /bin/bash


CURRENT_DIR="$(pwd)"
DIRNAME="$(dirname $0)"
FILENAME="$(basename $0)"

PYTHON_DIR="${CURRENT_DIR}/${DIRNAME}/python"
PYTHON_FILE="${PYTHON_DIR}/startInstall.py"

echo "Current dir = $CURRENT_DIR"
echo "Python dir  = $PYTHON_DIR"
echo "Python file = $PYTHON_FILE"
echo "Arg 0       = $0"
echo "Filename    = ${FILENAME}"
echo "Dirname     = ${DIRNAME}"

# We don't necessarily want to export the PYTHONPATH environment variable which is set in the
# command below. The reason for this is because the calling environment might already have it set
# the way it wants.
#
# Therefore, use the BASH set command line utility to just set the PYTHONPATH it locally for this
# command.

set PYTHONPATH=${PYTHON_DIR} ; python3 ${PYTHON_FILE}


exit 0
