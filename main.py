# 線形合同法
class LinearCongruentialGenerator:
    def __init__(self, a: int, c: int, module: int, seed: int):
        # readonly
        self.a = a % module
        self.c = c % module
        self.module = module
        self.seed = seed

        # state
        self.index = 0
        self.value = seed

        self.tmp_index = -1
        self.tmp_value = -1

    def generate(self) -> int:
        self.index += 1
        self.value = (self.a * self.value + self.c) % self.module
        return self.value

    def reset(self):
        self.index = 0
        self.value = self.seed

    def save(self):
        self.tmp_index = self.index
        self.tmp_value = self.value

    def recall(self):
        if self.tmp_index == -1 or self.tmp_value == -1:
            return

        self.index = self.tmp_index
        self.value = self.tmp_value

    def get_period(self) -> int:
        initial_index = self.index
        initial_value = self.value

        self.reset()
        while True:
            next = self.generate()
            if next == self.seed:
                period = self.index
                self.index = initial_index
                self.value = initial_value
                return period
