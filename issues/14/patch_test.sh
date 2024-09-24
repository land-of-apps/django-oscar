#!/usr/bin/env bash

set +e

cat ../django-oscar-demo/issues/14/test.patch | git apply
