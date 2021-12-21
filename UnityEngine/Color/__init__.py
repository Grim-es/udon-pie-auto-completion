from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Color:
    def __new__(cls, arg1=None):
        '''
        :returns: Color
        :rtype: UnityEngine.Color
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
        :returns: Color
        :rtype: UnityEngine.Color
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
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def ctor(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def op_Addition(arg1, arg2):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Color
        :type arg2: UnityEngine.Color
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def op_Subtraction(arg1, arg2):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Color
        :type arg2: UnityEngine.Color
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def op_Multiply(arg1, arg2):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Color
        :type arg2: UnityEngine.Color
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def op_Multiply(arg1, arg2):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def op_Multiply(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Color
        :type arg2: UnityEngine.Color
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def op_Multiply(arg1=None, arg2=None):
        pass

    @staticmethod
    def op_Division(arg1, arg2):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Color
        :type arg2: UnityEngine.Color
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Color
        :type arg2: UnityEngine.Color
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def op_Implicit(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
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
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def op_Implicit(arg1=None):
        pass

    @staticmethod
    def get_r():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_r():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_g():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_g():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_b():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_b():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_a():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_a():
        '''
        :returns: Single
        :rtype: System.Single
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
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None):
        pass

    @staticmethod
    def Lerp(arg1, arg2, arg3):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Color
        :type arg2: UnityEngine.Color
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def LerpUnclamped(arg1, arg2, arg3):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Color
        :type arg2: UnityEngine.Color
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_red():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_green():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_blue():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_white():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_black():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_yellow():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_cyan():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_magenta():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_gray():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_grey():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_clear():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_grayscale():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_linear():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_gamma():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_maxColorComponent():
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
    def RGBToHSV(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Undefined variable
        :type arg2: SingleRef.SingleRef
        :param arg3: Undefined variable
        :type arg3: SingleRef.SingleRef
        :param arg4: Undefined variable
        :type arg4: SingleRef.SingleRef
        '''
        pass

    @staticmethod
    @overload
    def HSVToRGB(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def HSVToRGB(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Boolean
        :type arg4: System.Boolean or bool
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def HSVToRGB(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
