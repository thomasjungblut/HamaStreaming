"""

Basic Hello World BSP, in Hama this is called serialize printing.
Each task sends its peer name to each other task who reads the
message and outputs it to console.

"""
from BSP import BSP

class HelloWorldBSP(BSP):
    def bsp(self, peer):
        name = peer.getPeerName()
        for i in range(15):
            for otherPeer in peer.getAllPeerNames():
                peer.send(otherPeer, ("Hello from " + name + " in superstep " + str(i)))
            peer.sync()
            for msg in peer.getAllMessages():
                peer.log(msg)


