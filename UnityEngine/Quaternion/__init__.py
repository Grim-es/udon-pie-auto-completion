from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Quaternion:
    def __new__(cls, arg1=None):
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def ctor(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    @overload
    def op_Multiply(arg1, arg2):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    @overload
    def op_Multiply(arg1, arg2):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def op_Multiply(arg1=None, arg2=None):
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_x():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_x():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_y():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_y():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_z():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_z():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_w():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_w():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_kEpsilon():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def FromToRotation(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def Inverse(arg1):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def Slerp(arg1, arg2, arg3):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def SlerpUnclamped(arg1, arg2, arg3):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def Lerp(arg1, arg2, arg3):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def LerpUnclamped(arg1, arg2, arg3):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def AngleAxis(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    @overload
    def LookRotation(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    @overload
    def LookRotation(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def LookRotation(arg1=None, arg2=None):
        pass

    @staticmethod
    def get_Item(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_Item(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    def Set(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    def get_identity():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def Dot(arg1, arg2):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def SetLookRotation(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def SetLookRotation(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def SetLookRotation(arg1=None, arg2=None):
        pass

    @staticmethod
    def Angle(arg1, arg2):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_eulerAngles():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_eulerAngles(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def Euler(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    @overload
    def Euler(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def Euler(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def ToAngleAxis(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: SingleRef.SingleRef
        :param arg2: Undefined variable
        :type arg2: Vector3Ref.Vector3Ref
        '''
        pass

    @staticmethod
    def SetFromToRotation(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def RotateTowards(arg1, arg2, arg3):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    @overload
    def Normalize(arg1):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    @overload
    def Normalize():
        pass

    @staticmethod
    def Normalize(arg1=None):
        pass

    @staticmethod
    def get_normalized():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
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
    @overload
    def Equals(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None):
        pass

    @staticmethod
    @overload
    def ToString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ToString(arg1=None):
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
