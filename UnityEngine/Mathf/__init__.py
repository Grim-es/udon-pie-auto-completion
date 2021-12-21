from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Mathf:
    def __new__(cls, arg1=None):
        '''
        :returns: Mathf
        :rtype: UnityEngine.Mathf
        '''
        pass

    @staticmethod
    def get_Epsilon():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_PI():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_Infinity():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_NegativeInfinity():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_Deg2Rad():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_Rad2Deg():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def ClosestPowerOfTwo(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def IsPowerOfTwo(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def NextPowerOfTwo(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GammaToLinearSpace(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def LinearToGammaSpace(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def CorrelatedColorTemperatureToRGB(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def FloatToHalf(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    def HalfToFloat(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def PerlinNoise(arg1, arg2):
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
    def Sin(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Cos(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Tan(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Asin(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Acos(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Atan(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Atan2(arg1, arg2):
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
    def Sqrt(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Abs(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Abs(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Abs(arg1=None):
        pass

    @staticmethod
    @overload
    def Min(arg1, arg2):
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
    def Min(arg1):
        '''
        :param arg1: SingleArray
        :type arg1: System.SingleArray
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Min(arg1, arg2):
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
    @overload
    def Min(arg1):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Min(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def Max(arg1, arg2):
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
    def Max(arg1):
        '''
        :param arg1: SingleArray
        :type arg1: System.SingleArray
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Max(arg1, arg2):
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
    @overload
    def Max(arg1):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Max(arg1=None, arg2=None):
        pass

    @staticmethod
    def Pow(arg1, arg2):
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
    def Exp(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Log(arg1, arg2):
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
    def Log(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Log(arg1=None, arg2=None):
        pass

    @staticmethod
    def Log10(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Ceil(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Floor(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Round(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def CeilToInt(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def FloorToInt(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def RoundToInt(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Sign(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Clamp(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Clamp(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Clamp(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def Clamp01(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Lerp(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def LerpUnclamped(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def LerpAngle(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def MoveTowards(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def MoveTowardsAngle(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def SmoothStep(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Gamma(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Approximately(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SmoothDamp(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: SingleRef.SingleRef
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def SmoothDamp(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: SingleRef.SingleRef
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def SmoothDamp(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: SingleRef.SingleRef
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def SmoothDamp(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def SmoothDampAngle(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: SingleRef.SingleRef
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def SmoothDampAngle(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: SingleRef.SingleRef
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def SmoothDampAngle(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: SingleRef.SingleRef
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def SmoothDampAngle(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    def Repeat(arg1, arg2):
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
    def PingPong(arg1, arg2):
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
    def InverseLerp(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def DeltaAngle(arg1, arg2):
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
