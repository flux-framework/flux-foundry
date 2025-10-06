AM_CFLAGS = \
	$(WARNING_CFLAGS) \
	$(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
	$(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir) \
	-I$(top_srcdir)/vendored/libccan

noinst_LTLIBRARIES = liboptparse.la
fluxinclude_HEADERS = optparse.h
liboptparse_la_SOURCES = optparse.c

lib_LTLIBRARIES = \
	libflux-optparse.la

libflux_optparse_la_SOURCES =
libflux_optparse_la_LIBADD = \
	$(builddir)/liboptparse.la \
	$(top_builddir)/vendored/libczmq/libczmq.la \
	$(top_builddir)/vendored/libglibc/libglibc.la \
	$(top_builddir)/src/libutil/libutil.la \
	$(top_builddir)/src/libmissing/libmissing.la
libflux_optparse_la_LDFLAGS = \
	-export-symbols-regex "^(optparse_|__asan)" \
	-version-info 1:0:0 \
	-shared -export-dynamic --disable-static \
	$(ld_gc_sections) \
	$(san_ld_zdef_flag)

TESTS = test_optparse.t

check_PROGRAMS = $(TESTS)

TEST_EXTENSIONS = .t
T_LOG_DRIVER = env AM_TAP_AWK='$(AWK)' $(SHELL) \
       $(top_srcdir)/config/tap-driver.sh

test_optparse_t_SOURCES = test/optparse.c
test_optparse_t_CPPFLAGS = $(AM_CPPFLAGS)
test_optparse_t_LDADD = \
	$(top_builddir)/vendored/libtap/libtap.la \
	$(builddir)/liboptparse.la \
	$(top_builddir)/vendored/libczmq/libczmq.la \
	$(top_builddir)/vendored/libglibc/libglibc.la \
	$(top_builddir)/src/libutil/libutil.la \
	$(top_builddir)/src/libmissing/libmissing.la

pkgconfig_DATA = flux-optparse.pc
