from typing import overload

from UdonPie import System
from UdonPie.Undefined import *


class Char:
    def __new__(cls, arg1=None):
        '''
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    def op_Addition(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def op_Subtraction(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def op_Multiplication(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def op_Division(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def op_UnaryMinus(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_LessThan(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_GreaterThan(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_LessThanOrEqual(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_GreaterThanOrEqual(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_LeftShift(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def op_RightShift(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def op_LogicalAnd(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def op_LogicalOr(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def op_LogicalXor(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_MaxValue():
        '''
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    def get_MinValue():
        '''
        :returns: Char
        :rtype: System.Char
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
        :param arg1: Char
        :type arg1: System.Char
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
        :param arg1: Char
        :type arg1: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CompareTo(arg1=None):
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
        :param arg1: Char
        :type arg1: System.Char
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ToString(arg1=None):
        pass

    @staticmethod
    def Parse(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    def TryParse(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: CharRef.CharRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsDigit(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsDigit(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsDigit(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsLetter(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsLetter(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsLetter(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsWhiteSpace(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsWhiteSpace(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsWhiteSpace(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsUpper(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsUpper(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsUpper(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsLower(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsLower(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsLower(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsPunctuation(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsPunctuation(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsPunctuation(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsLetterOrDigit(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsLetterOrDigit(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsLetterOrDigit(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToUpper(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: CultureInfo
        :type arg2: System.CultureInfo
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToUpper(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    def ToUpper(arg1=None, arg2=None):
        pass

    @staticmethod
    def ToUpperInvariant(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToLower(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: CultureInfo
        :type arg2: System.CultureInfo
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToLower(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    def ToLower(arg1=None, arg2=None):
        pass

    @staticmethod
    def ToLowerInvariant(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def IsControl(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsControl(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsControl(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsNumber(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsNumber(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsNumber(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsSeparator(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsSeparator(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsSeparator(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsSurrogate(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsSurrogate(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsSurrogate(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsSymbol(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsSymbol(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsSymbol(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetUnicodeCategory(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: UnicodeCategory
        :rtype: System.UnicodeCategory
        '''
        pass

    @staticmethod
    @overload
    def GetUnicodeCategory(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: UnicodeCategory
        :rtype: System.UnicodeCategory
        '''
        pass

    @staticmethod
    def GetUnicodeCategory(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetNumericValue(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def GetNumericValue(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    def GetNumericValue(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsHighSurrogate(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsHighSurrogate(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsHighSurrogate(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsLowSurrogate(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsLowSurrogate(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsLowSurrogate(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsSurrogatePair(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsSurrogatePair(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsSurrogatePair(arg1=None, arg2=None):
        pass

    @staticmethod
    def ConvertFromUtf32(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ConvertToUtf32(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ConvertToUtf32(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def ConvertToUtf32(arg1=None, arg2=None):
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
