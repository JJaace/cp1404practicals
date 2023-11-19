"""Estimate: 2 hours
   Actual: 3 hours"""


class Band:
    """Represents a band."""

    def __init__(self, name=""):
        """Initialise a Band"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        result = []
        for musician in self.musicians:
            musician_str = f"{musician.name} ("
            instruments_str = ', '.join(str(instrument) for instrument in musician.instruments)
            musician_str += f"[{instruments_str}]" if musician.instruments else "[]"
            musician_str += ")"
            result.append(musician_str)
        return f"{self.name} ({', '.join(result)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing whether the musician is playing or needs an instrument"""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)
