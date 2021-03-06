"""
Abstract representation of objects and relations.

"""

class AObject(object):
    """
    An object, aka model or table, with a list of fields
    """

    def __init__(self, name="", color=None, shape=None):
        self.name = name
        self.fields = []
        self.color = color or (1, 1, 1)
        self.shape = shape or "Rectangle"

    def add_field(self, name="", type="", field=None):
        """
        supply either name and type, OR field
        @param field: AField
        @return: the AField that was added
        """
        if field:
            f = field
        else:
            f = AField(name, type)
        self.fields.append(f)
        return f

class AField(object):
    """
    A relation to another object
    """

    def __init__(self, name="", type="", dest=None):
        """
        @param dest: AObject
        """
        self.name = name
        self.type = type
        self.dest = dest

    def set_destination(self, dest):
        """
        @param dest: AObject
        """
        self.dest = dest
