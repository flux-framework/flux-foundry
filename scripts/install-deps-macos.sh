#!/bin/bash

die() {
    echo "$(basename $0): $@" >&2
    exit 1
}

test -f scripts/$(basename $0) || die "please run from the top level of the source tree"

eval "$(/opt/homebrew/bin/brew shellenv)"

brew install \
  autoconf \
  automake \
  libtool \
  make \
  pkg-config \
  hwloc

echo "Now run scripts/configure-macos.sh"
