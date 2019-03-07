#!/bin/bash

ln ../libaltaircamlegacy-*.tar.gz
rel=`cut -d' ' -f3 < /etc/redhat-release`
fedpkg --release f$rel local
