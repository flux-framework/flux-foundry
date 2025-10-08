AM_CFLAGS = \
	$(WARNING_CFLAGS) \
        $(CODE_COVERAGE_CFLAGS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir)

noinst_LTLIBRARIES = libmissing.la

libmissing_la_LIBADD = $(LTLIBOBJS)
libmissing_la_SOURCES =

EXTRA_libmissing_la_SOURCES = \
	argz.h \
	mempcpy.h
