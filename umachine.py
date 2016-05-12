import os
import mmap
import struct

# Make sure that native sizes (as used by memoryview.cast()) have expected size
assert struct.calcsize("H") == 2
assert struct.calcsize("I") == 4


class PhysMem:

    def __init__(self, access_sz=None):
        self.fd = os.open("/dev/mem", os.O_RDWR)
        self.access_sz = access_sz
        self.mmap = None
        self.mv = None
        self.offset = None
        self.mmap_size = 65536
        self.map(0)

    def map(self, addr):
        self.offset = addr & ~0xfff
        self.mmap = mmap.mmap(self.fd, self.mmap_size, offset=self.offset)
        if self.access_sz == 1:
            self.mv = self.mmap
        else:
            self.mv = memoryview(self.mmap).cast("H" if self.access_sz == 2 else "I")

    def winoff(self, addr):
        off = addr - self.offset
        if not(0 <= off <= self.mmap_size):
            self.map(addr)
            off = addr - self.offset
        return off

    def __getitem__(self, addr):
        off = self.winoff(addr)
        return self.mv[off // self.access_sz]

    def __setitem__(self, addr, val):
        off = self.winoff(addr)
        self.mv[off // self.access_sz] = val


mem8 = PhysMem(1)
mem16 = PhysMem(2)
mem32 = PhysMem(4)
