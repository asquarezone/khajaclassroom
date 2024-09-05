"""This module has classes for theatre related stufff
"""


class Seat:
    """This class represents a seat"""

    def __init__(self, row, number) -> None:
        self.row = row
        self.number = number


class Screen:
    """This class represents screen"""

    def __init__(self, name):
        self.name = name
        self.seats = []

    def add_seat(self, seat):
        """_summary_

        Args:
            seat (_type_): _description_
        """
        self.seats.append(seat)


class Theatre:
    """Theatre"""

    def __init__(self, name):
        self.name = name
        self.screens = []

    def add_screen(self, screen):
        """_summary_

        Args:
            screen (_type_): _description_
        """
        self.screens.append(screen)
