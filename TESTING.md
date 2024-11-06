# KVRN Apparel Testing Documentation

## Index
- [KVRN Apparel Testing Documentation](#kvrn-apparel-testing-documentation)
  - [Index](#index)
  - [Introduction](#introduction)
  - [Testing Strategy](#testing-strategy)
  - [Types of Testing Conducted](#types-of-testing-conducted)
  - [Tools Used](#tools-used)
  - [Test Cases](#test-cases)
  - [Browser and Responsiveness Testing](#browser-and-responsiveness-testing)
    - [Chrome](#chrome)
    - [Edge](#edge)
    - [Safari](#safari)
    - [Opera](#opera)
    - [Firefox](#firefox)
  - [User Acceptance Testing](#user-acceptance-testing)
  - [Test Cases - by Features](#test-cases---by-features)
  - [Code Validation](#code-validation)
    - [Validation Tests/Results](#validation-testsresults)
    - [CI Python Linter Results](#ci-python-linter-results)
    - [JSLint Results](#jslint-results)
    - [W3C Validator HTML/CSS Results](#w3c-validator-htmlcss-results)
    - [Wave Accessibility Results](#wave-accessibility-results)
    - [PageSpeed Insights Results](#pagespeed-insights-results)
  - [Bugs](#bugs)
    - [Bug 01](#bug-01)
    - [Bug 02](#bug-02)
    - [Bug 03](#bug-03)
    - [Bug 04](#bug-04)
    - [Bug 05](#bug-05)
    - [Bug 06](#bug-06)
    - [Bug 07](#bug-07)
    - [Bug 08](#bug-08)
    - [Bug 09](#bug-09)
    - [Bug 10](#bug-10)
  - [Bug 11](#bug-11)
    - [Bug 12](#bug-12)
    - [Bug 13](#bug-13)
    - [Bug 14](#bug-14)
    - [Bug 15](#bug-15)
  - [Unfixed Bugs](#unfixed-bugs)
    - [Bug 01](#bug-01-1)

## Introduction
This document details the testing conducted for **KVRN Apparel**, an e-commerce platform specializing in custom apparel. Comprehensive testing was performed to ensure that each feature provides a reliable, accessible, and user-friendly experience.

## Testing Strategy
Our testing strategy included a combination of manual and user acceptance testing. The goal was to validate functionality, performance, and accessibility across devices and browsers, ensuring a consistent experience for users.

## Types of Testing Conducted
1. **Unit Testing**: Validation of individual components, particularly models and views. Tests focused on verifying database interactions, model relationships, and view behaviors.
2. **Integration Testing**: Tested interactions between key components (e.g., Cart, Wishlist, Checkout) to confirm smooth functionality across the full shopping flow.
3. **System Testing**: End-to-end testing covering workflows from browsing to checkout, ensuring users can navigate the site, add products to the cart, and complete purchases.
4. **User Acceptance Testing (UAT)**: Real-world scenario testing to confirm that the application meets user expectations and requirements.
6. **Cross-Browser Testing**: Tested compatibility across major browsers (Chrome, Firefox, Safari, Edge) on desktop and mobile devices.

## Tools Used
- **Flake8 and pycodestyle**: For Pep8 compliance with python line length, white spaces and blank lines.
- **Browser Developer Tools**: For manual testing, inspecting elements, and testing responsiveness.
- **Wave Accessibility Tool**: For accessibility validation.
- **JSLint**: For JavaScript code validation.
- **W3C HTML Validator**: For HTML markup validation.
- **W3C CSS Validator**: For CSS validation.

## Test Cases

| Test Area                     | Test Case Description                                                                                   | Expected Outcome                                                                                       | Actual Outcome           | Notes               |
|-------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------|---------------------|
| **Navigation**                |                                                                                                         |                                                                                                       |                           |                     |
| Main Navigation Links         | Test that all main navigation links direct to the correct pages (e.g., Home, Shop, Wishlist, Profile).  | Each link navigates to its designated page without errors.                                             | Works as intended         |                     |
| Admin Links Visibility        | Confirm admin-only links (Product Management, User Messages) are hidden for non-superuser accounts.     | Admin-only links do not display for regular users.                                                     | Works as intended         |                     |
| Footer Links                  | Verify that footer links to social media and additional info pages are functional.                      | Footer links open correct pages in new tabs or sections.                                               | Works as intended         |                     |
| **Authentication**            |                                                                                                         |                                                                                                       |                           |                     |
| Account Registration          | Test that users can register an account and receive a verification email.                              | Account registration completes, and verification email is sent.                                        | Works as intended         |                     |
| Login and Logout              | Verify login and logout functions across the site and redirect to correct pages upon action completion. | Users can log in, log out, and are redirected appropriately.                                           | Works as intended         |                     |
| Password Reset                | Test that password reset link is sent to registered users and allows successful password update.        | Password reset email is sent, and user can reset password using provided link.                         | Works as intended         |                     |
| **Shopping Flow**             |                                                                                                         |                                                                                                       |                           |                     |
| Add to Cart                   | Confirm that users can add items to the cart with selected quantities and sizes.                        | Cart updates with correct items, quantities, and sizes.                                                | Works as intended         |                     |
| Update Cart                   | Test ability to change quantities or remove items from cart.                                           | Cart reflects changes accurately and updates totals.                                                   | Works as intended         |                     |
| Checkout Process              | Ensure the checkout process allows address input, payment, and order confirmation.                     | User can complete checkout, process payment, and receive confirmation.                                 | Works as intended         |                     |
| Stripe Payment Processing     | Test payment integration with Stripe using test card to complete checkout securely.                    | Stripe processes payments successfully, and order confirmation displays.                               | Works as intended         |                     |
| Order Confirmation Email      | Verify that users receive an order confirmation email with accurate order details after checkout.       | Confirmation email is sent to user with order summary.                                                 | Works as intended         |                     |
| **User Profile Management**   |                                                                                                         |                                                                                                       |                           |                     |
| Update Profile                | Confirm users can update their profile bio information.                                                | Profile information saves and displays updated content.                                                | Works as intended         |                     |
| View Order History            | Test that users can access past orders, including marking removed products as unavailable.             | Order history shows past orders, marking removed items accordingly.                                    | Works as intended         | Mobile layout requires scroll; future fix planned. |
| **Wishlist**                  |                                                                                                         |                                                                                                       |                           |                     |
| Add to Wishlist               | Verify users can add items to the Wishlist from multiple locations (product and Wishlist pages).       | Items are added to Wishlist and visible across sessions.                                               | Works as intended         |                     |
| Remove from Wishlist          | Test ability to remove items from Wishlist without page refresh.                                       | Items are removed from Wishlist, and page doesn’t refresh on removal.                                  | Works as intended         |                     |
| **Review System**             |                                                                                                         |                                                                                                       |                           |                     |
| Submit Review                 | Test that users can submit and update reviews for purchased items.                                     | Reviews save and display; users can update ratings as needed.                                          | Works as intended         |                     |
| Disable Review for Removed    | Confirm that reviews are disabled for removed items within past orders.                                | Reviews cannot be submitted for removed items; message displays as unavailable.                        | Works as intended         |                     |
| **Design Submission**         |                                                                                                         |                                                                                                       |                           |                     |
| Submit Design Entry           | Verify users can submit entries to the design competition.                                             | Submissions are saved and viewable in user submission list.                                            | Works as intended         |                     |
| Edit Design Entry             | Confirm users can edit submissions if status is still "submitted".                                     | Users can edit submissions with "submitted" status; changes display correctly.                         | Works as intended         |                     |
| Lock Design Edit on Status    | Test that design entries with "processing" or "finalized" status cannot be edited.                     | Entries with these statuses are locked from editing; user receives notification message.               | Works as intended         |                     |
| **Error Handling**            |                                                                                                         |                                                                                                       |                           |                     |
| Form Validation Errors        | Verify that invalid form submissions display error messages.                                           | Form validation errors display relevant messages, preventing submission with invalid data.             | Works as intended         |                     |
| Page Not Found (404) Handling | Confirm 404 page displays for invalid URL entries.                                                     | Users are shown a custom 404 page for non-existent pages.                                              | Works as intended         |                     |
| Internal Server Error (500)   | Test that a custom 500 page displays when a server error occurs.                                       | Users are shown a custom 500 error page on server error.                                               | Works as intended         |                     |
| Forbidden Error (403)         | Confirm 403 page displays for unauthorized actions (e.g., accessing restricted areas).                 | Users are shown a custom 403 page for unauthorized access attempts.                                    | Works as intended         |                     |
| Bad Request Error (400)       | Verify that a custom 400 page displays for invalid requests.                                          | Users are shown a custom 400 page on invalid requests.                                                 | Works as intended         |                     |
| General Error Messages        | Check that general errors are handled with user-friendly messages across the site.                    | Error messages display and prevent unintended actions site-wide.                                       | Works as intended         | Comprehensive error handling in place. |

## Browser and Responsiveness Testing

### Chrome
| Device/Screen Size            | Operating System  | Test Results                                                                                       | Notes                       |
|-------------------------------|-------------------|----------------------------------------------------------------------------------------------------|-----------------------------|
| iPhone SE                     | iOS               | No irregularities found.                                                                           |                             |
| iPhone XR                     | iOS               | No irregularities found.                                                                           |                             |
| iPhone 12 Pro                 | iOS               | No irregularities found.                                                                           |                             |
| iPhone 14 Pro Max             | iOS               | No irregularities found.                                                                           |                             |
| Pixel 7                        | Android           | No irregularities found.                                                                           |                             |
| Samsung Galaxy S8+            | Android           | No irregularities found.                                                                           |                             |
| Samsung Galaxy S20 Ultra      | Android           | No irregularities found.                                                                           |                             |
| iPad Mini                     | iOS               | No irregularities found.                                                                           |                             |
| iPad Air                      | iOS               | No irregularities found.                                                                           |                             |
| iPad Pro                      | iOS               | No irregularities found.                                                                           |                             |
| Surface Pro 7                 | Windows           | No irregularities found.                                                                           |                             |
| Surface Duo                   | Android           | No irregularities found.                                                                           |                             |
| Galaxy Z Fold 5               | Android           | No irregularities found.                                                                           |                             |
| Asus Zenbook Fold             | Windows           | No irregularities found.                                                                           |                             |
| Samsung Galaxy A51/A71        | Android           | No irregularities found.                                                                           |                             |
| Nest Hub                      | Android           | No irregularities found.                                                                           |                             |
| Nest Hub Max                  | Android           | No irregularities found.                                                                           |                             |
| Large Screen (2560px)    | Windows          | No irregularities found.                                                                           | Covered all available device presets in Chrome DevTools. |

### Edge
| Device/Screen Size       | Operating System | Test Results                                                                                       | Notes                       |
|--------------------------|------------------|----------------------------------------------------------------------------------------------------|-----------------------------|
| iPad (768px)             | iOS              | No irregularities found.                                                                           |                             |
| iPhone (375px)           | iOS              | No irregularities found.                                                                           |                             |
| Samsung (360px)          | Android          | No irregularities found.                                                                           |                             |
| Galaxy Fold (344px)      | Android          | No irregularities found.                                                                           |                             |
| Laptop (1366px)          | Windows          | No irregularities found.                                                                           |                             |
| Large Screen (2560px)    | Windows          | No irregularities found.                                                                           | Covered main sizes in Edge. |

### Safari
| Device/Screen Size       | Operating System | Test Results                                                                                       | Notes                             |
|--------------------------|------------------|----------------------------------------------------------------------------------------------------|-----------------------------------|
| iPad (768px)             | iOS              | No irregularities found.                                                                           |                                   |
| iPhone (375px)           | iOS              | No irregularities found.                                                                           |                                   |

### Opera
| Device/Screen Size       | Operating System | Test Results                                                                                       | Notes                                                                                                      |
|--------------------------|------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Nest Hub (1024px)        | Windows, Android | Zooming issue when filtering products or rendering new pages; fixes on refresh.                    | Uncertain if this is an issue with Opera DevTools; unable to test on a physical device. <details><summary>Opera Nest Hub Error</summary><img src="documentation/testing/opera-nest-zoom-error.png"></details> |
| Galaxy Fold (344px)      | Android          | Zooming issue similar to Nest Hub, resolved on refresh.                                            | Same issue as above. <details><summary>Opera Galaxy Fold Error</summary><img src="documentation/testing/opera-galaxy-zoom-error.png"></details> |
| iPad (768px)             | iOS              | No irregularities found.                                                                           |                                                                                                            |
| iPhone (375px)           | iOS              | No irregularities found.                                                                           |                                                                                                            |
| Laptop (1366px)          | Windows          | No irregularities found.                                                                           |                                                                                                            |
| Large Screen (2560px)    | Windows          | No irregularities found.                                                                           | Opera issues isolated to specific devices above.                                                           |

### Firefox
| Device/Screen Size       | Operating System | Test Results                                                                                       | Notes                             |
|--------------------------|------------------|----------------------------------------------------------------------------------------------------|-----------------------------------|
| iPad (768px)             | iOS              | No irregularities found.                                                                           |                                   |
| iPhone (375px)           | iOS              | No irregularities found.                                                                           |                                   |
| Samsung (360px)          | Android          | No irregularities found.                                                                           |                                   |
| Laptop (1366px)          | Windows          | No irregularities found.                                                                           |                                   |
| Large Screen (2560px)    | Windows          | No irregularities found.                                                                           | Tested comprehensively up to 2560px. |

## User Acceptance Testing

## Test Cases - by Features

| Feature                             | Test Case Description                                                                                              | Expected Outcome                                                                                                    | Actual Outcome           | Notes               |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------|
| **Home Page**                       |                                                                                                                    |                                                                                                                      |                           |                     |
| Navigation Links                    | Verify all navigation links direct to the correct pages.                                                           | Each link navigates to the intended page.                                                                            | No issues                |                     |
| Scrolling Banner                    | Confirm scrolling banner displays free delivery and competition messages.                                          | Banner displays intended messages clearly.                                                                           | Works as intended         |                     |
| Admin Nav Elements                  | Verify that admin-only elements are hidden for non-superusers.                                                     | Non-superusers do not see product management and user messages in nav.                                               | Works as intended         |                     |
| Responsive Design                   | Confirm layout adapts across desktop, tablet, and mobile screens.                                                  | Page elements resize and stack appropriately on smaller screens.                                                     | No issues                 |                     |
| Load Time                           | Test page load time for optimal performance.                                                                       | Home page loads within acceptable time limits after image compression.                                               | Improved significantly    | Images below 500KB, homepage images ~1MB for quality. |
| **Product Catalog and Filtering**   |                                                                                                                    |                                                                                                                      |                           |                     |
| Gender Buttons on Home Page         | Test gender buttons on home page navigate to gender-specific product sections.                                     | Clicking each button displays products filtered by gender.                                                           | Works as intended         |                     |
| Search Functionality                | Test search by product name returns relevant results.                                                              | Results match search keywords or are empty if no matches are found.                                                  | Works as intended         |                     |
| Filter by Rating                    | Test filter by rating to confirm products display based on rating selection.                                       | Products are filtered by rating.                                                                                     | Not functioning           | Feature removed; will be fixed in future iteration. |
| **Product Detail Page**             |                                                                                                                    |                                                                                                                      |                           |                     |
| Product Information Display         | Verify that product details (name, price, description, size) are displayed accurately.                             | All product details display correctly.                                                                               | Works as intended         |                     |
| Wishlist Button                     | Test adding/removing items from Wishlist.                                                                          | Clicking 'Add to Wishlist' adds the item; 'Remove' removes it.                                                       | Works as intended         | Displays message when Wishlist is empty. |
| Add to Cart                         | Confirm item is added to cart with correct size and quantity.                                                      | Item with specified details appears in cart.                                                                         | Works as intended         |                     |
| Free Delivery Delta                 | Verify free delivery threshold of over €50 functions correctly.                                                    | Free delivery is applied for orders over €50.                                                                        | Works as intended         |                     |
| Stripe Payment Integration          | Confirm Stripe processes payments securely.                                                                        | Stripe transaction completes successfully, and order confirmation displays.                                          | No issues found           |                     |
| Email Confirmation                  | Verify order confirmation email is sent with details.                                                              | Email is received with correct order information.                                                                    | Works as intended         |                     |
| Order Display in Profile            | Confirm completed orders display in user profile.                                                                  | Order history displays in profile page.                                                                              | Works as intended         |                     |
| Pre-filled Profile Information      | Check that profile information pre-fills checkout fields.                                                          | Profile info (name, address) populates checkout fields automatically.                                                | Works as intended         |                     |
| **User Profile**                    |                                                                                                                    |                                                                                                                      |                           |                     |
| Order History                       | Confirm users can view past orders, even for removed products marked accordingly.                                  | Past orders display with removed products noted as unavailable.                                                      | Works as intended         | Mobile layout requires horizontal scrolling for ratings; will update in future iteration. |
| Rating System                       | Ensure users can rate products and update ratings; disabled for removed products.                                  | Ratings are added/updated, disabled for removed items, and averaged across orders.                                   | Works as intended         |                     |
| Profile Update                      | Verify user can update bio information.                                                                            | Profile changes persist and display as updated.                                                                      | Works as intended         |                     |
| Wishlist Management                 | Confirm Wishlist functionality on Wishlist page, product page, and product detail page.                            | Users can add or remove items from Wishlist on multiple pages.                                                       | Works as intended         |                     |
| **Wishlist and Review System**      |                                                                                                                    |                                                                                                                      |                           |                     |
| Add to Wishlist                     | Test adding an item to Wishlist from the product page.                                                             | Product appears in Wishlist.                                                                                         | Works as intended         |                     |
| Remove from Wishlist                | Test removing an item from Wishlist.                                                                               | Product no longer appears in Wishlist.                                                                               | Works as intended         |                     |
| Wishlist Update without Refresh     | Confirm that Wishlist updates without refreshing the page, allowing users to remain in their current scroll position. | Wishlist updates asynchronously without page refresh; changes appear upon full page refresh.                         | Works as intended         | Prevents user from being sent back to top of page after each click. |
| Logged-Out User Redirect            | Verify that logged-out users are redirected to the login page when they attempt to add items to the wishlist.       | Unauthenticated users are redirected to the login page, and a message is displayed prompting login.                  | Works as intended         |                     |
| Logged-In User Toggle               | Confirm that logged-in users can add/remove items from the wishlist without page reload, and icon updates visually. | Wishlist toggle functions as expected; icon changes based on wishlist state without page refresh.                    | Works as intended         |                     |
| Submit Review                       | Confirm users can submit and update a star rating for items via a Bootstrap modal.                                 | Users can submit, view, and update ratings; modal displays feedback messages.                                        | Works as intended         |                     |
| Disabled Reviews for Removed Items  | Verify that ratings are disabled for removed products in the order page.                                           | Rating system is disabled, showing a message if the item has been removed.                                           | Works as intended         |                     |
| Update Review                       | Confirm user can update existing ratings, and that rating average is displayed on product.                         | User can update rating; average rating updates accordingly on the product.                                           | Works as intended         |                     |
| Bootstrap Modal for Reviews         | Verify Bootstrap modal shows the current rating if it exists.                                                      | Modal pre-fills with existing rating, if available.                                                                  | Works as intended         |                     |
| **Design Submission and Competition**|                                                                                                                    |                                                                                                                      |                           |                     |
| Submit Design Entry                 | Test submitting a design entry in the competition.                                                                 | Entry is saved and visible in user’s submission list.                                                                | Works as intended         |                     |
| Update Design Entry                 | Confirm user can update design entry if status is not ‘processing’ or ‘finalized’.                                 | Entry is editable if allowed; displays updated version upon save.                                                    | Works as intended         |                     |
| Submission Success Message          | Verify success message is displayed upon submission or update.                                                     | Message appears confirming successful submission/update.                                                             | Works as intended         |                     |
| Admin Status Management             | Confirm admin can change entry status between submitted, processing, and finalized.                                | Status updates correctly in admin panel; processing/finalized submissions cannot be updated by users.                | Works as intended         |                     |
| Submission Restriction              | Verify users are notified when they attempt to edit entries that are processing or finalized.                      | Users see a message if submission is locked due to processing/finalized status.                                      | Works as intended         |                     |
| **Footer Links**                    |                                                                                                                    |                                                                                                                      |                           |                     |
| Social Media Links                  | Verify that footer links redirect to the appropriate Facebook, Instagram, and GitHub pages for the business.       | All footer links open the correct pages in a new tab.                                                                | Works as intended         |                     |
| Open in New Tab                     | Confirm that all footer links open in a new tab, maintaining the current session.                                  | Footer links open external pages in new tabs, keeping the user on the site.                                          | Works as intended         |                     |
| **Other Features**                  |                                                                                                                    |                                                                                                                      |                           |                     |
| Account Creation                    | Verify account registration, including email confirmation if applicable.                                           | Account is created, and user receives verification email.                                                            | Works as intended         |                     |
| Login and Logout                    | Test login and logout functionality to ensure sessions work correctly.                                             | User can log in, navigate site, and log out without issues.                                                          | Works as intended         |                     |
| Password Reset                      | Confirm password reset request triggers email with reset link, and password can be updated.                        | Password reset email is sent; user can reset password via link, and new password works as expected.                  | Works as intended         |                     |
| Change Password                     | Verify that user can successfully change password within the profile section.                                      | Password update is saved and works correctly on the next login.                                                      | Works as intended         |                     |
| Error Handling                      | Confirm error messages display appropriately for invalid actions and input across the site.                        | Error handling is consistent and informative across pages, preventing unintended actions.                            | Works as intended         | Comprehensive site-wide error handling in place. |

## Code Validation

### Validation Tests/Results
Summary of the tools used for code validation and any results.

### CI Python Linter Results
- **Flake8**: Verified PEP 8 compliance and error-free Python code.

### JSLint Results
- **JavaScript Code Quality**: Ensured JavaScript code follows best practices and is free of syntax errors.

### W3C Validator HTML/CSS Results
- **HTML**: Validated that HTML files are error-free and compliant with W3C standards.
- **CSS**: Checked CSS for syntax errors and compliance with W3C standards.

### Wave Accessibility Results
- **WCAG Compliance**: Confirmed that key pages meet accessibility standards for color contrast, ARIA roles, and screen reader compatibility.

### PageSpeed Insights Results
- **Performance Metrics**: Page load speeds optimized to meet or exceed industry standards.

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

### Bug 05
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

### Bug 06
**Largest Issue to date: Issue begin-23/10/2024**
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

### Bug 07
- **Issue**: Couldn't run migrations as I accidentally modified a core django file.
- **Fix**: Uninstall and reinstalll django

### Bug 08
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

### Bug 09
- **Issue**: When an item is added to the wishlist, it shows the "Add to Bag" modal with cart contents instead of a simple success message.
- **Cause**: The toast notification used for success messages was displaying cart contents whenever a success message was generated. This was because the toast template included bag details (like bag_items and grand_total) whenever a success message was triggered, regardless of whether it was for the wishlist or the cart.
- **Fix**: Add tags to differentiate between "cart" and "wishlist" messages. In the add_to_bag view, success messages were tagged with "cart," and in the toggle_wishlist view, messages were tagged with "wishlist." The toast template was updated to conditionally display bag contents only for messages tagged with "cart." This ensured that wishlist actions displayed a simple success message without triggering the bag modal.

### Bug 10
- **Issue**: Placement of the wishlist button on the product_detail page would not overlay correctly on the product image or carousel, despite working correctly on the products page. Instead, it stayed positioned above the image or floated inconsistently on the page.
- **Cause**: Differences in the layout structure between products and product_detail templates led to unexpected behavior. The carousel-item structure on product_detail uses specific positioning and overflow styles that interfere with the absolute positioning of the button, preventing it from appearing on top of the image as expected.
- **Fix**: Attempted various placement alternatives, including placing the button outside the carousel structure, to ensure it displayed consistently on the page. Solution was to leave it where the Add to Bag button is.

## Bug 11
- **Issue**: When flex was used and both the Wishlist button and Add to Bag button were side by side, the add to bag view was called when the wishlist button was clicked. Both had seperate class names, and correct urls. The reason for this is still not known. I ran the code through AI to see if they could find the issue but to no avail.
- **Fix**: The only fix was to not have them on the same line using flexbox. When they were on seperate lines of the page this issue did not occur, even with the exact same html structure.

### Bug 12
- **Issue**: When an item was added to the wishlist, the toast message displayed the contents of the shopping bag instead of a wishlist confirmation.
- **Cause**: The toast message, intended for wishlist feedback, was inadvertently using the bag toast success code.
- **Fix**: Add checks to toast_success.html ` {% if 'cart' in message.tags and grand_total and not on_profile_page %}` and add `extra_tags` to both bag view and wishlist view to identify what the messages were for.

### Bug 13
- **Issue**: Old toast notifications appeared upon revisiting the site, resulting in multiple stacked notifications for actions previously completed.

### Bug 14
- **Issue1**: Emails would not send and sent the error `SMTP.starttls() got an unexpected keyword argument 'keyfile'` on live site.
- **Cause**: Compatibility issues with python3.12 and some django versions relating to SMPT.
- **Fix**: [This page](https://stackoverflow.com/questions/77482831/smtp-starttls-got-an-unexpected-keyword-argument-keyfile) outlined that my solution was to upgrade to django 4.12.

### Bug 15
- **Issue**: Internal server error occurs on the live Heroku site when accessing the design submission page, causing the page to fail due to a missing database table for the UserDesignSubmission model.
- **Cause**: This error indicates that the necessary database table, design_submissions_userdesignsubmission, does not exist in the production database. 
- **Fix**: Run migrations in Heroku console.

## Unfixed Bugs
### Bug 01
- **Issue**: When a sorting option is picked and the page updates, it no lomger displays what it is being sorted by, instead it says 'Sort By...' no matter what option is picked.
- **Cause**: Unknown. The walkthrough was followed and extensive troubleshooting took place.
