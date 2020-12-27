class Borg:
    """Borg class making class attributes global"""
    _shared_state = {}  # Attribute dictionary
    def __init__(self):
        # Make it an attributr dictionary
        self.__dict__ = self._shared_state

class Singleton(Borg): # Inherits from the borg class
    """This class noe shares all its attributes among its various instance"""
    # this essenstially makes the singleton objects an object oriented global variables

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)


#  Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
# Print the object
print(x)

# Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym
y = Singleton(SNMP="Simple Network Management Protocol")
# Print the object
print(y)
