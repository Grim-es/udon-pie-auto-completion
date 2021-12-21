from UdonPie import System
from UdonPie import UnityEngine
from UdonPie import VRC
from UdonPie.Undefined import *


class TrackingData:
    def __new__(cls, arg1=None):
        '''
        :returns: TrackingData
        :rtype: VRC.SDKBase.VRCPlayerApi.TrackingData
        '''
        pass

    @staticmethod
    def ctor(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :returns: VRCPlayerApi+TrackingData
        :rtype: VRC.VRCPlayerApi+TrackingData
        '''
        pass

    @staticmethod
    def get_position():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_position():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_rotation():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def set_rotation():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
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
    def ToString():
        '''
        :returns: String
        :rtype: System.String
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
