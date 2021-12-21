from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Random:
    def __new__(cls, arg1=None):
        '''
        :returns: Random
        :rtype: UnityEngine.Random
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: Random
        :rtype: UnityEngine.Random
        '''
        pass

    @staticmethod
    def InitState(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def Range(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Range(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Range(arg1=None, arg2=None):
        pass

    @staticmethod
    def get_value():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_insideUnitSphere():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_insideUnitCircle():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_onUnitSphere():
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
    def get_rotationUniform():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    @overload
    def ColorHSV():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def ColorHSV(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def ColorHSV(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def ColorHSV(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def ColorHSV(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Single
        :type arg7: System.Single or float
        :param arg8: Single
        :type arg8: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def ColorHSV(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None):
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
