#!/bin/bash

version=`cat version`

rm -fr libaltaircamlegacy-$version
rm -fr libaltaircamlegacy_*
rm -fr libaltaircamlegacy-dev_*
rm -f debfiles/compat
rm -f debfiles/patches/*
