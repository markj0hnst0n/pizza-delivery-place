## Testing

### Manual Testing

Manual testing was used to test navigation, responsiveness on different screen sizes, database operations (Create, Read, Update and Delete) and application functions.

### Responsiveness

#### Desired Result

All information from each page on the app should be viewable on all screen sizes from small mobile phone, to tablet sized devices up to very large monitor screens.

#### Steps Taken to Ensure Result

The Bootstrap grid system was used to ensure data displayed in a satisfactory manner on vaious screen sizes. CSS was used to make images responsive and create appropriate behavour also media queries were used to ensure readbility on all screen sizes.

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
- Verify profile dropdown works correctly showing register or login options before login, profile and logout options when the suer is logged in.  Superusers can also see the site admin link here :heavy_check_mark:
- Verify clicking on cart takes you to the cart page :heavy_check_mark:
- Verify that the cart gives and accurate total of the bill to be paid from the items which are in the cart :heavy_check_mark:
- Verify that using the search input redirects the user to the **Menu** page which displays the relevant results or user feedback message stating that no results were found :heavy_check_mark:
- Confirm that the navbar stays fixed at the top of the screen and is displayed on top of all other site content :heavy_check_mark:

#### Tablet/Mobile Navbar

- Verify clicking on page logo takes you to the homepage :heavy_check_mark:
- Verify correct colour transition of navigation links on click :heavy_check_mark:
- Verify profile dropdown works correctly showing register or login options before login, profile and logout options when the suer is logged in.  Superusers can also see the site admin link here :heavy_check_mark:
- Verify clicking on cart takes you to the cart page :heavy_check_mark:
- Verify that the cart gives and accurate total of the bill to be paid from the items which are in the cart :heavy_check_mark:
- Verify that using the search input redirects the user to the **Menu** page which displays the relevant results or user feedback message stating that no results were found :heavy_check_mark:
- Confirm that the navbar stays fixed at the top of the screen and is displayed on top of all other site content :heavy_check_mark:

Notes
- In testing the logo was cut off slightly on 'Galaxy fold' device emulation.  This appears to only show 1 half of screen size of the device on research so was not deemed to be a major issue.
- In Chrome dev tools there was a bug where on small screen sizes the navbar did not fill the entire width of the screen byt a tine amount unless the burger icon was tapped.  This is not present in the deployed version on any of the live testing I've used.

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
- Verify that if there are available timeslots in the database they displayed on screen sorted with the earliest times at the top of the page :heavy_check_mark:
- Verify that the timeslots are sorted into columns based on days in the database :heavy_check_mark:
- Verify that if a single timeslot is sold out the button for that timeslot is disabled :heavy_check_mark:
- Verify that if logged in as a super user the user can see the amount remaining for each slot and also edit and delete links to change the timselot if neccessary :heavy_check_mark:
- Clicking on any of the timeslots books this timeslot, dislpays a user feedback message confirming that the slot was booked and takes the customer to the menu to choose their food :heavy_check_mark:

#### Menu Items page

- Verify that items are displayed on screen based on how the user has navigated to this screen.  If the come from booking a timeslot all menu items are displayed but if they choose an option from the menu navbar only options matching the selected category appear :heavy_check_mark:
- Verify that image, price and icons displaying product info display :heavy_check_mark:
- Verify that quick add button appears for all items and clicking this adds 1 of the item to the shopping cart :heavy_check_mark:
- Verify that clicking on the item image takes the user to the menu item display page :heavy_check_mark:

#### Menu Item Detail page

- Verify that all relevant information about the product is dislpayed on screen :heavy_check_mark:
- Verify that clicking on the image takes the user to link of the product image in full size in a new tab :heavy_check_mark:
- Verify that quantity selector is displayed and any quantity of 1 or less makes the minus button disable
- Verify that the quantity selector will not accept values of less than 1 or more than 4 for each product

#### Cart page



#### Checkout page

- Timer
- Preloader

#### Checkout Success page

#### Profile page

#### Admin page

#### Checkout success page

#### User Profile page

#### Admin Profile page

#### About page

#### Contact page




### Automated testing

#### W3C HTML Validation

#### W3C CSS Validation

Custom static CSS file run through w3c CSS validator without any issues.

#### Google Lighthouse Testing information

|   Bug	    | Debug                |
|-----------|----------------------|
| Database stopped working due to information in one of the fields not fitting the data model | Ran python3 manage.py flush to delete all information in database |
| Error message of "'decimal.Decimal' object is not iterable" being returned when trying to use context processor to add up cart item total | There was a return statement in my function in contexts.py which meant the contexts where not being rendered correctly.  Cart total now works correctly.
| Quantity increase and decrease buttons were not disabling below 1 and above 99 as per js. | The classes which the js used to identify the buttons were named as the wrong variable names.
| Remove button not working on cart page. | JQuery version being used did not have the correct POST functionality and there were indentation errors in the remove from cart view.  I was also using square brackets as opposed to normal brackets in the view to reomve the item from cart.
| While developing on VScode I couldn't use the local server to test webhooks | I tired to use gitpod and transfer code across but this was un wieldly.  I then used a service called ngrok to create a tunnel from my localhost address which allowed the local site to be available on a public server.  This enabled me to test webhooks.
| Users could book a timeslot but technically never check out and therefore use up slots the that could be used by another customer | I Moved the timeslot database call to the checkout so that the slot is only booked in when the order goes through
| Card can be charged and order created but if there is no slot available an error can be generated | Moved the function to check the number of timeslots left to the checkout page itself instead of success so that the slots remaining are checked before the card can be charged
| User Email not being picked up from form on contact form | Name needed to be added to form data
| Customer could sit on checkout page indefinitely ensuring that once there they could book a slot at any time this could mean multiple extra bookings for the same slot as slot database only checked when checkout page loaded | Timer added to checkout page to ensure fast checkout of user.  Only a 2 min window for multiple booking possibilities.
| Profile page didn't display default saved address | form instance had syntax relating to request.POST when the request was GET so it was not filling the form data correctly
| Only 1 allergen could be added to each menu item | Changed relationship from foreignkey to many to many which enabled multiple allergens for each menu item