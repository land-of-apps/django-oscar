#!/usr/bin/env bash

set +e

cat .navie/issues/14/code.patch | git apply
