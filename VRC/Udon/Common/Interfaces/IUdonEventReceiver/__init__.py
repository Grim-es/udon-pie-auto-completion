from UdonPie import System
from UdonPie import VRC
from UdonPie.Undefined import *


class IUdonEventReceiver:
    def __new__(cls, arg1=None):
        '''
        :returns: IUdonEventReceiver
        :rtype: VRC.Udon.Common.Interfaces.IUdonEventReceiver
        '''
        pass

    @staticmethod
    def SendCustomEvent(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def SendCustomNetworkEvent(arg1, arg2):
        '''
        :param arg1: NetworkEventTarget
        :type arg1: VRC.NetworkEventTarget
        :param arg2: String
        :type arg2: System.String or str
        '''
        pass

    @staticmethod
    def SetProgramVariable(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Object
        :type arg2: System.Object
        '''
        pass

    @staticmethod
    def GetProgramVariable(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Object
        :rtype: System.Object
        '''
        pass
