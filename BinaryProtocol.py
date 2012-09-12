"""

Binary protocol to communicate with the Java BSP task via streams.

"""

class BinaryProtocol:
    START = 0
    SET_BSPJOB_CONF = 1
    SET_INPUT_TYPES = 2
    RUN_SETUP = 3
    RUN_BSP = 4
    RUN_CLEANUP = 5
    READ_KEYVALUE = 6
    WRITE_KEYVALUE = 7
    GET_MSG = 8
    GET_MSG_COUNT = 9
    SEND_MSG = 10
    SYNC = 11
    GET_ALL_PEERNAME = 12
    GET_PEERNAME = 13
    GET_PEER_INDEX = 14
    GET_PEER_COUNT = 15
    GET_SUPERSTEP_COUNT = 16
    REOPEN_INPUT = 17
    CLEAR = 18
    CLOSE = 19
    ABORT = 20
    DONE = 21
    TASK_DONE = 22
    REGISTER_COUNTER = 23
    INCREMENT_COUNTER = 24
    LOG = 25

    @staticmethod
    def getProtocolString(opCode):
        return "%" + str(opCode) + "%=\n";

    @staticmethod
    def getProtocolStringNL(opCode):
        return "%" + str(opCode) + "%=";

    @staticmethod
    def getAckProtocolString(opCode):
        return "%ACK_" + str(opCode) + "%=\n";

