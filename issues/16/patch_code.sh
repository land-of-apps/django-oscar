#!/usr/bin/env bash

set +e

cat ../django-oscar-demo/issues/16/code.patch | git apply
