## Bugs 

### Bug 01
- **Issue**: Migrate would not run when initializing the workspace and adding `'django.contrib.sites',` to installed apps.
- **Cause**: Added `'allauth.socialaccount',` and migrated before adding `'django.contrib.sites',`.
- **Fix**: Remove `'allauth.socialaccount',`, run migrations and then re-add and migrate again. 