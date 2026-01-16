# Oscar E-Commerce Data Architecture

## Overview

Oscar is a Django e-commerce framework built on an **abstract model architecture** enabling complete customization. Core apps include catalogue, partner, basket, order, customer, and offer.

## Django Essentials for Oscar

**Abstract Model Pattern**: All models are abstract base classes in `abstract_models.py`. Concrete models inherit only if not registered:

```python
if not is_model_registered("catalogue", "Product"):
    class Product(AbstractProduct):
        pass
```

**Dynamic Loading**: Use `get_model('catalogue', 'Product')` and `get_class()` from `oscar.core.loading` to access models/classes, enabling project-level overrides.

## Key Model Structure

### Product (Catalogue)
- Three types: `STANDALONE`, `PARENT` (variants container), `CHILD` (variant)
- Related: `product_class`, `categories` (M2M), `stockrecords`, `images`, `attributes`
- EAV pattern via `ProductAttributeValue` supports flexible attributes (TEXT, INTEGER, DATE, OPTION, IMAGE, etc.)

### Category
- Hierarchical using django-treebeard's MP_Node for efficient tree operations
- Key methods: `get_ancestors_and_self()`, `get_full_slug()`

### StockRecord (Partner)
- Links products to partners with pricing/inventory
- Atomic operations: `allocate()`, `consume_allocation()`, `cancel_allocation()`
- Thread-safe updates using F() expressions

### Basket
- States: OPEN, MERGED, SAVED, FROZEN, SUBMITTED
- Caches lines and discount calculations for performance
- Methods: `add_product()`, `all_lines()` (cached), `reset_offer_applications()`

## Data Loading Strategies

### Optimized QuerySets

```python
# Start with base_queryset() - includes select_related/prefetch_related
products = Product.objects.base_queryset()

# Chain prefetch methods to avoid N+1 queries
products = products.prefetch_browsable_categories() \
                   .prefetch_public_children() \
                   .prefetch_attribute_values()  # Critical for EAV

# Aggressive prefetching for orders
orders = Order.objects.select_related(
    'billing_address', 'billing_address__country',
    'shipping_address__country', 'user'
).prefetch_related('lines', 'status_changes')

# Use annotations for existence checks
products.annotate(has_options=Exists(product_options))

# Custom Prefetch objects for fine-grained control
Prefetch('product_class__attributes',
         queryset=ProductAttribute.objects.select_related('option_group'),
         to_attr='_prefetched_attributes')
```

## Performance Optimization

**Bulk Operations**: Use batch_size=500 for `bulk_update()` and `bulk_create()`

**QuerysetCache Pattern**: Oscar caches EAV attribute access. Checks prefetched data before querying.

**Basket Caching**: `basket.all_lines()` caches results. Call `reset_offer_applications()` after modifications.

**Atomic Stock Updates**: Use F() expressions for thread-safe updates:
```python
StockRecord.objects.filter(pk=pk).update(num_allocated=Coalesce(F('num_allocated'), 0) + qty)
```

**Cached Properties**: Oscar uses `@cached_property` extensively. Clear with `del instance.property` if data changes.

## Common Performance Pitfalls

1. **N+1 on Children**: Use `prefetch_public_children()` before accessing `product.children`
2. **Attribute Access**: Always use `prefetch_attribute_values()` before `product.attr.my_attribute`
3. **StockRecord Lookup**: Prefetch stockrecords or use strategy pattern instead of `product.stockrecords.first()` in loops
4. **Category Trees**: Use `get_ancestors_and_self()` once instead of repeated `get_ancestors()`
5. **Basket Modifications**: Group changes before triggering recalculation

## Customization Strategies

### Fork Apps
```bash
python manage.py oscar_fork_app catalogue your_project
```
Update `INSTALLED_APPS` to reference your fork before Oscar's app.

### Extend Models
```python
from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    custom_field = models.CharField(max_length=100)
```

### Custom Managers
```python
from oscar.apps.catalogue.managers import ProductQuerySet

class CustomProductQuerySet(ProductQuerySet):
    def my_filter(self):
        return self.filter(custom_field__isnull=False)
```

## Key Files

- Abstract models: `src/oscar/apps/*/abstract_models.py`
- Managers/QuerySets: `src/oscar/apps/*/managers.py`
- Strategy pattern: `src/oscar/apps/partner/strategy.py`
- Dynamic loading: `src/oscar/core/loading.py`

## Resources

Oscar docs: https://django-oscar.readthedocs.io/
