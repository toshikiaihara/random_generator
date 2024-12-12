class XorShift128Plus:
    _STATE_BIT_MASK = 2**128 - 1
    _OUTPUT_MASK = 2**64 - 1

    def __init__(self, seed1: int, seed2: int, a: int = 23, b: int = 18, c: int = 5):
        self.state = [
            seed1 & self._STATE_BIT_MASK,
            seed2 & self._STATE_BIT_MASK,
        ]
        self.a = a
        self.b = b
        self.c = c

    def __xorshift(self, value: int, direction: str, shift_amount: int):
        if shift_amount <= 0:
            raise ValueError("Shift amount must be greater than 0")

        if direction == "left":
            return value ^ (value << shift_amount) & self._STATE_BIT_MASK
        elif direction == "right":
            return value ^ (value >> shift_amount)
        raise ValueError(f"Invalid direction: {direction}")

    def generate(self, output_format: str | None = None):
        old_s0, old_s1 = self.state
        output = (old_s0 + old_s1) & self._OUTPUT_MASK

        self.state[0] = old_s1
        old_s0_ILa = self.__xorshift(old_s0, "left", self.a)
        old_s0_ILa_IRb = self.__xorshift(old_s0_ILa, "right", self.b)
        old_s1_IRc = self.__xorshift(old_s1, "right", self.c)
        self.state[1] = old_s0_ILa_IRb ^ old_s1_IRc

        if output_format == "unit":
            return output / self._OUTPUT_MASK

        return output
