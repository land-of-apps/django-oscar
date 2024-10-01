#!/usr/bin/env bash

set +e

cat ./.navie/issues/16/code.patch | git apply
