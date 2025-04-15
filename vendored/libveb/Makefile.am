AM_CFLAGS = \
        $(WARNING_CFLAGS) \
        $(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
        $(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir)

EXTRA_DIST = \
	LICENSE \
	README \
	veb_mach.c \
	man/veb.3

noinst_LTLIBRARIES = libveb.la
libveb_la_SOURCES = \
	veb.c \
	veb.h

TESTS = test_veb.t

check_PROGRAMS = $(TESTS)

TEST_EXTENSIONS = .t
T_LOG_DRIVER = env AM_TAP_AWK='$(AWK)' $(SHELL) \
	$(top_srcdir)/config/tap-driver.sh

test_veb_t_SOURCES = test/veb.c
test_veb_t_CPPFLAGS = $(AM_CPPFLAGS)
test_veb_t_LDADD = \
	$(builddir)/libveb.la \
	$(top_builddir)/vendored/libtap/libtap.la
