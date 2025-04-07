AM_CFLAGS = \
    -I$(top_srcdir) \
    $(WARNING_CFLAGS) \
    $(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
    $(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
    $(CODE_COVERAGE_CPPFLAGS)

noinst_LTLIBRARIES = \
    libhostlist.la

fluxinclude_HEADERS = \
    hostlist.h

lib_LTLIBRARIES = \
	libflux-hostlist.la

libflux_hostlist_la_SOURCES =
libflux_hostlist_la_LIBADD = \
	$(builddir)/libhostlist.la
libflux_hostlist_la_LDFLAGS = \
	-export-symbols-regex "^(hostlist_|__asan)" \
	-version-info 1:0:0 \
	-shared -export-dynamic --disable-static \
	$(ld_gc_sections) \
	$(san_ld_zdef_flag)

libhostlist_la_SOURCES = \
    util.h \
    util.c \
    hostname.h \
    hostname.c \
    hostrange.h \
    hostrange.c \
    hostlist.h \
    hostlist.c

TESTS = \
    test_util.t \
    test_hostname.t \
    test_hostrange.t \
    test_hostlist.t

check_PROGRAMS = \
    $(TESTS)

TEST_EXTENSIONS = .t
T_LOG_DRIVER = env AM_TAP_AWK='$(AWK)' $(SHELL) \
       $(top_srcdir)/config/tap-driver.sh

test_hostname_t_SOURCES = \
    test/hostname.c
test_hostname_t_CPPFLAGS = \
    $(AM_CPPFLAGS)
test_hostname_t_LDADD = \
    $(top_builddir)/vendored/libtap/libtap.la \
    $(top_builddir)/src/libhostlist/libhostlist.la

test_util_t_SOURCES = \
    test/util.c
test_util_t_CPPFLAGS = \
    $(AM_CPPFLAGS)
test_util_t_LDADD = \
    $(top_builddir)/vendored/libtap/libtap.la \
    $(top_builddir)/src/libhostlist/libhostlist.la

test_hostrange_t_SOURCES = \
    test/hostrange.c
test_hostrange_t_CPPFLAGS = \
    $(AM_CPPFLAGS)
test_hostrange_t_LDADD = \
    $(top_builddir)/vendored/libtap/libtap.la \
    $(top_builddir)/src/libhostlist/libhostlist.la

test_hostlist_t_SOURCES = \
    test/hostlist.c
test_hostlist_t_CPPFLAGS = \
    $(AM_CPPFLAGS)
test_hostlist_t_LDADD = \
    $(top_builddir)/vendored/libtap/libtap.la \
    $(top_builddir)/src/libhostlist/libhostlist.la
