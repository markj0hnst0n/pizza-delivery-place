## Testing

### Manual Testing

Manual testing was used to test navigation, responsiveness on different screen sizes, database operations (Create, Read, Update and Delete) and application functions.

### Responsiveness

#### Desired Result

All information from each page on the app should be viewable on all screen sizes from small mobile phone, to tablet sized devices up to very large monitor screens.

#### Steps Taken to Ensure Result

The Bootstrap grid system was used to ensure data displayed in a satisfactory manner on vaious screen sizes. CSS was used to make images responsive and create appropriate behavour.

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

#### Navbar (Navigation Bar)

#### Search function

#### Footer

#### Menu Category navbar

### Behaviour of Site Pages

#### Index page

#### Timeslot page

#### Menu Items page

#### Cart page

#### Checkout page

- Preloader

#### Checkout success page

#### User Profile page

#### Admin Profile page

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