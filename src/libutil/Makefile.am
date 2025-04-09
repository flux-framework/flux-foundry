AM_CFLAGS = \
	$(WARNING_CFLAGS) \
	$(CODE_COVERAGE_CFLAGS) \
	-Wno-strict-aliasing -Wno-error=strict-aliasing \
	-Wno-parentheses -Wno-error=parentheses

AM_LDFLAGS = \
	$(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir) \
	-I$(top_srcdir)/src/include \
	-I$(top_srcdir)/src/common/libccan \
	-I$(top_builddir)/src/common/libflux \
	-DABS_TOP_BUILDDIR=\"$(abs_top_builddir)\" \
	$(JANSSON_CFLAGS)

noinst_LTLIBRARIES = libutil.la

libutil_la_SOURCES = \
	errno_safe.h
