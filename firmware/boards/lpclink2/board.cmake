#
# This file is part of greatfet.
#
include_guard()

# General board information.
set(BOARD_ID    3)
set(BOARD_NAME  "lpclink2")

# Pull in the common code for the LPC4330.
include(${PATH_LIBGREAT_FIRMWARE_CMAKE}/platform/lpc4330.cmake)
