#!/bin/bash

cp ../patches/*.patch .
rm -f makefile.patch

rm -f libaltaircamlegacy-*.tar.gz
ln ../libaltaircamlegacy-*.tar.gz
rel=`cut -d' ' -f3 < /etc/redhat-release`
fedpkg --release f$rel local
