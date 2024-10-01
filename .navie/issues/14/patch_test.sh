#!/usr/bin/env bash

set +e

cat .navie/issues/14/test.patch | git apply
