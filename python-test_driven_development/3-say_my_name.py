>>> say_my_name = __import__('3-say_my_name').say_my_name


>>> say_my_name("megema", "jackson")
My name is umugabo Mugisha

Check wrong value for first name
>>> say_my_name(2005, "megema")
Traceback (most recent call last):
        ...
TypeError: first_name must be a string

>>> say_my_name(None, "megema")
Traceback (most recent call last):
        ...
TypeError: first_name must be a string

Check wrong value for last name
>>> say_my_name("muyizeye", 1990)
Traceback (most recent call last):
        ...
TypeError: last_name must be a string

Check missing arguments
>>> say_my_name()
Traceback (most recent call last):
	...
TypeError: say_my_name() missing 1 required positional argument: 'first_name'
 
