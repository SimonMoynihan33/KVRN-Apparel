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

## Bug 06 (Largest Issue to date: Issue begin-23/10/2024)
- **Issue**: When submitting the checkout form, I encountered a problem where the payment was being processed on the frontend, but the client secret was not being passed to my Django view on the backend. This resulted in either a continuous loading screen after the form submission and a failure to redirect to the checkout success page, or an error page telling me 
<details>
  <summary>Click to view the image</summary>

  ![Error Message](/documentation/bugs/attribute-client-secret-bug.png)
</details>This was avoided by adding checks to see if client secret was loaded to which I would get the error message: "Missing client secret."

**Steps Taken to Troubleshoot:**

Initial Investigation: I began by reviewing the network logs in the browser's developer tools. This allowed me to confirm that the client secret was being properly generated and passed to the frontend, as I could see it in the console logs and in the page source. However, it was not making its way to the backend, as the Django view was logging None for the client secret.

Adding Logs to the Code: To better understand where things were breaking down, I added several log statements to both my JavaScript (to check if the client secret was being passed correctly) and to my Django view (to check if the secret was received). This helped confirm that the client secret was being correctly logged in the frontend, but it wasn't arriving in the backend as part of the form submission.

Using AI for Troubleshooting: I used AI to help guide me through potential issues. With its assistance, I was able to break the problem down and try out various debugging strategies, including checking network requests and cross-checking the flow of data between the frontend and backend.

Working with Tutor Support: I reached out to tutor support for guidance, as this issue had been blocking my progress for a while. They helped me confirm that the client secret was necessary for Stripe to identify the payment intent, and that this was the key missing piece in my form submission.

Identifying the Problem: After carefully reviewing the form submission process, I realized that I was not explicitly passing the client secret from the frontend to the backend. While the client secret was being generated in the frontend, it wasn’t included in the form data being submitted to Django. This explained why my view was receiving None for the client secret.

The Fix: To resolve this issue I rewatched all Stripe videos again, checking my code for potential problems in relation to the walkthrough. To my surprise, I forgot to add a line into my checkout.html:

`<input type="hidden" value="{{ client_secret }}" name="client_secret">`

It really is the simple things! *crying face*

**Issue closed-24/10/2024**

## Bug 07
- **Issue**: Couldn't run migrations as I accidentally modified a core django file.
- **Fix**: Uninstall and reinstalll django

## Bug 08
- **Issue**: Cannot commit.
- **Cause**: Unknown
- **Error**:
```
  no changes added to commit (use "git add" and/or "git commit -a")
gitpod /workspace/KVRN-Apparel/documentation (main) $ git add .
gitpod /workspace/KVRN-Apparel/documentation (main) $ git commit -m "Remove JS console.logs and print statement"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../README.md
        modified:   ../checkout/static/checkout/js/stripe_elements.js
        modified:   ../checkout/views.py

no changes added to commit (use "git add" and/or "git commit -a")
```
- **Fix**: Close terminal and refresh workspace.


## Unfixed Bugs
### Bug 01
- **Issue**: When a sorting option is picked and the page updates, it no lomger displays what it is being sorted by, instead it says 'Sort By...' no matter what option is picked.
- **Cause**: Unknown. The walkthrough was followed and extensive troubleshooting took place.


## Credits
### Images
- [Hero Image](https://modernartetc.com/products/photography-of-american-landscape-series) 