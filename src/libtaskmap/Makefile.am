AM_CFLAGS = \
	$(WARNING_CFLAGS) \
	$(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
	$(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir) \
	-I$(top_srcdir)/src/include \
	-I$(top_srcdir)/vendored/libccan \
	$(JANSSON_CFLAGS)

noinst_LTLIBRARIES = \
	libtaskmap.la
fluxinclude_HEADERS = \
	taskmap.h
libtaskmap_la_SOURCES = \
	taskmap_private.h \
	taskmap.c

TESTS = test_taskmap.t

check_PROGRAMS = \
	$(TESTS)

TEST_EXTENSIONS = .t
T_LOG_DRIVER = env AM_TAP_AWK='$(AWK)' $(SHELL) \
       $(top_srcdir)/config/tap-driver.sh

test_taskmap_t_SOURCES = test/taskmap.c
test_taskmap_t_CPPFLAGS = $(AM_CPPFLAGS)
test_taskmap_t_LDADD = \
	$(top_builddir)/vendored/libtap/libtap.la \
	$(builddir)/libtaskmap.la \
	$(top_builddir)/src/libutil/libutil.la \
	$(top_builddir)/src/libidset/libidset.la \
	$(top_builddir)/vendored/libveb/libveb.la \
	$(top_builddir)/vendored/libczmq/libczmq.la \
	$(JANSSON_LIBS)
