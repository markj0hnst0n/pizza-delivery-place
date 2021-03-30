## Testing

### Manual Testing

Manual testing was used to test navigation, responsiveness on different screen sizes, database operations (Create, Read, Update and Delete) and application functions.

### Responsiveness

#### Desired Result

All information from each page on the app should be viewable on all screen sizes from small mobile phone, to tablet sized devices up to very large monitor screens.

#### Steps Taken to Ensure Result

The Bootstrap grid system was used to ensure data displayed in a satisfactory manner on vaious screen sizes. CSS was used to make images responsive and create appropriate behaviour also media queries were used to ensure readbility on all screen sizes.

On Chrome Developer Tools the following devices were emulated to check responsiveness:

- Moto G4 (smallest phone screen width available)
- Pixel XL
- iPhone X
- iPad


These physical devices were also used for testing:

- Macbook Pro 15-inch retina screen
- HP e233 23-inch monitor
- Samsung S10e
- iPhone SE2020

#### Verdict

The app adapts to all tested screen sizes and devices and displays as expected. :heavy_check_mark:

### Cross-browser Compatability

#### Desired Result

Display correctly in any browser users are likely to use.

#### Steps Taken to Ensure Result

Tested site on the following browsers:

- [Chrome](https://www.google.com/chrome/) - Desktop and Mobile
- [Firefox](https://www.mozilla.org/en-US/firefox/new/) - Desktop and Mobile
- [Opera](https://www.opera.com/) - Dekstop and Mobile
- [Safari](https://www.safari.com/) - Desktop and Mobile
- [DuckDuckGo](https://duckduckgo.com) - Mobile

#### Verdict

No obvious bugs were detected in any of the tested browsers. :heavy_check_mark:

### Behaviour of Shared Site Components

#### Security

All views where important database CRUD operations are completed have been secured to the best of my knowledge and only verified, authenticated superusers should be able to complete them :heavy_check_mark:

#### Toasts

- Any time user feedback is mentioned this is usually given in the form of a toast pop up at the top of the screen just below the navbar.
- Appear at appropriate times giving user feedback :heavy_check_mark:
- Sit on top of any other content on the screen and a wholely legible and visible :heavy_check_mark:

Note
- The 'arrow' at the top of the toast does not point to the cart on large screens.  This was deemed a minor issue and was not corrected as of the time of writing.

#### Main Navbar (Navigation Bar)

- Verify clicking on page logo takes you to the homepage :heavy_check_mark:
- Verify correct colour transition of navigation links on hover :heavy_check_mark:
- Verify profile dropdown works correctly showing register or login options before login, profile and logout options when the user is logged in.  Superusers can also see the site admin link here :heavy_check_mark:
- Verify clicking on cart takes you to the cart page :heavy_check_mark:
- Verify that the cart gives an accurate total of the bill to be paid from the items which are in the cart :heavy_check_mark:
- Verify that using the search input redirects the user to the **Menu** page which displays the relevant results or user feedback message stating that no results were found :heavy_check_mark:
- Confirm that the navbar stays fixed at the top of the screen and is displayed on top of all other site content :heavy_check_mark:

#### Tablet/Mobile Navbar

- Verify clicking on page logo takes you to the homepage :heavy_check_mark:
- Verify correct colour transition of navigation links on click :heavy_check_mark:
- Verify profile dropdown works correctly showing register or login options before login, profile and logout options when the user is logged in.  Superusers can also see the site admin link here :heavy_check_mark:
- Verify clicking on cart takes you to the cart page :heavy_check_mark:
- Verify that the cart gives an accurate total of the bill to be paid from the items which are in the cart :heavy_check_mark:
- Verify that using the search input redirects the user to the **Menu** page which displays the relevant results or user feedback message stating that no results were found :heavy_check_mark:
- Confirm that the navbar stays fixed at the top of the screen and is displayed on top of all other site content :heavy_check_mark:

Notes
- In testing the logo was cut off slightly on 'Galaxy fold' device emulation.  This appears to only show 1 half of screen size of the device on research so was not deemed to be a major issue.
- In Chrome dev tools there was a bug where on small screen sizes the navbar did not fill the entire width of the screen but a tine amount unless the burger icon was tapped.  This is not present in the deployed version on any of the live testing I've used.

#### Menu Category navbar

- Verify that it displays the menu category options on all screen sizes and clicking the links take you to all the menu options of that category with a descriptive URL :heavy_check_mark:

#### Footer

- Click on navigation links to confirm correct redirection to the appropriate pages :heavy_check_mark:
- All information is legible and visibile on all screen sizes :heavy_check_mark:
- Confirm that the footer stays fixed at the bottom of the screen and is displayed on top of all other site content :heavy_check_mark:

### Behaviour of Site Pages

#### Index/Home page

- Verify that the expected background image is displayed :heavy_check_mark:
- Verify that the expected text is displayed on all screen sizes :heavy_check_mark:
- Confirm that the CTA (Call to Action) button to book a timslot is displayed and clicking it takes customeer to the timeslot booking page :heavy_check_mark:
- Verify correct colour transition of CTA button on hover :heavy_check_mark:

#### Timeslot page

- Verify that if there are no available timeslots in the database an appropriate message is displayed :heavy_check_mark:
- Verify that if there are available timeslots in the database they are displayed on screen sorted with the earliest times at the top of the page :heavy_check_mark:
- Verify that the timeslots are sorted into columns based on days in the database :heavy_check_mark:
- Verify that if a single timeslot is sold out the button for that timeslot is disabled :heavy_check_mark:
- Verify that if logged in as a super user the user can see the amount remaining for each slot and also edit and delete links to change the timselot if neccessary.  CRUD operations tested on the relevant page links :heavy_check_mark:
- Clicking on any of the timeslots books this timeslot, dislpays a user feedback message confirming that the slot was booked and takes the customer to the menu to choose their food :heavy_check_mark:

#### Menu Items page

- Verify that items are displayed on screen based on how the user has navigated to this screen.  If they come from booking a timeslot all menu items are displayed but if they choose an option from the menu navbar only options matching the selected category appear :heavy_check_mark:
- Verify that image, price and icons displaying product info display :heavy_check_mark:
- Verify that quick add button appears for all items and clicking this adds 1 of the item to the shopping cart :heavy_check_mark:
- Verify that clicking on the item image takes the user to the menu item display page :heavy_check_mark:
- Verify that is logged in as a superuser there is an option to edit or delete item and CRUD operations have been tested on the relevant links :heavy_check_mark:

Notes
Deleting a menu item when it is in the cart causes and error.

#### Menu Item Detail page

- Verify that all relevant information about the product is displayed on screen :heavy_check_mark:
- Verify that clicking on the image takes the user to link of the product image in full size in a new tab :heavy_check_mark:
- Verify that quantity selector is displayed and any quantity of 1 or less and 4 or more makes the minus button disable :heavy_check_mark:
- Verify that the quantity selector will not accept values of less than 1 or more than 4 for each product :heavy_check_mark:

#### Cart page

- Verify that a preview of each item in the cart is displayed :heavy_check_mark:
- Verify that quantity selector is displayed and any quantity of 1 or less and 4 or more makes the minus button disable :heavy_check_mark:
- Verify that the quantity selector will not accept values of less than 1 or more than 4 for each product :heavy_check_mark:
- Verify that delivery charge, item totals and grand total figures are displayed correctly :heavy_check_mark:
- Secure Checkout button is displayed and clicking this takes user to the checkout page :heavy_check_mark:

Notes
- Quantity selector checking is completed by both HTML and at the back end so that even though on larger screens one is able to take the quatity selector higher than 4 and lower than -1 input of incorrect figures is not allowed and provides relevant message.

#### Checkout page

- Verify that if user is not logged in a form displays for them to provide all delivery information required.  An option to log in is given at the bottom :heavy_check_mark:
- Verify that if user is logged in a form displays with all their default delivery information if held.  This can be updated and saved via the save information checkbox :heavy_check_mark:
- Verify that a preview of the timeslot booked and cart are displayed to make any final checks prior to payment :heavy_check_mark:
- Verify that an input for credit/debit card info is displayed and errors generate by the input are displayed below the input :heavy_check_mark:
- Verify that the page displays a 2 minute timer at the bottom with a message informing the user that their timeslot is in danger of being booked if they do not check out in that time :heavy_check_mark:
- Verify that a pizza slice loader screen displays once the payment button has been clicked :heavy_check_mark:
- Verify a back button is displayed if the user wants to go back to their cart to adjust items :heavy_check_mark:
- Verify that even if checkout success page is not displayed an order will be generated via information from the payment company and a confirmation email will be sent :heavy_check_mark:

Notes
- Before this page is generated the timeslot database is checked and the user can only get onto the page if there is at least 1 of the chosen timeslot left.  In theory 1 or more users with the same timeslot could get onto this page at the same time if there is only 1 slot left when they attempt to navigate to this page.  The reason for the timer is to minimise the window the user has to checkout to minimise the chance for the same slot to be booked more than once.  If a user manages to checkout and pay but there are no timeslots available an error is generated but they need to contact the shop.  Their card is charged and the order is generated in the webhook.  They will also receive a confirmation email.  The shop can either honour this order or cancel it and refund.

#### Checkout Success page

- Verify that a summary of the order is generated and displayed for the user with all relevant information :heavy_check_mark:
- Verify that a success user feedback message will be displayed :heavy_check_mark:
- Verify that once the order has been generated a confirmation will be sent to the customer :heavy_check_mark:

Notes
- It is only when this page is generated does the site take the timeslot out of the database so that it cannot be used

#### User Profile page

- Verify that a form displays with all the users default delivery information if held.  This can be updated and saved.  CRUD operations checked :heavy_check_mark:
- Verify that the history of the users orders is displays with the most recent showing at the top :heavy_check_mark:
- Users can click on the order number to get a summary of their order. It is a reproduction of the checkout success page :heavy_check_mark:

#### Admin Profile page

- Verify that the order history of all users orders is displays with the most recent showing at the top and a search function to search by order name or customer name :heavy_check_mark:
- Admins can click on the order number to get a summary of the order. It is a reproduction of the checkout success page.  Admins also have the ability to delete an order :heavy_check_mark:
- Refresh timeslot section gives the admin the ability to put a set number of available timeslots into each record on the database :heavy_check_mark:
- Options to Add menu item, add new day or create new timeslot are available to the admin.  All CRUD options available on the relevant pages have been tested :heavy_check_mark:

#### About page

- Verify about page brings up a short message explaining the premise of the company

#### Contact page

- Verify contact link brings up a contact form giving the user the ability to contact the store owner with any issues or feedback


### Automated testing

#### How to run Python automated tests

To run the existing Python tests:
1. Activate your IDE.
2. In the terminal enter the following command: `python3 manage.py test`
    * If you wish to run the tests for a specific app you can enter the following command: `python3 manage.py test <app name>`
3. The test results will be shown within the terminal.

### Coverage

[Coverage.py](https://coverage.readthedocs.io/) was used to provide feedback during testing.

My code coverage currently stands at 63%, and covers most major functionality. 

Due to time constraints 100% coverage was not acheived.

#### How to run coverage

To view the coverage, you can run the following commands:

1. `coverage run --source=. manage.py test` This will run all tests/
2. `coverage report` The coverage will be shown within the terminal, broken down by .py file.
3. You can view an interactive version by using `coverage html`, and then `python3 -m http.server`, and you can view the htmlcov folder in the browser, select specific files, and view which particular sections of code are or aren't being covered.

#### W3C HTML Validation

HTML validation carried out and no major issues.  Type/javascript information was removed from script taqgs as they were causing a warning.

Errors were caused by duplicate ids on cart page but the elements which trigger these errors are never on the screen at the same time one part of the html relates to small screens and one to med/large so this was not investigated further.

#### W3C CSS Validation

Custom static CSS files run through w3c CSS validator without any issues.

#### Flake8/Pep8 Python Validation

Most issues being flagged are for variables that are not being used but removing them would impact functionality of the code.  Line 
148 in settings.py is too long but shortening may impact functionality.  Most other issues caused by automated files.

#### Google Lighthouse Testing information

Extensive lighthouse testing information can be found in pdf form [here](https://github.com/markj0hnst0n/pizza-delivery-place/blob/master/README/testing/lighthouse-testing/)

The main focus was to test for any accessibilty issues for visually impaired readers.  Pages were testing with user logged in as an admin to put the maximum amount of content on each page.  The scores for most pages were acceptable with the index, about, contact, menu, timeslot and cart pages being particularly good.

Performance scores were variable and I have found that some pages scored well at certain times and less well at others so it's assumed that ISP speed variability is the issue and as such less credence was given to these scores.

Search engine optimisation scores were consistently in the high 80s but could have been improved by a meta description.

Accessibility was marked down on cart screen and menu item detail screen due to the increment and decrement buttons.  These were given aria labels to mitigate against this but scores did not improve.

#### Debug Table

|   Bug	    | Debug                |
|-----------|----------------------|
| Database stopped working due to information in one of the fields not fitting the data model | Ran python3 manage.py flush to delete all information in database |
| Error message of "'decimal.Decimal' object is not iterable" being returned when trying to use context processor to add up cart item total | There was a return statement in my function in contexts.py which meant the contexts where not being rendered correctly.  Cart total now works correctly.
| Quantity increase and decrease buttons were not disabling below 1 and above 99 as per js. | The classes which the js used to identify the buttons were named as the wrong variable names.
| Remove button not working on cart page. | JQuery version being used did not have the correct POST functionality and there were indentation errors in the remove from cart view.  I was also using square brackets as opposed to normal brackets in the view to reomve the item from cart.
| While developing on VScode I couldn't use the local server to test webhooks | I tried to use gitpod and transfer code across but this was un wieldly.  I then used a service called ngrok to create a tunnel from my localhost address which allowed the local site to be available on a public server.  This enabled me to test webhooks.
| Users could book a timeslot but technically never check out and therefore use up slots the that could be used by another customer | I Moved the timeslot database call to the checkout so that the slot is only booked in when the order goes through
| Card can be charged and order created but if there is no slot available an error can be generated | Moved the function to check the number of timeslots left to the checkout page itself instead of success so that the slots remaining are checked before the card can be charged
| User Email not being picked up from form on contact form | Name needed to be added to form data
| Customer could sit on checkout page indefinitely ensuring that once there they could book a slot at any time this could mean multiple extra bookings for the same slot as slot database only checked when checkout page loaded | Timer added to checkout page to ensure fast checkout of user.  Only a 2 min window for multiple booking possibilities.
| Profile page didn't display default saved address | form instance had syntax relating to request.POST when the request was GET so it was not filling the form data correctly
| Only 1 allergen could be added to each menu item | Changed relationship from foreignkey to many to many which enabled multiple allergens for each menu item
| It is possible for the user to complete an order when there are no timeslots available.  While the impact on the store should be minimal it may cause issues | Users impacted receive a custom message asking them to contact the store and still receive a confirmation email.
| If a menu item is deleted while it is in the cart it causes an error and the site will generate a 404 error on all pages | Issue with cache.  If all site data is cleared from browser cache the issue does not persist.
| On cart page on large screens increment and decrement buttons would take numbers above 4 and below zero | Rewrote code based on item detail page increment and decrement buttons and bug no longer persisted