SUBDIRS = \
	vendored/libtap \
	src/libutil \
	src/libhostlist

EXTRA_DIST = \
	NEWS.md \
	README.md \
	NOTICE.LLNS \
	config/tap-driver.sh

ACLOCAL_AMFLAGS = -I config

CODE_COVERAGE_IGNORE_PATTERN = \
	"/usr/include/*" \
	"*/t/*" \
	"*/src/common/libccan/*" \
	"*/src/common/libtap/*" \
	"*/test/*.c"

CODE_COVERAGE_LCOV_OPTIONS =
@CODE_COVERAGE_RULES@
