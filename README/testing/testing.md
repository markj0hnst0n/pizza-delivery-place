|   Bug	    | Debug                |
|-----------|----------------------|
| Database stopped working due to information in one of the fields not fitting the data model | Ran python3 manage.py flush to delete all information in database |
| Error message of "'decimal.Decimal' object is not iterable" being returned when trying to use context processor to add up cart item total | There was a return statement in my function in contexts.py which meant the contexts where not being rendered correctly.  Cart total now works correctly.
| Quantity increase and decrease buttons were not disabling below 1 and above 99 as per js | The classes which the js used to identify the buttons were named as the wrong variable names 