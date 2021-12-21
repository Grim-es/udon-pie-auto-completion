from typing import overload

from UdonPie import System
from UdonPie.Undefined import *


class Boolean:
    def __new__(cls, arg1=None):
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_LogicalAnd(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_LogicalOr(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_LogicalXor(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_ConditionalAnd(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_ConditionalOr(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_ConditionalXor(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_UnaryNegation(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_TrueString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_FalseString():
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
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None):
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
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CompareTo(arg1=None):
        pass

    @staticmethod
    def Parse(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
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
    def ToString(arg1=None):
        pass

    @staticmethod
    def TryParse(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: BooleanRef.BooleanRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
