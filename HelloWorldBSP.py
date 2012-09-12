"""

Basic Hello World BSP, in Hama this is called serialize printing.
Each task sends its peer name to each other task who reads the
message and outputs it to console.

"""
from BSP import BSP

class HelloWorldBSP(BSP):
    def bsp(self, peer):
        for i in range(15):
            for otherPeer in peer.getAllPeerNames():
                peer.send(otherPeer, "Hello from " + peer.getPeerName() + " in superstep " + i)
            peer.sync()

        for msg in peer.getCurrentMessage():
            if not msg:
                break
            peer.log(msg)


