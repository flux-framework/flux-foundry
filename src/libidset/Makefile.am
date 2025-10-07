AM_CFLAGS = \
	$(WARNING_CFLAGS) \
	$(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
	$(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir) \
	-I$(top_srcdir)/vendored/libccan \
	-I$(top_srcdir)/src/include

pkgconfig_DATA = flux-idset.pc

noinst_LTLIBRARIES = libidset.la
fluxinclude_HEADERS = idset.h
libidset_la_SOURCES = idset.c \
		      idset_private.h \
		      idset_decode.c \
		      idset_encode.c \
		      idset_format.c

lib_LTLIBRARIES = \
	libflux-idset.la

libflux_idset_la_SOURCES =
libflux_idset_la_LIBADD = \
	$(builddir)/libidset.la \
	$(top_builddir)/vendored/libveb/libveb.la \
	$(top_builddir)/src/libutil/libutil.la
libflux_idset_la_LDFLAGS = \
	-export-symbols-regex "^(idset_|__asan)" \
	-version-info 1:0:0 \
	-shared -export-dynamic --disable-static \
	$(ld_gc_sections) \
	$(san_ld_zdef_flag)

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
	$(top_builddir)/src/libutil/libutil.la \
	$(top_builddir)/vendored/libtap/libtap.la
