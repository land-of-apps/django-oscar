### Title
Optimize ConditionalOffer Products Query by Removing Unnecessary Children Joins

### Problem
The current implementation of `ConditionalOffer.products()` queries product children using `Q(parent__includes=self)` in `Range.product_queryset()` and then excludes these children. This leads to unnecessary joins, significantly slowing down the system, especially with a large product database (e.g., 3,000,000 products). The effect is noticeable when querying `OfferListView` and `OfferDetailView`, where response times can exceed 11 seconds, which is unacceptable for a performant system.

### Analysis
The root cause of the issue lies in the inefficient query construction within `Range.product_queryset()`. The query initially includes child products using a Q-join and then subsequently excludes them within `ConditionalOffer.products()`. This results in inefficient database operations that greatly slow down response times. By updating the query logic to bypass unnecessary child product joins when they are excluded later on, significant optimization can be achieved.

### Proposed Changes
1. **src/oscar/apps/offer/abstract_models.py**:
    - **Update `Range.product_queryset()` method**:
        - Modify the query logic to conditionally add the child product joins only if necessary. If the products do not include children, skip the joins.
    - **Update `ConditionalOffer.products()` method**:
        - Ensure that the filtering logic remains correct while adjusting it to the optimized query.

### Detailed Proposed Changes

1. **src/oscar/apps/offer/abstract_models.py**:
    - **`Range.product_queryset()` method:**
        - Refactor the logic adding Q-joins for children. Implement a check to see if these joins are necessary before adding them. If the range includes no child products, skip the inclusion of `Q(parent__includes=self)`.

    <!-- file: /Users/kgilpin/source/land-of-apps/django-oscar_issue16/src/oscar/apps/offer/abstract_models.py -->
    ```python
    def product_queryset(self):
        ...
        # Add logic to check if there are classes in the range or if the included products have children
        if self.includes_classes_or_children():
            product_queryset |= Q(parent__includes=self)
        ...
    ```

2. **`ConditionalOffer.products()` method:**
    - Ensure the exclusion logic remains but is supported by the optimized query from the `product_queryset()` when no child products are included.

    <!-- file: /Users/kgilpin/source/land-of-apps/django-oscar_issue16/src/oscar/apps/offer/abstract_models.py -->
    ```python
    def products(self):
        ...
        # Filtering to keep the logic intact
        return queryset.filter(is_discountable=True).exclude(structure=Product.CHILD)
        ...
    ```

By refactoring the `Range.product_queryset()` to conditionally include joins only when necessary and ensuring that the `ConditionalOffer.products()` method has the correct filtering logic, the response times for querying offers can be significantly improved.
