AM_CFLAGS = \
	$(WARNING_CFLAGS) \
	$(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
	$(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	-I$(top_srcdir) \
	-I$(top_srcdir)/vendored/libccan \
	-I$(top_srcdir)/src/include \
	$(JANSSON_CFLAGS) \
	$(CODE_COVERAGE_CPPFLAGS)

pkgconfig_DATA = flux-conf.pc

noinst_LTLIBRARIES = \
	libconf.la

fluxinclude_HEADERS = \
	conf.h

lib_LTLIBRARIES = \
	libflux-conf.la

libflux_conf_la_SOURCES =
libflux_conf_la_LIBADD = \
	$(builddir)/libconf.la \
	$(top_builddir)/src/libutil/libutil.la \
	$(top_builddir)/vendored/libtomlc99/libtomlc99.la \
	$(JANSSON_LIBS)
libflux_conf_la_LDFLAGS = \
	-export-symbols-regex "^(flux_conf_|__asan)" \
	-version-info 1:0:0 \
	-shared -export-dynamic --disable-static \
	$(ld_gc_sections) \
	$(san_ld_zdef_flag)

libconf_la_SOURCES = \
	conf.c \
	conf_private.h \
	tomltk.h \
	tomltk.c

TESTS = \
	test_tomltk.t \
	test_conf.t

check_PROGRAMS = \
	$(TESTS)

test_ldadd = \
	$(top_builddir)/vendored/libtap/libtap.la \
	$(builddir)/libconf.la \
	$(top_builddir)/src/libutil/libutil.la \
	$(top_builddir)/vendored/libtomlc99/libtomlc99.la \
	$(JANSSON_LIBS)

TEST_EXTENSIONS = .t
T_LOG_DRIVER = env AM_TAP_AWK='$(AWK)' $(SHELL) \
       $(top_srcdir)/config/tap-driver.sh

test_tomltk_t_SOURCES = test/tomltk.c
test_tomltk_t_CPPFLAGS = $(AM_CPPFLAGS)
test_tomltk_t_LDADD = $(test_ldadd)

test_conf_t_SOURCES = test/conf.c
test_conf_t_CPPFLAGS = $(AM_CPPFLAGS)
test_conf_t_LDADD = $(test_ldadd)
