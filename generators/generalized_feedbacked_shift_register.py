# 線形帰還シフトレジスタ
# x_{i+n} = x_{i+m} + x_i (mod 2)
class GeneralizedFeedbackedShiftRegister:
    def __init__(self, n: int, m: int, seed: int):
        # validation
        if n <= m:
            raise ValueError("n must be greater than m")
        if m <= 0:
            raise ValueError("m must be greater than 0")

        # readonly
        self.n = n
        self.m = m
        self.seed = seed

        # state
        self.value = seed

        self.saved_value = -1

    def generate(self) -> int:
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
        if self.saved_value == -1:
            return

        self.value = self.saved_value
