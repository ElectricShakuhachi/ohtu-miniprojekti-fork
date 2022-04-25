class ReadingTip:

    """Class that represents the reading tip."""

    def __init__(self, identifier=None, title=None, reading_type=None,
                author=None, isbn=None, url=None, description=None, comment=None, status=None):
        self.id = identifier
        self.title = title
        self.author = author
        self.type = reading_type
        self.isbn = isbn
        self.url = url
        self.description = description
        self.comment = comment
        self.related_courses = []
        self.status = str(status)

    def format(self, seperator=", ") -> str:
        """Formats the reading tip values to a string using the specified seperator (default ", ").
        """
        values = []
        attributes = {"Id": self.id, "Title": self.title, "Type": self.type, "Author": self.author, "URL": self.url, "Status": self.status}
        for key, attr in attributes.items():
            if attr:
                values.append(": ".join([key, attr]))
        return seperator.join(values)

    def __str__(self):
        return self.format()
