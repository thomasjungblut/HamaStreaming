"""

Main Runner utility that will get the bsp class from the user, passed via args and start
it with the whole context and stuff.

"""
import sys
from BSPPeer import BSPPeer

className = sys.argv[1]
module = __import__(className)
class_ = getattr(module, className)

bspInstance = class_()

peer = BSPPeer(bspInstance)
peer.runSetup()
peer.runBSP()
peer.runCleanup()
peer.done()