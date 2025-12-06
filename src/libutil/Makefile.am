AM_CFLAGS = \
	$(WARNING_CFLAGS) \
	$(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
	$(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS) \
	-I$(top_srcdir) \
	-I$(top_srcdir)/vendored/libccan

noinst_LTLIBRARIES = libutil.la

fluxinclude_HEADERS = types.h

libutil_la_SOURCES = \
	errno_safe.h \
	fsd.h \
	fsd.c \
	parse_size.h \
	parse_size.c \
	errprintf.h \
	errprintf.c \
	timestamp.h \
	timestamp.c

TESTS = \
	test_errprintf.t \
	test_fsd.t \
	test_parse_size.t \
	test_timestamp.t

test_ldadd = \
        $(builddir)/libutil.la \
        $(top_builddir)/vendored/libtap/libtap.la \
        $(top_builddir)/vendored/libccan/libccan.la \
        $(top_builddir)/src/libmissing/libmissing.la

test_cppflags = \
	$(AM_CPPFLAGS)

check_PROGRAMS = \
	$(TESTS)

TEST_EXTENSIONS = .t
T_LOG_DRIVER = env AM_TAP_AWK='$(AWK)' $(SHELL) \
	$(top_srcdir)/config/tap-driver.sh

test_errprintf_t_SOURCES = test/errprintf.c
test_errprintf_t_CPPFLAGS = $(test_cppflags)
test_errprintf_t_LDADD = $(test_ldadd)

test_fsd_t_SOURCES = test/fsd.c
test_fsd_t_CPPFLAGS = $(test_cppflags)
test_fsd_t_LDADD = $(test_ldadd)

test_parse_size_t_SOURCES = test/parse_size.c
test_parse_size_t_CPPFLAGS = $(test_cppflags)
test_parse_size_t_LDADD = $(test_ldadd)

test_timestamp_t_SOURCES = test/timestamp.c
test_timestamp_t_CPPFLAGS = $(test_cppflags)
test_timestamp_t_LDADD = $(test_ldadd)
