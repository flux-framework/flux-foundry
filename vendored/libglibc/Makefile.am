AM_CFLAGS = \
        $(WARNING_CFLAGS) \
        $(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
        $(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir)


noinst_LTLIBRARIES = libglibc.la
libglibc_la_SOURCES =

EXTRA_libglibc_la_SOURCES = \
	argz.h \
	argz.c \
	mempcpy.h \
	mempcpy.c
