#!/bin/sh -v
#
# Run an extra libtoolize before autoreconf to ensure that
# libtool macros can be found if libtool is in PATH, but its
# macros are not in default aclocal search path.
#
libtoolize --automake --copy || exit
autoreconf --force --verbose --install || exit
echo "Now run ./configure."
