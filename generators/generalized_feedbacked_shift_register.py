import numpy as np


# (3項)線形帰還シフトレジスタ
# x_{i+n} = x_{i+m} + x_i (mod 2)
class GeneralizedFeedbackedShiftRegister:
    def __init__(self, n: int, m: int, seed: list[int]):
        # validation
        if m <= 0:
            raise ValueError("m must be greater than 0")
        if n <= m:
            raise ValueError("n must be greater than m")
        if len(seed) == 0:
            raise ValueError("seed must not be empty")

        # readonly
        self.n = n
        self.m = m
        self.seed = np.array(seed, dtype=int)

        # state
        self.value = self.seed.copy()

        self.saved_value = np.array([], dtype=int)

    def generate(self) -> np.ndarray:
        x_i = self.value & 1
        x_im = (self.value >> self.m) & 1
        x_in = x_im ^ x_i
        self.value = (self.value >> 1) | (x_in << (self.n - 1))
        return x_in

    def reset(self):
        self.value = self.seed

    def save(self):
        self.saved_value = self.value

    def recall(self):
        if self.saved_value.size == 0:
            return

        self.value = self.saved_value
