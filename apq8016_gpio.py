from umachine import mem32

class Pin:

    def __init__(self, no):
        # Set base address to TLMM_GPIO_IN_OUT register,
        # as get/set is the most common operation
        self.addr = 0x01000000 + 0x1000 * no + 4

    def value(self, v=None):
        if v is None:
            return mem32[self.addr] & 1
        mem32[self.addr] = v << 1

    #
    # The additional methods below show why high() and low()
    # operations should be in basis of any efficient GPIO
    # API - they translate to a single machine instruction
    # (unlike methods like .set(0_or_1)).
    #

    def high(self):
        mem32[self.addr] = 2

    def low(self):
        mem32[self.addr] = 0
