from typing import overload

from UdonPie import System
from UdonPie.Undefined import *


class Single:
    def __new__(cls, arg1=None):
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def op_Addition(arg1, arg2):
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
    def op_Subtraction(arg1, arg2):
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
    def op_Multiplication(arg1, arg2):
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
    def op_Division(arg1, arg2):
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
    def op_UnaryMinus(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
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
    def op_Inequality(arg1, arg2):
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
    def op_LessThan(arg1, arg2):
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
    def op_GreaterThan(arg1, arg2):
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
    def op_LessThanOrEqual(arg1, arg2):
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
    def op_GreaterThanOrEqual(arg1, arg2):
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
    def op_Remainder(arg1, arg2):
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
    def get_MinValue():
        '''
        :returns: Single
        :rtype: System.Single
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
    def get_MaxValue():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_PositiveInfinity():
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
    def get_NaN():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def IsInfinity(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsPositiveInfinity(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsNegativeInfinity(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsNaN(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CompareTo(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CompareTo(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CompareTo(arg1=None):
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
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None):
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
        :param arg1: IFormatProvider
        :type arg1: System.IFormatProvider
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
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ToString(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def Parse(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Parse(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: NumberStyles
        :type arg2: System.NumberStyles
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Parse(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Parse(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: NumberStyles
        :type arg2: System.NumberStyles
        :param arg3: IFormatProvider
        :type arg3: System.IFormatProvider
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Parse(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def TryParse(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SingleRef.SingleRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def TryParse(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: NumberStyles
        :type arg2: System.NumberStyles
        :param arg3: IFormatProvider
        :type arg3: System.IFormatProvider
        :param arg4: Undefined variable
        :type arg4: SingleRef.SingleRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def TryParse(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
