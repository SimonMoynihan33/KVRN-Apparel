## Bugs 

### Bug 01
- **Issue**: Migrate would not run when initializing the workspace and adding `'django.contrib.sites',` to installed apps.
- **Cause**: Added `'allauth.socialaccount',` and migrated before adding `'django.contrib.sites',`.
- **Fix**: Remove `'allauth.socialaccount',`, run migrations and then re-add and migrate again. 

### Bug 02
- **Issue**: After django-makrdownx would not work due to compatibility issues, I uninstalled it. This caused errors due to earlier migrations and would not allow my server to run.
- **Cause**: After uninstalling it, earlier migrations depended on it.
- **Fix**: Manually delete migration 0005 and 0006. Migration 0006 depended on 005 so they both had to be deleted and new migrations had to be run.

### Bug 03
- **Issue**: Sorting by category in the dropdown duplicates products.
- **Cause**: Use of ManyToMany relationship for categories.
- **Fix**: Remove this option to save time.

### Bug 04
- **Issue**: Toast close button not working.
- **Cause**: Div tag automatically closed at the end of line.
- **Fix**: Move closing div tag to end of toast file.

## Bug 05
- **Issue**: `AttributeError at /checkout/
'NoneType' object has no attribute 'split'`. 
- **Cause**: This was happening because the `request.POST.get('client_secret')` is returning `None`, and I was trying to call `.split('_secret')` on it, which causes the `AttributeError` as `None` does not have a `split()` method.
- **Fix**: Add a Check for `client_secret`:
```
pid = request.POST.get('client_secret')
if pid:
    pid = pid.split('_secret')[0]
    order.stripe_pid = pid
else:
    messages.error(request, 'There was an issue processing your payment. Please try again.')
    return redirect(reverse('checkout'))
```

## Bug 06 
- **Issue**: Stripe order not processing on front end or going to databse, but being successful on stripe end.

## Unfixed Bugs
### Bug 01
- **Issue**: When a sorting option is picked and the page updates, it no lomger displays what it is being sorted by, instead it says 'Sort By...' no matter what option is picked.
- **Cause**: Unknown. The walkthrough was followed and extensive troubleshooting took place.


## Credits
### Images
- [Hero Image](https://modernartetc.com/products/photography-of-american-landscape-series) 