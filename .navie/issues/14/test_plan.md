# Title

Add test case to verify exclusive voucher offer behavior in basket views

# Problem

Exclusive vouchers can be added to the basket multiple times when they should not be, depending on the order they are added. This behavior violates the exclusivity constraint of such vouchers.

# Analysis

The issue seems to be occurring due to a discrepancy in the logic that checks for the exclusivity of voucher offers when they are added to the basket. Exclusive vouchers should ensure that no other vouchers can be used in conjunction. There may be a conditional check or ordering issue within the current validation logic or state management for vouchers in the basket.

To identify and fix the issue, it's necessary to create a failing test case that demonstrates the problem. By doing so, it will be easier to understand where and why the logic is failing, enabling a more straightforward fix.

# Proposed Changes

1. **tests/integration/basket/test_views.py**: Add a new test case that:
   - Creates two exclusive voucher offers and respective vouchers.
   - Adds the vouchers to the basket in different sequences.
   - Verifies that the exclusivity constraint prevents the second voucher from being added after the first.

   Describe the new test case logic:
   - Create two exclusive voucher offers using the `factories.ConditionalOfferFactory` method.
   - Create two vouchers linked to these offers using the `factories.VoucherFactory` method.
   - Simulate adding each voucher to the basket using the `VoucherAddView`.
   - Check that adding the second voucher of an exclusive pair into a basket is correctly blocked and an appropriate message is shown.

2. **src/oscar/apps/basket/views.py** (if needed): Review and potentially modify the logic in the `VoucherAddView` to ensure that the exclusivity of offers is accurately validated regardless of the order in which the vouchers are added. Ensure that the error message or exclusion logic on detecting conflicting exclusive vouchers is correctly implemented.

   Describe specific changes to be made (assuming issues are found in logic after the test fails):
   - Ensure no other exclusive vouchers exist in the basket before adding a new exclusive voucher.
   - Add checks within the `apply_voucher_to_basket` method to validate the exclusivity of vouchers already present in the basket.

By making these changes, the issue with exclusive voucher offers allowing multiple additions to the basket can be corrected and prevented in the future.
