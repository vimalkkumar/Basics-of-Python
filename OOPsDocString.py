class Demo:
    """
    docString inside the class

    Attributes:
        title(str) : the title
    """
    def __init__(self, title):
        """
        Demo init method for

        Args:
            title (str) : initialise the title attributes
        :param title:
        """
        self.title = title


#  Raw Literals introduction

raw_string = "This is \n the format \t\t of the raw string"
print(raw_string)

raw_string = r"This is \n the format \t\t of the raw string"
print(raw_string)

b_string = "This is" + chr(10) + "the format" + chr(9) + chr(9) + "of the raw string"
print(b_string)