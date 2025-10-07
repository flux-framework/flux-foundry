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

lib_LTLIBRARIES = \
	libflux-taskmap.la

libflux_taskmap_la_SOURCES =
libflux_taskmap_la_LIBADD = \
	$(builddir)/libtaskmap.la \
	$(top_builddir)/src/libutil/libutil.la \
	$(top_builddir)/src/libidset/libidset.la \
	$(top_builddir)/vendored/libveb/libveb.la \
	$(top_builddir)/vendored/libczmq/libczmq.la \
	$(JANSSON_LIBS)
libflux_taskmap_la_LDFLAGS = \
	-export-symbols-regex "^(taskmap_|__asan)" \
	-version-info 1:0:0 \
	-shared -export-dynamic --disable-static \
	$(ld_gc_sections) \
	$(san_ld_zdef_flag)

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
