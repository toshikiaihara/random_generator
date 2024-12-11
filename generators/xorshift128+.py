class XorShift128Plus:
    _128BIT_MASK = 0xFFFFFFFFFFFFFFFF

    def __init__(self, seed1: int, seed2: int, a: int = 23, b: int = 18, c: int = 5):
        self.state = [
            seed1 & self._128BIT_MASK,
            seed2 & self._128BIT_MASK,
        ]
        self.a = a
        self.b = b
        self.c = c

    def generate(self):
        old_s0 = self.state[0]
        old_s1 = self.state[1]
        result = (old_s0 + old_s1) & self._128BIT_MASK

        self.state[0] = old_s1
        old_s0_ILa = old_s0 ^ (old_s0 << self.a) & self._128BIT_MASK
        old_s0_ILa_IRb = old_s0_ILa ^ (old_s0_ILa >> self.b)
        old_s1_IRc = old_s1 ^ (old_s1 >> self.c)
        self.state[1] = old_s0_ILa_IRb ^ old_s1_IRc

        return result
