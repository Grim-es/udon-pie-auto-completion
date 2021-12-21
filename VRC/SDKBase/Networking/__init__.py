from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie import VRC
from UdonPie.Undefined import *


class Networking:
    def __new__(cls, arg1=None):
        '''
        :returns: Networking
        :rtype: VRC.SDKBase.Networking
        '''
        pass

    @staticmethod
    def get():
        pass

    @staticmethod
    def set():
        pass

    @staticmethod
    def get_IsNetworkSettled():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_IsMaster():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_LocalPlayer():
        '''
        :returns: VRCPlayerApi
        :rtype: VRC.VRCPlayerApi
        '''
        pass

    @staticmethod
    @overload
    def IsOwner(arg1, arg2):
        '''
        :param arg1: VRCPlayerApi
        :type arg1: VRC.VRCPlayerApi
        :param arg2: GameObject
        :type arg2: UnityEngine.GameObject
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsOwner(arg1):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsOwner(arg1=None, arg2=None):
        pass

    @staticmethod
    def GetOwner(arg1):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        :returns: VRCPlayerApi
        :rtype: VRC.VRCPlayerApi
        '''
        pass

    @staticmethod
    def SetOwner(arg1, arg2):
        '''
        :param arg1: VRCPlayerApi
        :type arg1: VRC.VRCPlayerApi
        :param arg2: GameObject
        :type arg2: UnityEngine.GameObject
        '''
        pass

    @staticmethod
    def IsObjectReady(arg1):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Destroy(arg1):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        '''
        pass

    @staticmethod
    def GetUniqueName(arg1):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def GetNetworkDateTime():
        '''
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def GetServerTimeInSeconds():
        '''
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    def GetServerTimeInMilliseconds():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CalculateServerDeltaTime(arg1, arg2):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :param arg2: Double
        :type arg2: System.Double
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    def Equals(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetHashCode():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass

    @staticmethod
    def ToString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass
