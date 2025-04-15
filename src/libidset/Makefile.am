AM_CFLAGS = \
	$(WARNING_CFLAGS) \
	$(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
	$(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir) \
	-I$(top_srcdir)/vendored/libccan

noinst_LTLIBRARIES = libidset.la
fluxinclude_HEADERS = idset.h
libidset_la_SOURCES = idset.c \
		      idset_private.h \
		      idset_decode.c \
		      idset_encode.c \
		      idset_format.c

TESTS = test_idset.t

check_PROGRAMS = $(TESTS)

TEST_EXTENSIONS = .t
T_LOG_DRIVER = env AM_TAP_AWK='$(AWK)' $(SHELL) \
       $(top_srcdir)/config/tap-driver.sh

test_idset_t_SOURCES = test/idset.c
test_idset_t_CPPFLAGS = $(AM_CPPFLAGS)
test_idset_t_LDADD = \
	$(builddir)/libidset.la \
	$(top_builddir)/vendored/libveb/libveb.la \
	$(top_builddir)/vendored/libtap/libtap.la
