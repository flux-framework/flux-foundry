SUBDIRS = \
	vendored/libtap \
	vendored/libccan \
	vendored/libveb \
	vendored/libglibc \
	vendored/libczmq \
	vendored/libtomlc99 \
	src/libmissing \
	src/libutil \
	src/libhostlist \
	src/libidset \
	src/liboptparse \
	doc

EXTRA_DIST = \
	NEWS.md \
	README.md \
	NOTICE.LLNS \
	config/tap-driver.sh \
	vendored/libjansson/LICENSE \
	vendored/libjansson/value.c

ACLOCAL_AMFLAGS = -I config

noinst_HEADERS = \
	src/include/flux/types.h \
	src/include/flux/idset.h

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
