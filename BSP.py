"""

BSP Class that can be overridden to implement the computation logic.

"""
from BSPPeer import BSPPeer

class BSP:

    def __init__(self):
        pass

    def setup(self, peer):
        pass

    def bsp(self, peer):
        pass

    def cleanup(self, peer):
        pass