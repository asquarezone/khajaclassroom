"""
investment.py

This module contains the base implementation of investment
"""


class Investment:
    """Investment Class is used represent an investment
    This contains operations to calculate investment returns

    Attributes:
        amount (float): investment amount
        returns_rate (float): returns rate 12% => 12
        time (int): time in years

    """

    def __init__(self, amount, returns_rate, time):
        """Initializes the investment

        Args:
            amount (float): investment amount
            returns_rate (float): returns rate 12% => 12
            time (int): time in years
        """
        self._amount = amount
        self._returns_rate = returns_rate
        self._time = time

    @property
    def amount(self):
        """Getter Property for amount

        Returns:
            float: investment amount
        """
        return self._amount

    @property
    def returns_rate(self):
        """Get Returns Rate

        Returns:
            float: returns rate
        """
        return self._returns_rate

    @property
    def time(self):
        """Get investment time

        Returns:
            int: time in years
        """
        return self._time

    def calculate(self):
        """This method calculates the investement returns

        Returns:
            float: value after investment
        """
        pass


class FixedDeposit(Investment):
    """This is Fixed Deposit investment"""

    def calculate(self):
        """This method calculates FD Returns

        Returns:
            float: total value post investment
        """
        returns = self.returns_rate/100
        total_amount = self.amount * (1 + returns) ** self.time
        return total_amount


class SIP(Investment):
    """This represents Monthly SIP returns"""

    def calculate(self):
        """This method calculates monthly sip
        investment returns

        Returns:
            float: total value post investment
        """
        months = self.time * 12
        yearly_returns = self.returns_rate/100
        returns = yearly_returns/12
        total_amount = (
            self.amount
            * (((1 + returns) ** months - 1) / returns)
            * (1 + returns)
        )
        return total_amount
