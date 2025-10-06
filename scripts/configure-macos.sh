#!/bin/bash

die() {
    echo "$(basename $0): $@" >&2
    exit 1
}

test -f scripts/$(basename $0) || die "please run from the top level of the source tree"

eval "$(/opt/homebrew/bin/brew shellenv)"

LDFLAGS=-L${HOMEBREW_PREFIX}/lib

PKG_CONFIG_PATH=$(pkg-config --variable pc_path pkg-config)

PATH=$(brew --prefix libtool)/libexec/gnubin:$PATH

./autogen.sh

CPPFLAGS="$CPPFLAGS" LDFLAGS=$LDFLAGS PKG_CONFIG_PATH=$PKG_CONFIG_PATH \
  ./configure "--prefix=$(pwd)/install-macos"
