### Rewrite Query to Use Django Q Syntax

### Title
Optimize Database Query Using Django Q Syntax for Conditional Offers

### Problem
Offers listing and detail views are experiencing unacceptable performance issues, with request times over 11 seconds, especially with a large database of 3,000,000+ products. The root cause has been identified as unnecessary joins in the `AbstractRange.product_queryset` and `AbstractConditionalOffer.products` methods. These joins involve querying product children that are later excluded, which significantly slows down the query.

### Analysis
1. **Unnecessary Children Joins**:
   * The `AbstractRange.product_queryset` method includes child products using joins.
   * The `AbstractConditionalOffer.products` method subsequently excludes these child products.
   * This redundant querying increases the load and execution time.

2. To solve the issue:
   * Remove unnecessary joins that include child products.
   * Use Django's Q objects to optimize query conditions.
   * Ensure that the optimized query logic aligns with Django's ORM capabilities.

### Proposed Changes
1. **Modify `AbstractRange.product_queryset` Method**:
   Remove the join conditions that include child products.

2. **Refactor `AbstractConditionalOffer.products` Method**:
   Update the filtering logic to use Django Q objects for better efficiency.

### Detailed Changes
1. **File: `src/oscar/apps/offer/abstract_models.py`**:

   Update `AbstractRange.product_queryset` to remove child product joins:

   <!-- file: /Users/kgilpin/source/land-of-apps/django-oscar_issue16/src/oscar/apps/offer/abstract_models.py -->
   ```python
   class AbstractRange(models.Model):
       ...
       def product_queryset(self):
           return Product.objects.exclude(structure=Product.CHILD)
       ...
   ```

2. **File: `src/oscar/apps/offer/abstract_models.py`**:

   Update `AbstractConditionalOffer.products` to use Django Q objects:

   <!-- file: /Users/kgilpin/source/land-of-apps/django-oscar_issue16/src/oscar/apps/offer/abstract_models.py -->
   ```python
   from django.db.models import Q
   class AbstractConditionalOffer(models.Model):
       ...
       def products(self):
           return self.range.product_queryset().filter(
               Q(is_discountable=True) & 
               ~Q(structure=Product.CHILD)
           )
       ...
   ```

### Steps to Implement the Solution
1. **Update the Code**:
   * Modify the `AbstractRange.product_queryset` and `AbstractConditionalOffer.products` methods as detailed.
   * Remove unnecessary joins in `product_queryset`.
   * Use Django Q syntax for product filtering in `products`.

2. **Indexing**:
   * Verify that indices are in place for the columns involved in filtering and joining, primarily `is_discountable` and `structure`.

3. **Testing**:
   * Add and run tests ensuring the optimized query performs correctly without returning child products.
   * Ensure no regressions by running the full test suite.

4. **Performance Monitoring**:
   * Monitor the performance in production to ensure the changes have the desired effect.
   * Evaluate request times for OfferListView and OfferDetailView.

By implementing these changes, the query performance for Conditional Offers should improve significantly, reducing request times from more than 11 seconds to below 1 second.