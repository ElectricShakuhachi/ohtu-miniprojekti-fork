from repositories.reading_tip_repository import (
    ReadingTipRepository as default_reading_tip_repository
    )
from entities.reading_tip import ReadingTip

class ReadingTipService:
    """Class encapsulating the business logic such as exposed to the application.

       This class is responsible for validating and sanitizing parameters to be valid the
       for underlying data storage.
    """
    def __init__(self, reading_tip_repository=default_reading_tip_repository):
        self._reading_tip_repository = reading_tip_repository

    def create(self, title: str, author=None, link=None,
                description=None, comment=None, status=str):
        """Adds a new tip with given fields to the underlying repository.

           Raises an exception if given fields do not follow the validation rules.
        """
        self.validate_title(title)

        reading_tip = ReadingTip(title=title, author=author, url=link,
                                 description=description, comment=comment, status=status)

        created_row = self._reading_tip_repository.create(reading_tip)

        if created_row is False:
            raise Exception("Failed to add a new reading tip!")

        return created_row


    def delete(self, tip_id):
        """Delete selected reading tip by id
        """
        self._reading_tip_repository.delete(tip_id)

    def get_all(self):
        """Returns all reading tips from the underlying repository.
        """
        return self._reading_tip_repository.get_all()
    
    def get_unread(self):
        """Returns all unread reading tips from the underlying repository.
        """
        return self._reading_tip_repository.get_unread()

    def search_by_title(self, tip_title):
        """Returns reading tips by found from the underlying repository by given title.

           If no tips were found from the repository, returns None.
        """
        return self._reading_tip_repository.search_by_title(tip_title)

    def get_by_id(self, tip_id) -> ReadingTip:
        """Returns reading tip by given id from the underlying repository.

           If reading tip on given id does not exist in the repository, returns None.
        """
        return self._reading_tip_repository.get_by_id(tip_id)

    def update(self, new_reading_tip: ReadingTip) -> bool:
        """Updates given reading tip fields in the underlying repository.
        """
        # Validate the fields of the new reading tip object
        self.validate_title(new_reading_tip.title)
        self._reading_tip_repository.update(new_reading_tip)

    def update_status(self, reading_tip_status: ReadingTip) -> bool:
        self._reading_tip_repository.update_status(reading_tip_status)

    def validate_title(self, title):
        # Remove whitespace from the start and end of the title
        title = title.strip()
        if len(title) == 0:
            raise Exception("Reading tip cannot have a empty title!")

        if len(title) > 200:
            raise Exception("Reading tip length cannot exceed 200 characters!")

    def get_ids(self, reading_tips):
        ids = []
        for tip in reading_tips:
            ids.append(tip.id)
        return ids
