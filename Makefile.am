SUBDIRS = \
	vendored/libtap \
	src/libutil \
	src/libhostlist \
	doc

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

export DEB_BUILD_OPTIONS ?= nocheck terse
deb: debian scripts/debbuild.sh
	+@$(top_srcdir)/scripts/debbuild.sh $(abs_top_srcdir)

clean-local:
	@rm -rf debbuild
