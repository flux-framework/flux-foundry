##
# Prologue
##
AC_INIT([flux-foundry],
        m4_esyscmd([git describe --always | awk '/.*/ {sub(/^v/, ""); printf "%s",$1; exit}']))
AC_CONFIG_AUX_DIR([config])
AC_CONFIG_MACRO_DIR([config])
AC_CONFIG_SRCDIR([NEWS.md])
AC_CANONICAL_TARGET

AM_INIT_AUTOMAKE([subdir-objects tar-pax foreign])
AM_SILENT_RULES([yes])
AC_CONFIG_HEADERS([config/config.h])
AM_MAINTAINER_MODE([enable])

AC_DEFINE([_GNU_SOURCE], 1,
          [Define _GNU_SOURCE so that we get all necessary prototypes])

##
# Generate project versions from PACKAGE_VERSION (set from git describe above)
##
AX_SPLIT_VERSION
AX_POINT_VERSION=$(echo $AX_POINT_VERSION | $SED 's/-.*$//')
AC_SUBST([AX_MAJOR_VERSION])
AC_SUBST([AX_MINOR_VERSION])
AC_SUBST([AX_POINT_VERSION])

##
# Initialize pkg-config for PKG_CHECK_MODULES to avoid conditional issues
##
PKG_PROG_PKG_CONFIG
PKG_INSTALLDIR

# Checks for programs
##
m4_version_prereq(2.70, [AC_PROG_CC], [AC_PROG_CC_C99])
AM_PROG_CC_C_O
AX_COMPILER_VENDOR
AX_COMPILER_VERSION
AS_CASE($ax_cv_c_compiler_vendor,
  [clang | gnu], [
    WARNING_CFLAGS="-Wall -Werror -Wno-strict-aliasing -Wno-error=deprecated-declarations"
  ]
)
AC_SUBST([WARNING_CFLAGS])

LT_INIT

AX_CODE_COVERAGE

AC_ARG_ENABLE([docs],
              AS_HELP_STRING([--disable-docs], [disable building docs]))
AS_IF([test "x$enable_docs" != "xno"], [
            AM_PATH_PYTHON(3.6)
            AM_CHECK_PYMOD(sphinx,
                           [Version(sphinx.__version__) >= Version ('1.6.7')],
                           [sphinx=true],
                           [sphinx=false; AC_MSG_WARN([could not find sphinx to generate docs, version 1.6.7+ required])]
                           )
            AM_CHECK_PYMOD(docutils,
                           [Version(docutils.__version__) >= Version ('0.11.0')],
                           [docutils=true],
                           [docutils=false; AC_MSG_WARN([could not find docutils to generate docs, version 0.11.0+ required])]
                           )
])
#  If --enable-docs=yes, but no doc generator found,
#   then error immediately:
#
AS_IF([test "x$enable_docs" = "xyes" -a "x$sphinx" = "xfalse"],[
  AC_MSG_ERROR([--enable-docs used but no document generator found!])
])
AS_IF([test "x$enable_docs" = "xyes" -a "x$docutils" = "xfalse"],[
  AC_MSG_ERROR([--enable-docs used but docutils not found!])
])
AM_CONDITIONAL([ENABLE_DOCS], [test "x$sphinx" = "xtrue" -a "x$docutils" = "xtrue"])
AC_CHECK_PROG(ASPELL,[aspell],[aspell])


AS_VAR_SET(fluxincludedir, $includedir/flux)
AC_SUBST(fluxincludedir)

##
# Epilogue
##
AC_CONFIG_FILES( \
  Makefile \
  vendored/libtap/Makefile \
  vendored/libccan/Makefile \
  vendored/libveb/Makefile \
  src/libutil/Makefile \
  src/libhostlist/Makefile \
  src/libhostlist/flux-hostlist.pc \
  src/libidset/Makefile \
  src/libidset/flux-idset.pc \
  doc/Makefile \
  doc/test/Makefile \
)

AC_OUTPUT
