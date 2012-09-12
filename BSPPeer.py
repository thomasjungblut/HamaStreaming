"""

The BSPPeer handles the incoming protocol requests and forwards it to the BSP class.
Basically you can register the to be executed BSP class into this peer,
it will then callback the according methods.

"""
from BspJobConfiguration import BspJobConfiguration
from sys import stdin
from sys import stdout
from BinaryProtocol import BinaryProtocol as bp

class BSPPeer:
    PROTOCOL_VERSION = 0

    def __init__(self, bspClass):
        self.config = BspJobConfiguration()
        self.bspClass = bspClass;
        self.initialize()

    def initialize(self):
        """
        INIT protocol works as follows:
        START OP_CODE
        PROTOCOL_NUMBER
        SET_BSPJOB_CONF OP_CODE
        NUMBER OF CONF ITEMS (#KEY + #VALUES)
        N-LINES, where line is key and the following the value
        """

        self.log("HELLO FROM PYTHON OMG!")
        # parse our initial values
        line = stdin.readline()
        self.log("LINE: " + line)
        # start code is the first
        if line == bp.getProtocolString(bp.START):
            # check the protocol compatibility
            protocolNumber = int(stdin.readline())
            if protocolNumber != self.PROTOCOL_VERSION:
                raise RuntimeError(
                    "Protocol version mismatch: Expected: " + str(self.PROTOCOL_VERSION) +
                    " but got: " + str(protocolNumber))
        line = stdin.readline()
        self.log("LINE: " + line)
        # parse the configurations
        if line == bp.getProtocolString(bp.SET_BSPJOB_CONF):
            numberOfItems = stdin.readline()
            key = None
            value = None
            for i in range(0, int(numberOfItems), 2):
                key = stdin.readline()
                value = stdin.readline()
                self.config.put(key, value)

        self.ack(bp.START)

    def send(self, peer, msg):
        println(bp.getProtocolString(bp.SEND_MSG))
        println(peer)
        println(msg)


    def getCurrentMessage(self):
        println(bp.getProtocolString(bp.GET_MSG))
        line = stdin.readline()
        # if no message is send it will send %%-1%%
        if line == "%%-1%%\n":
            return -1

        return line;


    def getNumCurrentMessages(self):
        println(bp.getProtocolString(bp.GET_MSG_COUNT))
        return stdin.readline()


    def sync(self):
        println(bp.getProtocolString(bp.SYNC))
        # this should block now until we get a response
        line = stdin.readline()
        if line != (bp.getProtocolString(bp.SYNC) + "_SUCCESS\n"):
            raise RuntimeError(
                "Barrier sync failed!")


    def getSuperstepCount(self):
        println(bp.getProtocolString(bp.GET_SUPERSTEP_COUNT))
        return stdin.readline()


    def getPeerName(self):
        return self.getPeername(self, -1)


    def getPeerName(self, index):
        println(bp.getProtocolString(bp.GET_PEERNAME))
        println(index);
        return stdin.readline()


    def getPeerIndex(self):
        println(bp.getProtocolString(bp.GET_PEER_INDEX))
        return stdin.readline()


    def getAllPeerNames(self):
        println(bp.getProtocolString(bp.GET_ALL_PEERNAME))
        ln = stdin.readline()
        self.log("allpeernames " + ln)
        names = []
        for i in range(int(ln)):
            self.log("in the loop ")
            peerName = stdin.readLine # TODO WHY IS THIS BLOCKING SO HARD?
            self.log("peername " + peerName)
            names.append(peerName)
        self.log("allpeernames " + names)
        return names


    def getNumPeers(self):
        println(bp.getProtocolString(bp.GET_PEER_COUNT))
        return stdin.readline()


    def clear(self):
        println(bp.getProtocolString(bp.CLEAR))


    def write(self, key, value):
        println(bp.getProtocolString(bp.WRITE_KEYVALUE))
        println(key)
        println(value)


    def readNext(self):
        println(bp.getProtocolString(bp.READ_KEYVALUE))
        line = stdin.readline()
        secondLine = stdin.readline()
        # if no message is send it will send %%-1%%
        if line == "%%-1%%\n" and secondLine == "%%-1%%\n":
            return -1
        return [line, secondLine]


    def reopenInput(self):
        println(bp.getProtocolString(bp.REOPEN_INPUT))


    # TODO counter!

    def runSetup(self):
        self.log("Starting setup!")
        line = stdin.readline()
        self.log("read: " + line)
        # start code is the first
        if line.startswith(bp.getProtocolString(bp.RUN_SETUP)):
            self.bspClass.setup(self);
            self.ack(bp.RUN_SETUP)


    def runBSP(self):
        self.log("Starting BSP!")
        line = stdin.readline()
        self.log("read: " + line)
        # start code is the first
        if line.startswith(bp.getProtocolString(bp.RUN_BSP)):
            self.bspClass.bsp(self);
            self.ack(bp.RUN_BSP)


    def runCleanup(self):
        self.log("Starting cleanup!")
        line = stdin.readline()
        self.log("read: " + line)
        # start code is the first
        if line.startswith(bp.getProtocolString(bp.RUN_CLEANUP)):
            self.bspClass.cleanup(self);
            self.ack(bp.RUN_CLEANUP)


    def ack(self, code):
        println(bp.getAckProtocolString(code))


    def done(self):
        println(bp.getProtocolString(bp.TASK_DONE))
        println(bp.getProtocolString(bp.DONE))


    def log(self, msg):
        println(bp.getProtocolStringNL(bp.LOG) + msg)


def println(text):
    if "\n" in text:
        print(text)
    else:
        print(text + "\n")
    stdout.flush()
