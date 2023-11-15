"""Estimate: 1 hour
   Actual: 1 hour 40 minutes"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represents a silver service taxi"""
    FLAGFALL = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a silver service taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a silver service taxi."""
        return f"{super().__str__()} including a flagfall of ${self.FLAGFALL:.2f}"

    def get_fare(self):
        """Get the current fare."""
        return self.FLAGFALL + super().get_fare()
