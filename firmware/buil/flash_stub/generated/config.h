/**
 * This file is part of greatfet.
 *
 * Base configuration for greatfet builds.
 */

//
// WARNING: This configuration file (config.h) is automatically generated, and may be overwritten during build!
//          The source for this file is config.h.in, which CMake automatically configures into config.h. You likely
//          want to edit the cmake configuration (or the .in template file) instead.
//

// The identification number for the current board.
#define CONFIG_BOARD_ID 1

// The version of the firmware currently running.
#define CONFIG_VERSION_STRING "git-v2021.2.1-25-g744afa0-dirty"

// The size of the platform's debug ring, in bytes.
#define CONFIG_DEBUG_RING_SIZE 4096
#define CONFIG_DEFAULT_LOG_LEVEL 6

// Define how much logging we're willing to enable.
#define CONFIG_ENABLE_LOGGING
//#define CONFIG_ENABLE_QUIET_LOGGING
//#define CONFIG_ENABLE_VERBOSE_LOGGING
//#define CONFIG_ENABLE_VERBOSE_TRACING

// Determine what logging methods we're willing to use.
#define CONFIG_ENABLE_DEBUG_RING
#define CONFIG_ENABLE_SEMIHOSTING

// Genreal logging options.
#define CONFIG_ENABLE_LOG_TIMESTAMPS

// Uncommented automatically if the build has enabled backtrace support and the platform supports backtracing.
#define CONFIG_ENABLE_BACKTRACE

// The maximum depth of a debug backtrace.
#define CONFIG_MAX_BACKTRACE_SIZE 25

// Uncommented if our compiler has included function names in the binary for our debug use.
//#define CONFIG_ENABLE_FUNCTION_NAMES
