#!/usr/bin/env bash

set +e

cat issues/14/test.patch | git apply
