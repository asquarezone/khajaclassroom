"""Ticketing classes
"""


class Screening:
    """_summary_"""

    def __init__(self, theatre, movie) -> None:
        self.theatre = theatre
        self.movie = movie

    def add_showtime(self, screen_index, show_time):
        """_summary_

        Args:
            screen_index (_type_): _description_
            show_time (_type_): _description_
        """


class Booking:
    """_summary_"""

    def book_ticket(self, user, screening, seat, payment):
        """_summary_

        Args:
            user (_type_): _description_
            screening (_type_): _description_
            seat (_type_): _description_
            payment (_type_): _description_
        """


class Payment:
    """_summary_"""

    def payment_done(self, user, amount):
        """_summary_

        Args:
            user (_type_): _description_
            amount (_type_): _description_
        """
