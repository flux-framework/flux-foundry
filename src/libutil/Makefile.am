AM_CFLAGS = \
	$(WARNING_CFLAGS) \
	$(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
	$(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir) \
	-I$(top_srcdir)/vendored/libccan

noinst_LTLIBRARIES = libutil.la

fluxinclude_HEADERS = types.h

libutil_la_SOURCES = \
	errno_safe.h \
	fsd.h \
	fsd.c \
	parse_size.h \
	parse_size.c \
	errprintf.h \
	errprintf.c
