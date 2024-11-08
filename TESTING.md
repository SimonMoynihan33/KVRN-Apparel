# KVRN Apparel Testing Documentation

## Index
- [KVRN Apparel Testing Documentation](#kvrn-apparel-testing-documentation)
  - [Index](#index)
  - [Introduction](#introduction)
  - [Testing Strategy](#testing-strategy)
  - [Types of Testing Conducted](#types-of-testing-conducted)
  - [Test Cases](#test-cases)
  - [Browser and Responsiveness Testing](#browser-and-responsiveness-testing)
    - [Chrome](#chrome)
    - [Edge](#edge)
    - [Safari](#safari)
    - [Opera](#opera)
    - [Firefox](#firefox)
  - [User Acceptance Criteria](#user-acceptance-criteria)
    - [Milestone 1: Project Planning and Research](#milestone-1-project-planning-and-research)
    - [Milestone 2: Product Setup and Home Page](#milestone-2-product-setup-and-home-page)
    - [Milestone 3: Product Management and Shopping Bag](#milestone-3-product-management-and-shopping-bag)
    - [Milestone 4: Checkout, Payments, and Profile Management](#milestone-4-checkout-payments-and-profile-management)
    - [Milestone 5: Testing, Documentation, Final Deployment, and Marketing Strategy](#milestone-5-testing-documentation-final-deployment-and-marketing-strategy)
    - [Milestone 6: Planned for Future Deployments](#milestone-6-planned-for-future-deployments)
  - [Test Cases - by Features](#test-cases---by-features)
  - [Code Validation](#code-validation)
    - [Validation Tests/Results](#validation-testsresults)
    - [Python Formatting and Linting](#python-formatting-and-linting)
      - [Tools Used](#tools-used)
      - [Process](#process)
    - [JavaScript Linting with ESLint](#javascript-linting-with-eslint)
      - [ESLint Setup and Configuration](#eslint-setup-and-configuration)
      - [Results of ESLint Linting](#results-of-eslint-linting)
      - [Future Reference and Additional Notes](#future-reference-and-additional-notes)
    - [HTML Validation Results](#html-validation-results)
    - [CSS Validation Results](#css-validation-results)
  - [Lighthouse](#lighthouse)
    - [Desktop Lighthouse Scores](#desktop-lighthouse-scores)
    - [Mobile Lighthouse Scores](#mobile-lighthouse-scores)
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

## Introduction
This document details the testing conducted for **KVRN Apparel**, an e-commerce platform specializing in custom apparel. Comprehensive testing was performed to ensure that each feature provides a reliable, accessible, and user-friendly experience.

## Testing Strategy
Our testing strategy included a combination of manual and user acceptance testing. The goal was to validate functionality, performance, and accessibility across devices and browsers, ensuring a consistent experience for users.

## Types of Testing Conducted
1. **Integration Testing**: Tested interactions between key components (e.g., Cart, Wishlist, Checkout) to confirm smooth functionality across the full shopping flow.
2. **System Testing**: End-to-end testing covering workflows from browsing to checkout, ensuring users can navigate the site, add products to the cart, and complete purchases.
3. **Extensive Manual Testing**: Extensive manual testing was carried out and documented in this file.
4. **User Acceptance Testing (UAT)**: Real-world scenario testing to confirm that the application meets user expectations and requirements.
5. **Cross-Browser Testing**: Tested compatibility across major browsers (Chrome, Firefox, Safari, Edge) on desktop and mobile devices.

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
| Nest Hub (1024px)        | Windows, Android | Zooming issue when filtering products or rendering new pages; fixes on refresh.                    | Uncertain if this is an issue with Opera DevTools; unable to test on a physical device. <details><summary>Opera Nest Hub Error</summary><img src="documentation/testing/responsive-errors/opera-nest-zoom-error.png"></details> |
| Galaxy Fold (344px)      | Android          | Zooming issue similar to Nest Hub, resolved on refresh.                                            | Same issue as above. <details><summary>Opera Galaxy Fold Error</summary><img src="documentation/testing/responsive-errors/opera-galaxy-zoom-error.png"></details> |
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

## User Acceptance Criteria

### Milestone 1: Project Planning and Research

| **User Story**               | **MoSCoW**   | **Acceptance Criteria**                                                                                                           | **Status**           |
|------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **Wireframes**               | Must Have    | - [x] Wireframes are created for the home page, product page, and checkout page.                                                  | Completed            |
|                              |              | - [x] The wireframes align with the overall design direction.                                                                     |                       |
| **ERD**                      | Should Have  | - [x] An ERD is created outlining product, user, and order relationships.                                                         | Completed            |
|                              |              | - [x] The ERD reflects database structure and supports business logic.                                                            |                       |
|                              |              | - [x] Three custom models are planned for implementation.                                                                         |                       |
| **Project Setup**            | Must Have    | - [x] Project is initialized with version control (Git/GitHub).                                                                   | Completed            |
|                              |              | - [x] Necessary dependencies and libraries are installed.                                                                         |                       |
| **Base Template**            | Must Have    | - [x] Pages share a consistent header, footer, and navigation.                                                                    | Completed            |

### Milestone 2: Product Setup and Home Page

| **User Story**               | **MoSCoW**   | **Acceptance Criteria**                                                                                                           | **Status**           |
|------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **Home Page**                | Must Have    | - [x] The homepage has a hero section and displays featured products.                                                             | Completed            |
| **Products Setup**           | Must Have    | - [x] Products are displayed with images, descriptions, and prices.                                                               | Completed            |
|                              |              | - [x] Products are organized into categories.                                                                                     |                       |
| **Product Sorting**          | Must Have    | - [x] Customers can sort products by price (ascending/descending), name, and rating.                                              | Completed            |
|                              |              | - [x] Design is easy to use and shows relevant products.                                                                          |                       |
| **Product Filtering and Searching** | Must Have | - [x] Customers can search for products by name or description.                                                                  | Completed            |
|                              |              | - [x] Filtering options are available for categories, price range, etc.                                                           |                       |

### Milestone 3: Product Management and Shopping Bag

| **User Story**               | **MoSCoW**   | **Acceptance Criteria**                                                                                                           | **Status**           |
|------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **Toasts**                   | Must Have    | - [x] Toast notifications appear after key actions (adding to cart, product updates, successful checkout).                        | Completed            |
| **Shopping Bag**             | Must Have    | - [x] Products can be added to a shopping bag.                                                                                   | Completed            |
|                              |              | - [x] Shopping bag displays correct quantities, total price, and selected items.                                                  |                       |
| **Product Modifying**        | Should Have  | - [x] Admins can update product details from the admin panel.                                                                     | Completed            |
|                              |              | - [x] Super Users can update products from the front end.                                                                         |                       |
| **Adding Products**          | Must Have    | - [x] Admins can add products via an admin panel.                                                                                | Completed            |
|                              |              | - [x] Admins can also add products through the site, allowing for admin CRUD operations.                                          |                       |
| **About Us Page**            | Could Have   | - [x] A static webpage where users can view information about the shop owner.                                                     | Completed            |
|                              |              | - [x] Information is available to contact the KVRN team or just about the products.                                               |                       |

### Milestone 4: Checkout, Payments, and Profile Management

| **User Story**               | **MoSCoW**   | **Acceptance Criteria**                                                                                                           | **Status**           |
|------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **Guest Checkout**           | Must Have    | - [x] Guest checkout option is available for customers who don't want to register.                                                | Completed            |
|                              |              | - [x] Guest customers can still receive order confirmation emails.                                                                |                       |
| **Stripe Payments**          | Must Have    | - [x] Stripe payment gateway is integrated for secure transactions.                                                               | Completed            |
|                              |              | - [x] Customers receive an email confirmation after successful payment.                                                           |                       |
| **Checkout App**             | Must Have    | - [x] Customers can enter shipping details.                                                                                       | Completed            |
|                              |              | - [x] Payment methods are available (integrated with Stripe).                                                                     |                       |
| **Saved Payment Methods**    | Could Have   | - [x] Customers can save payment methods during checkout.                                                                         | Completed            |
|                              |              | - [x] Saved payment methods are securely stored and can be used in future purchases.                                              |                       |
| **More Products (Late in Development)** | Should Have | - [x] New products are added to existing categories.                                                                    | Completed            |
|                              |              | - [x] Each new product includes relevant details like description, price, and images.                                             |                       |
| **Authentication and Authorization** | Must Have | - [x] Secure registration and login process is implemented.                                                              | Completed            |
|                              |              | - [x] Users can log in and log out.                                                                                               |                       |
| **Wishlist Feature**         | Should Have  | - [x] Users can add products to a wishlist from the product page.                                                                 | Completed            |
|                              |              | - [x] The wishlist is accessible from the user’s profile.                                                                         |                       |
| **Newsletter Signup in Footer** | Could Have | - [x] A sign-up form is added to the footer of the site.                                                                          | Completed            |
| **Profile Management**       | Must Have    | - [x] Users can view and update profile details.                                                                                  | Completed            |
|                              |              | - [x] Users can see their order history on the profile page.                                                                      |                       |

### Milestone 5: Testing, Documentation, Final Deployment, and Marketing Strategy

| **User Story**               | **MoSCoW**   | **Acceptance Criteria**                                                                                                           | **Status**           |
|------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **Final Deployment**         | Must Have    | - [x] The project is deployed on Heroku.                                                                                          | Completed            |
|                              |              | - [x] All environment variables are configured for production.                                                                    |                       |
| **Testing**                  | Must Have    | - [x] Manual testing is carried out for all functionality.                                                                        | Completed            |
|                              |              | - [x] Integration tests are in place to test interactions between components.                                                     |                       |
| **Instagram Page Integration** | Could Have | - [x] A link to the Instagram page is added to the footer or header.                                                              | Completed            |
|                              |              | - [x] The Instagram page opens in a new tab when clicked.                                                                         |                       |
| **Facebook Page Setup**      | Must Have    | - [x] A branded Facebook page is set up with business details.                                                                    | Completed            |
|                              |              | - [x] The page is linked to the e-commerce website and products can be shared easily.                                             |                       |
| **SEO Optimization**         | Must Have    | - [x] The website follows SEO best practices.                                                                                     | Completed            |
|                              |              | - [x] Meta tags are added.                                                                                                        |                       |
|                              |              | - [x] robots.txt file is present for crawlers.                                                                                    |                       |
|                              |              | - [x] sitemap.xml file is present in the footer.                                                                                  |                       |
| **Accessibility Review**     | Could Have   | - [x] The site passes basic accessibility checks (contrast ratio, alt text for images).                                           | Completed            |
| **Documentation**            | Must Have    | - [x] In-code documentation is used generously to make sure all code is clear and maintainable                                    | Completed            |
|                              |              | - [x] Extensive README is written outlining features, testing, issues, bugs, etc.                                                 |                       |

### Milestone 6: Planned for Future Deployments

| **User Story**               | **MoSCoW**   | **Acceptance Criteria**                                                                                                           | **Status**           |
|------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **Blog Integration**         | Won't Have   | - [ ] A blog section is added to the website with promotional posts.                                                              | Future Deployment    |
|                              |              | - [ ] Users can leave likes on blog posts.                                                                                        |                       |
| **Abandoned Cart Email Reminders** | Won't Have | - [ ] Customers receive an email reminder after leaving items in their shopping cart for 24 hours.                               | Future Deployment    |
|                              |              | - [ ] The email contains a link back to the shopping cart.                                                                        |                       |
| **Multicurrency Support**    | Won't Have   | - [ ] Customers can select their preferred currency from a dropdown.                                                              | Future Deployment    |
|                              |              | - [ ] Prices update dynamically based on the selected currency.                                                                   |                       |
| **Quick View on Products**   | Won't Have   | - [ ] A "Quick View" button is available on the product catalog page.                                                             | Future Deployment    |
|                              |              | - [ ] The "Quick View" popup shows the product image, price, and a brief description.                                             |                       |
| **Wishlist to Cart Functionality** | Won't Have | - [ ] Customers can add wishlist items to the shopping cart with a single click.                                                 | Future Deployment    |
|                              |              | - [ ] Product quantities and options are retained when moving from wishlist to cart.                                              |                       |
| **Newsletter Email**         | Won't Have   | - [ ] Newsletter emails are sent to customers who subscribed to the mailing list.                                                 | Future Deployment    |
|                              |              | - [ ] The email includes links to the latest products and promotions.                                                             |                       |

---

This project follows Agile development principles, focusing on delivering core functionalities first to establish a Minimum Viable Product (MVP) for initial deployment. Lower-priority features were either postponed or scheduled for later iterations. The project board reflects this Agile approach, showing stories shifted between milestones as development needs evolved. For example, stories marked as milestone 2 (M2) were, in some cases, moved to milestone 3, highlighting the project's adaptive lifecycle and ensuring the most valuable features were prioritized and delivered within the timeline.

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
| **FAQ Accordion Functionality**    | Verify that the FAQ accordion displays relevant questions and allows smooth expansion and collapse functionality.  | Accordion works as intended, allowing users to navigate between questions easily.                                    | Works as intended         |
| **Internal Links in FAQ**          | Check that links within the FAQ page bring users to the relevant information sections.                             | Links navigate to the correct sections smoothly.                                                                     | Works as intended         |
| **Other Features**                  |                                                                                                                    |                                                                                                                      |                           |                     |
| Account Creation                    | Verify account registration, including email confirmation if applicable.                                           | Account is created, and user receives verification email.                                                            | Works as intended         |                     |
| Login and Logout                    | Test login and logout functionality to ensure sessions work correctly.                                             | User can log in, navigate site, and log out without issues.                                                          | Works as intended         |                     |
| Password Reset                      | Confirm password reset request triggers email with reset link, and password can be updated.                        | Password reset email is sent; user can reset password via link, and new password works as expected.                  | Works as intended         |                     |
| Change Password                     | Verify that user can successfully change password within the profile section.                                      | Password update is saved and works correctly on the next login.                                                      | Works as intended         |                     |
| Error Handling                      | Confirm error messages display appropriately for invalid actions and input across the site.                        | Error handling is consistent and informative across pages, preventing unintended actions.                            | Works as intended         | Comprehensive site-wide error handling in place. |

## Code Validation

### Validation Tests/Results
Summary of the tools used for code validation and any results.

### Python Formatting and Linting

In this project, Python code formatting and linting were handled using `flake8` and `black` to ensure code readability, consistency, and adherence to style guidelines.

#### Tools Used
- **Flake8**: Used for linting to catch style errors and improve code quality.
- **Black**: An autoformatter that enforces consistent styling across Python files.

#### Process
1. **Initial Linting with Flake8**  
   `flake8` was run manually on each file. This allowed a thorough review of linting issues, highlighting any PEP 8 inconsistencies, long lines, unused imports, and other style errors. Each issue was addressed individually while working within the file to maintain compliance.

2. **Auto-formatting with Black**  
   After manually reviewing and addressing issues flagged by `flake8`, the code was then auto-formatted using `black`. This tool standardized the code format according to Black's conventions, handling aspects such as line length, indentation, and string formatting automatically. This step ensures a consistent code style across the entire project.

3. **Final Linting with Flake8**  
   After running `black`, `flake8` was executed once more from the terminal to verify that all style errors were resolved. A lack of output indicated that the code passed `flake8` checks successfully, meaning no further linting issues were detected.


### JavaScript Linting with ESLint

This project uses **ESLint** to maintain code quality and consistency across JavaScript files, covering both standalone `.js` files and inline JavaScript within HTML files. This setup ensures modern JavaScript standards (ES6+) and custom project requirements are met.

#### ESLint Setup and Configuration

1. **Node.js and npm Installation**:
   - **Node.js** and **npm** are required to install and use ESLint.
   - Download and install **Node.js** from [nodejs.org](https://nodejs.org/), which includes **npm**.

2. **Installing ESLint and Plugins**:
   - ESLint was installed along with the `eslint-plugin-html` plugin to enable linting for both `.js` files and inline JavaScript within HTML files.
   - Install these as development dependencies in your project:
     ```bash
     npm install eslint eslint-plugin-html --save-dev
     ```

3. **Configuring ESLint (`.eslintrc.json`)**:
   - To support ES6 syntax, browser environment, and global variables, the following configurations were applied in `.eslintrc.json`:
   
     ```json
     {
       "parserOptions": {
         "ecmaVersion": 2020           // Enables ES6+ syntax support.
       },
       "env": {
         "browser": true                // Sets up browser-specific globals (e.g., `window`, `document`).
       },
       "globals": {
         "$": "readonly",               // Declares `$` (for jQuery) as a global variable, read-only.
         "Stripe": "readonly"           // Declares `Stripe` as a global variable, read-only.
       },
       "plugins": ["html"]              // Enables the `eslint-plugin-html` plugin to parse inline JavaScript in HTML files.
     }
     ```

   - **Configuration Breakdown**:
     - **`parserOptions.ecmaVersion`**: Set to `2020` to enable ES6+ syntax. This supports features like `const`, `let`, and arrow functions.
     - **`env.browser`**: Specifies that the code will run in a browser environment, making ESLint aware of browser-specific global variables like `window` and `document`.
     - **`globals`**:
       - **`$`** (jQuery) and **`Stripe`** were declared as global variables with `"readonly"` to avoid ESLint’s `no-undef` warnings. Declaring them as read-only prevents accidental modification.
     - **`plugins`**: The `html` plugin is included to enable ESLint to parse and lint inline JavaScript within HTML files.

4. **Running ESLint Commands**:
   - **Standard Run**:
     ```bash
     npx eslint .
     ```
     - Runs ESLint across the entire project. If there are no issues, no output is displayed.
   
   - **Quiet Mode**:
     ```bash
     npx eslint . --quiet
     ```
     - Runs ESLint in quiet mode, which suppresses non-error messages, only outputting actual errors (useful for streamlined checks).

   - **Debug Mode**:
     ```bash
     npx eslint . --debug
     ```
     - Provides verbose output about the files ESLint processes, the rules it applies, and the configuration loaded. This helps verify that all desired files (including HTML) are being linted.

#### Results of ESLint Linting

1. **Standalone JavaScript Files**:
   - Running `npx eslint .` successfully identified and checked all `.js` files in the project.
   - Since no issues were found, ESLint returned no output, indicating that the JavaScript code conforms to configured rules.

2. **Inline JavaScript in HTML Files**:
   - After installing `eslint-plugin-html` and updating the `.eslintrc.json` configuration, ESLint successfully parsed and linted JavaScript embedded in HTML files.
   - `npx eslint .` with `eslint-plugin-html` found no issues, indicating that inline JavaScript met all linting requirements.
   - Running in debug mode confirmed that ESLint processed HTML files and applied the JavaScript rules to inline scripts.

3. **Summary of No Output**:
   - ESLint returned no output in both standard and quiet mode, meaning no errors or warnings were found in the project’s JavaScript (including inline HTML).
   - Debug mode (`npx eslint . --debug`) confirmed that ESLint loaded the correct configuration and linted all intended files without errors.

#### Future Reference and Additional Notes

- **Re-running ESLint**: Use `npx eslint .` any time to check both standalone `.js` and inline JavaScript in HTML files.
- **Modifying Configuration**:
  - If additional global variables are needed, they can be added under the `globals` section in `.eslintrc.json` as `"variableName": "readonly"`.
  - The `parserOptions.ecmaVersion` can be updated if the project requires newer ECMAScript features.
  - Adding more plugins or rules can further customize linting to meet evolving project requirements.
- **Output and Quiet Mode**: A silent output in quiet mode (`--quiet`) generally indicates no errors or warnings, meaning your code meets ESLint rules.

By following these setup and configuration steps, ESLint is fully prepared to maintain code quality across JavaScript files, whether standalone or inline, throughout the project’s lifecycle.


### HTML Validation Results

| Page                         | Validation Status                    | Screenshot                                                                                                 |
|------------------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------|
| 400 Error Page               | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-400-val.png"></details> |
| 403 Error Page               | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-403-val.png"></details> |
| 404 Error Page               | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-404-val.png"></details> |
| 500 Error Page               | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-500-val.png"></details> |
| About Page                   | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-about-val.png"></details> |
| Bag Page                     | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-bag-val.png"></details> |
| Change Password Success Page | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-change-pass-success-val.png"></details> |
| Change Password Page         | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-change-pass-val.png"></details> |
| Checkout Success Page        | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-checkout-success-val.png"></details> |
| Checkout Page                | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-checkout-val.png"></details> |
| Confirm Email Verification   | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-confirm-email-verification-val.png"></details> |
| Cookies Page                 | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-cookies-val.png"></details> |
| Edit Product Page            | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-edit-product-val.png"></details> |
| FAQ Page                     | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-faq-val.png"></details> |
| Home Page                    | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-index-val.png"></details> |
| Login Page                   | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-login-val.png"></details> |
| Logout Page                  | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-logout-val.png"></details> |
| Order Detail Page            | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-order-detail-val.png"></details> |
| Password Reset Page          | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-pass-reset-val.png"></details> |
| Privacy Policy Page          | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-privacy-policy-val.png"></details> |
| Product Detail Page          | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-product-detail-val.png"></details> |
| Product Management Page      | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-product-management-val.png"></details> |
| Products Page                | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-products-val.png"></details> |
| Profile Page                 | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-profile-val.png"></details> |
| Register Page                | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-register-val.png"></details> |
| Submission Page              | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-submission-val.png"></details> |
| Terms and Conditions Page    | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-tnc-val.png"></details> |
| User Messages Page           | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-user-msgs-val.png"></details> |
| Verify Email Request Page    | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-varify-email-req-val.png"></details> |
| Wishlist Page                | No errors or warnings               | <details><summary>View</summary><img src="documentation/testing/code-validation/html-validation/html-wishlist-val.png"></details> |

### CSS Validation Results

| CSS File            | Validation Status                    | Warning Details                                                                                           | Screenshot                                                                                                 |
|---------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| About Styles          | No errors or warnings               | N/A                                                                                                      | <details><summary>View</summary><img src="documentation/testing/code-validation/css-validation/css-about-val.png"></details> |
| Base Styles         | Warning (non-critical)              | Imported Google Fonts. This warning does not affect functionality or styling compatibility.               | <details><summary>View Validation</summary><img src="documentation/testing/code-validation/css-validation/css-base-val.png"></details> <details><summary>View Warning</summary><img src="documentation/testing/code-validation/css-validation/css-base-warning.png"></details> |
| Checkout Styles       | Warning (non-critical)              | Webkit transition is a vendor extension for browser-specific compatibility; does not impact overall CSS. | <details><summary>View Validation</summary><img src="documentation/testing/code-validation/css-validation/css-checkout-val.png"></details> <details><summary>View Warning</summary><img src="documentation/testing/code-validation/css-validation/css-checkout-warning.png"></details> |
| FAQ Styles            | No errors or warnings               | N/A                                                                                                      | <details><summary>View</summary><img src="documentation/testing/code-validation/css-validation/css-faq-val.png"></details> |
| Messages Styles       | No errors or warnings               | N/A                                                                                                      | <details><summary>View</summary><img src="documentation/testing/code-validation/css-validation/css-messages-val.png"></details> |
| Profile Styles        | No errors or warnings               | N/A                                                                                                      | <details><summary>View</summary><img src="documentation/testing/code-validation/css-validation/css-profile-val.png"></details> |
| Submissions Styles    | No errors or warnings               | N/A                                                                                                      | <details><summary>View</summary><img src="documentation/testing/code-validation/css-validation/css-submissions-val.png"></details> |

## Lighthouse

### Desktop Lighthouse Scores

| Page                   | Lighthouse Score |
|------------------------|------------------|
| **About Page**         | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-about.png" alt="About Page Lighthouse Score"></details> |
| **Bag Page**           | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-bag.png" alt="Bag Page Lighthouse Score"></details> |
| **Checkout Success**   | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-checkout-success.png" alt="Checkout Success Lighthouse Score"></details> |
| **Checkout Page**      | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-checkout.png" alt="Checkout Page Lighthouse Score"></details> |
| **Home Page**          | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-home.png" alt="Home Page Lighthouse Score"></details> |
| **Order Detail**       | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-order-detail.png" alt="Order Detail Lighthouse Score"></details> |
| **Product Detail**     | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-product-detail.png" alt="Product Detail Lighthouse Score"></details> |
| **Products Page**      | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-products.png" alt="Products Page Lighthouse Score"></details> |
| **Profile Page**       | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-profile.png" alt="Profile Page Lighthouse Score"></details> |
| **Submit Design Page** | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-submit-design.png" alt="Submit Design Page Lighthouse Score"></details> |
| **Wishlist Page**      | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-desktop/lh-d-wishlist.png" alt="Wishlist Page Lighthouse Score"></details> |

### Mobile Lighthouse Scores

| Page                   | Lighthouse Score |
|------------------------|------------------|
| **About Page**         | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-about.png" alt="About Page Mobile Lighthouse Score"></details> |
| **Bag Page**           | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-bag.png" alt="Bag Page Mobile Lighthouse Score"></details> |
| **Checkout Success**   | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-checkout-success.png" alt="Checkout Success Mobile Lighthouse Score"></details> |
| **Checkout Page**      | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-checkout.png" alt="Checkout Page Mobile Lighthouse Score"></details> |
| **FAQ Page**           | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-faq.png" alt="FAQ Page Mobile Lighthouse Score"></details> |
| **Home Page**          | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-home.png" alt="Home Page Mobile Lighthouse Score"></details> |
| **Order Detail**       | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-order-detail.png" alt="Order Detail Mobile Lighthouse Score"></details> |
| **Product Detail**     | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-prduct-detail.png" alt="Product Detail Mobile Lighthouse Score"></details> |
| **Products Page**      | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-products.png" alt="Products Page Mobile Lighthouse Score"></details> |
| **Profile Page**       | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-profile.png" alt="Profile Page Mobile Lighthouse Score"></details> |
| **Submit Design Page** | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-submit-design.png" alt="Submit Design Page Mobile Lighthouse Score"></details> |
| **Wishlist Page**      | <details><summary>View Score</summary><img src="documentation/testing/lighthouse/lighthouse-mobile/lh-m-wishlist.png" alt="Wishlist Page Mobile Lighthouse Score"></details> |

---

Some of the Lighthouse scores, both on desktop and mobile, are currently sub-optimal due to time constraints and the project's short deadlines. Significant improvements have been made to maximize these scores as much as possible within the available time, but there is still room for optimization in areas such as accessibility and SEO. These scores are satisfactory and functional, but with more time, additional refinements would be possible. Future iterations will revisit these scores to further enhance performance, focusing especially on accessibility and SEO improvements that couldn't be fully implemented in this phase.



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

To date, no bugs have been found and left unfixed.
