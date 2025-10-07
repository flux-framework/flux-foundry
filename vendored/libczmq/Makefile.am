AM_CFLAGS = \
        $(WARNING_CFLAGS) \
        $(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
        $(CODE_COVERAGE_LDFLAGS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir)

noinst_LTLIBRARIES = \
	libczmq.la

libczmq_la_SOURCES = \
	czmq_internal.h \
	czmq_internal.c \
	czmq.h \
	zhash_primes.inc \
	zhash.h \
	zhash.c \
	zlist.h \
	zlist.c \
	zhashx.h \
	zhashx.c \
	zlistx.h \
	zlistx.c

EXTRA_DIST = \
	LICENSE
