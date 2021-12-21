from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Vector4:
    def __new__(cls, arg1=None):
        '''
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
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
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def ctor(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def op_Addition(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def op_Subtraction(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def op_UnaryNegation(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def op_Multiply(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def op_Multiply(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def op_Multiply(arg1=None, arg2=None):
        pass

    @staticmethod
    def op_Division(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def op_Implicit(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def op_Implicit(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def op_Implicit(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def op_Implicit(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def op_Implicit(arg1=None):
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
    def Lerp(arg1, arg2, arg3):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def LerpUnclamped(arg1, arg2, arg3):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def MoveTowards(arg1, arg2, arg3):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def Scale(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    @overload
    def Scale(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def Scale(arg1=None, arg2=None):
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
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None):
        pass

    @staticmethod
    @overload
    def Normalize(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
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
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def Dot(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Project(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def Distance(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Magnitude(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_magnitude():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_sqrMagnitude():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Min(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def Max(arg1, arg2):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :param arg2: Vector4
        :type arg2: UnityEngine.Vector4
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def get_zero():
        '''
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def get_one():
        '''
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def get_positiveInfinity():
        '''
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
        pass

    @staticmethod
    def get_negativeInfinity():
        '''
        :returns: Vector4
        :rtype: UnityEngine.Vector4
        '''
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
    @overload
    def SqrMagnitude(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def SqrMagnitude():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def SqrMagnitude(arg1=None):
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
