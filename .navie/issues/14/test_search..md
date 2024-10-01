Here are the relevant locations in the codebase that deal with adding vouchers to the basket and might be related to the issue where exclusive vouchers can be added multiple times:

* [tests/integration/basket/test_views.py](command:vscode.open?tests/integration/basket/test_views.py) This file contains tests for adding and removing vouchers from the basket.
  - `test_add_voucher` method: Tests that a voucher can be added to the basket through the appropriate view.
  - `test_remove_voucher` method: Tests that a voucher can be removed from the basket through the appropriate view.

* [tests/integration/basket/test_views.py:195-214](command:vscode.open?tests/integration/basket/test_views.py:195-214) This snippet tests adding products to the basket with required options.
  - `test_add_to_basket_with_options_required` method: Tests adding a product to the basket with required options.

* [tests/integration/basket/test_views.py:234-256](command:vscode.open?tests/integration/basket/test_views.py:234-256) This snippet tests adding products to the basket with non-required options.
  - `test_add_to_basket_with_options_not_required` method: Tests adding a product to the basket with non-required options.

* [tests/integration/offer/test_condition.py](command:vscode.open?tests/integration/offer/test_condition.py) This file contains tests for various conditions related to offers.
  - `test_single_item_fails` method: Tests that a single item fails the condition.
  - `test_not_discountable_item_fails` method: Tests that a non-discountable item fails the condition.
  - `test_single_item_passes_partial_condition` method: Tests that a single item passes the partial condition.
  - `test_upsell_message` method: Tests the upsell message for the condition.

* [tests/integration/offer/test_condition.py:190-210](command:vscode.open?tests/integration/offer/test_condition.py:190-210) This snippet tests various conditions related to the basket value.
  - `test_less_value_basket_passes_partial_condition` method: Tests that a basket with less value passes the partial condition.
  - `test_matching_basket_passes_condition` method: Tests that a matching basket passes the condition.
  - `test_greater_than_basket_passes_condition` method: Tests that a basket with greater value passes the condition.
  - `test_consumption` method: Tests the consumption of items in the basket.
  - `test_consumption_with_high_value_product` method: Tests the consumption of items with a high-value product.

These locations are relevant because they involve the logic for adding vouchers and products to the basket, as well as the conditions that determine whether an offer can be applied. Investigating these areas should help identify why exclusive vouchers can be added multiple times.
