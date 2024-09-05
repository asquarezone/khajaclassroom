"""This module represents the Movie
"""


class Movie:
    """Movie class"""

    def __init__(self, title, language):
        """Initialization of movie

        Args:
            title (str): title of the move
            language (str): language
        """
        self._title = title
        self._language = language

    @property
    def title(self):
        """Get title"""
        return self._title

    @property
    def language(self):
        """Get Language"""
        return self._language

    def __str__(self) -> str:
        return f"{self.title} - {self.language}"


class User:
    """User class
    """
    def __init__(self, username, email) -> None:
        self.username= username
        self.email = email