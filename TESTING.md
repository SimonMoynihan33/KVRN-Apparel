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

## Bug 09
- **Issue**: When an item is added to the wishlist, it shows the "Add to Bag" modal with cart contents instead of a simple success message.
- **Cause**: The toast notification used for success messages was displaying cart contents whenever a success message was generated. This was because the toast template included bag details (like bag_items and grand_total) whenever a success message was triggered, regardless of whether it was for the wishlist or the cart.
- **Fix**: Add tags to differentiate between "cart" and "wishlist" messages. In the add_to_bag view, success messages were tagged with "cart," and in the toggle_wishlist view, messages were tagged with "wishlist." The toast template was updated to conditionally display bag contents only for messages tagged with "cart." This ensured that wishlist actions displayed a simple success message without triggering the bag modal.

## Bug 10
- **Issue**: Placement of the wishlist button on the product_detail page would not overlay correctly on the product image or carousel, despite working correctly on the products page. Instead, it stayed positioned above the image or floated inconsistently on the page.
- **Cause**: Differences in the layout structure between products and product_detail templates led to unexpected behavior. The carousel-item structure on product_detail uses specific positioning and overflow styles that interfere with the absolute positioning of the button, preventing it from appearing on top of the image as expected.
- **Fix**: Attempted various placement alternatives, including placing the button outside the carousel structure, to ensure it displayed consistently on the page. Solution was to leave it where the Add to Bag button is.

## Bug 11
- **Issue**: When flex was used and both the Wishlist button and Add to Bag button were side by side, the add to bag view was called when the wishlist button was clicked. Both had seperate class names, and correct urls. The reason for this is still not known. I ran the code through AI to see if they could find the issue but to no avail.
- **Fix**: The only fix was to not have them on the same line using flexbox. When they were on seperate lines of the page this issue did not occur, even with the exact same html structure.

## Bug 12
- **Issue**: When an item was added to the wishlist, the toast message displayed the contents of the shopping bag instead of a wishlist confirmation.
- **Cause**: The toast message, intended for wishlist feedback, was inadvertently using the bag toast success code.
- **Fix**: Add checks to toast_success.html ` {% if 'cart' in message.tags and grand_total and not on_profile_page %}` and add `extra_tags` to both bag view and wishlist view to identify what the messages were for.

## Bug 13
- **Issue**: Old toast notifications appeared upon revisiting the site, resulting in multiple stacked notifications for actions previously completed.

## Bug 14
- **Issue1**: Emails would not send and sent the error `SMTP.starttls() got an unexpected keyword argument 'keyfile'` on live site.
- **Cause**: Compatibility issues with python3.12 and some django versions relating to SMPT.
- **Fix**: [This page](https://stackoverflow.com/questions/77482831/smtp-starttls-got-an-unexpected-keyword-argument-keyfile) outlined that my solution was to upgrade to django 4.12.

## Bug 15
- **Issue**: Internal server error occurs on the live Heroku site when accessing the design submission page, causing the page to fail due to a missing database table for the UserDesignSubmission model.
- **Cause**: This error indicates that the necessary database table, design_submissions_userdesignsubmission, does not exist in the production database. 
- **Fix**: Run migrations in Heroku console.

## Unfixed Bugs
### Bug 01
- **Issue**: When a sorting option is picked and the page updates, it no lomger displays what it is being sorted by, instead it says 'Sort By...' no matter what option is picked.
- **Cause**: Unknown. The walkthrough was followed and extensive troubleshooting took place.
