class XorShift32:
    _BIT_MASK = 2**32 - 1

    def __init__(self, seed: int):
        self.state = seed & self._BIT_MASK

    def generate(self):
        state = self.state
        state = state ^ state << 15 & self._BIT_MASK
        state = state ^ state >> 17
        state = state ^ state << 13 & self._BIT_MASK
        self.state = state
        return self.state
