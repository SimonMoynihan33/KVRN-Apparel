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
  

## Unfixed Bugs
### Bug 01
- **Issue**: When a sorting option is picked and the page updates, it no lomger displays what it is being sorted by, instead it says 'Sort By...' no matter what option is picked.
- **Cause**: Unknown. The walkthrough was followed and extensive troubleshooting took place.

## Credits
### Images
- [Hero Image](https://modernartetc.com/products/photography-of-american-landscape-series) 