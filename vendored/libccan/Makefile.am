AM_CFLAGS = \
        $(WARNING_CFLAGS) \
        $(CODE_COVERAGE_CFLAGS)

AM_LDFLAGS = \
        $(CODE_COVERAGE_LIBS)

AM_CPPFLAGS = \
	$(CODE_COVERAGE_CPPFLAGS)

EXTRA_DIST = \
	licenses \
	ccan/str/LICENSE \
	ccan/str/hex/LICENSE \
	ccan/build_assert/LICENSE \
	ccan/array_size/LICENSE \
	ccan/str/_info \
	ccan/str/hex/_info \
	ccan/build_assert/_info \
	ccan/array_size/_info

noinst_LTLIBRARIES = libccan.la
libccan_la_SOURCES = \
	ccan/str/str.c \
	ccan/str/debug.c \
	ccan/str/str.h \
	ccan/str/str_debug.h \
	ccan/str/hex/hex.h \
	ccan/str/hex/hex.c \
	ccan/build_assert/build_assert.h \
	ccan/array_size/array_size.h
