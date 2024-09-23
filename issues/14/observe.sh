#!/usr/bin/env bash

set +e

pytest --sqlite tests/integration/basket/test_exclusive_vouchers.py
pytest --sqlite tests/integration/basket/test_utils.py
pytest --sqlite tests/integration/basket/test_views.py
