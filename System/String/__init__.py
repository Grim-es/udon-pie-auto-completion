from typing import overload

from UdonPie import System
from UdonPie.Undefined import *


class String:
    def __new__(cls, arg1=None):
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCharAsterix.SystemCharAsterix
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCharAsterix.SystemCharAsterix
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemSByteAsterix.SystemSByteAsterix
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemSByteAsterix.SystemSByteAsterix
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemSByteAsterix.SystemSByteAsterix
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Undefined variable
        :type arg4: SystemTextEncoding.SystemTextEncoding
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ctor(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def op_Addition(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_Empty():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Join(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: StringArray
        :type arg2: System.StringArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Join(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: ObjectArray
        :type arg2: System.ObjectArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Join(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericIEnumerable.SystemCollectionsGenericIEnumerable
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Join(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericIEnumerable.SystemCollectionsGenericIEnumerable
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Join(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: StringArray
        :type arg2: System.StringArray
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def Join(arg1=None, arg2=None, arg3=None, arg4=None):
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
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: StringComparison
        :type arg2: System.StringComparison
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: StringComparison
        :type arg3: System.StringComparison
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def get_Chars(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    def CopyTo(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: CharArray
        :type arg2: System.CharArray
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def ToCharArray():
        '''
        :returns: CharArray
        :rtype: System.CharArray
        '''
        pass

    @staticmethod
    @overload
    def ToCharArray(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: CharArray
        :rtype: System.CharArray
        '''
        pass

    @staticmethod
    def ToCharArray(arg1=None, arg2=None):
        pass

    @staticmethod
    def IsNullOrEmpty(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsNullOrWhiteSpace(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
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
    def get_Length():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Split(arg1):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def Split(arg1, arg2):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def Split(arg1, arg2):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :param arg2: StringSplitOptions
        :type arg2: System.StringSplitOptions
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def Split(arg1, arg2, arg3):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: StringSplitOptions
        :type arg3: System.StringSplitOptions
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def Split(arg1, arg2):
        '''
        :param arg1: StringArray
        :type arg1: System.StringArray
        :param arg2: StringSplitOptions
        :type arg2: System.StringSplitOptions
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def Split(arg1, arg2, arg3):
        '''
        :param arg1: StringArray
        :type arg1: System.StringArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: StringSplitOptions
        :type arg3: System.StringSplitOptions
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    def Split(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def Substring(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Substring(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def Substring(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def Trim(arg1):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Trim():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def Trim(arg1=None):
        pass

    @staticmethod
    def TrimStart(arg1):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def TrimEnd(arg1):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def IsNormalized():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsNormalized(arg1):
        '''
        :param arg1: NormalizationForm
        :type arg1: System.NormalizationForm
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsNormalized(arg1=None):
        pass

    @staticmethod
    @overload
    def Normalize():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Normalize(arg1):
        '''
        :param arg1: NormalizationForm
        :type arg1: System.NormalizationForm
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def Normalize(arg1=None):
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: StringComparison
        :type arg3: System.StringComparison
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: CultureInfo
        :type arg3: System.CultureInfo
        :param arg4: CompareOptions
        :type arg4: System.CompareOptions
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        :param arg4: CultureInfo
        :type arg4: System.CultureInfo
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Boolean
        :type arg6: System.Boolean or bool
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Boolean
        :type arg6: System.Boolean or bool
        :param arg7: CultureInfo
        :type arg7: System.CultureInfo
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: CultureInfo
        :type arg6: System.CultureInfo
        :param arg7: CompareOptions
        :type arg7: System.CompareOptions
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Compare(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: StringComparison
        :type arg6: System.StringComparison
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Compare(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
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
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CompareTo(arg1=None):
        pass

    @staticmethod
    @overload
    def CompareOrdinal(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CompareOrdinal(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CompareOrdinal(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def Contains(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def EndsWith(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def EndsWith(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: StringComparison
        :type arg2: System.StringComparison
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def EndsWith(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :param arg3: CultureInfo
        :type arg3: System.CultureInfo
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def EndsWith(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def IndexOf(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IndexOf(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IndexOf(arg1, arg2, arg3):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IndexOf(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IndexOf(arg1, arg2):
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
    @overload
    def IndexOf(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IndexOf(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: StringComparison
        :type arg2: System.StringComparison
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IndexOf(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: StringComparison
        :type arg3: System.StringComparison
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IndexOf(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: StringComparison
        :type arg4: System.StringComparison
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def IndexOf(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def IndexOfAny(arg1):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IndexOfAny(arg1, arg2):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IndexOfAny(arg1, arg2, arg3):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def IndexOfAny(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def LastIndexOf(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LastIndexOf(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LastIndexOf(arg1, arg2, arg3):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LastIndexOf(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LastIndexOf(arg1, arg2):
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
    @overload
    def LastIndexOf(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LastIndexOf(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: StringComparison
        :type arg2: System.StringComparison
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LastIndexOf(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: StringComparison
        :type arg3: System.StringComparison
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LastIndexOf(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: StringComparison
        :type arg4: System.StringComparison
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def LastIndexOf(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def LastIndexOfAny(arg1):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LastIndexOfAny(arg1, arg2):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LastIndexOfAny(arg1, arg2, arg3):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def LastIndexOfAny(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def PadLeft(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def PadLeft(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Char
        :type arg2: System.Char
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def PadLeft(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def PadRight(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def PadRight(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Char
        :type arg2: System.Char
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def PadRight(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def StartsWith(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def StartsWith(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: StringComparison
        :type arg2: System.StringComparison
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def StartsWith(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :param arg3: CultureInfo
        :type arg3: System.CultureInfo
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def StartsWith(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def ToLower():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToLower(arg1):
        '''
        :param arg1: CultureInfo
        :type arg1: System.CultureInfo
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ToLower(arg1=None):
        pass

    @staticmethod
    def ToLowerInvariant():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToUpper():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToUpper(arg1):
        '''
        :param arg1: CultureInfo
        :type arg1: System.CultureInfo
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ToUpper(arg1=None):
        pass

    @staticmethod
    def ToUpperInvariant():
        '''
        :returns: String
        :rtype: System.String
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
    def Clone():
        '''
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    def Insert(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: String
        :type arg2: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Replace(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: Char
        :type arg2: System.Char
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Replace(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def Replace(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def Remove(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Remove(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def Remove(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def Format(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Object
        :type arg2: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Format(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Object
        :type arg2: System.Object
        :param arg3: Object
        :type arg3: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Format(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Object
        :type arg2: System.Object
        :param arg3: Object
        :type arg3: System.Object
        :param arg4: Object
        :type arg4: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Format(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: ObjectArray
        :type arg2: System.ObjectArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Format(arg1, arg2, arg3):
        '''
        :param arg1: IFormatProvider
        :type arg1: System.IFormatProvider
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: Object
        :type arg3: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Format(arg1, arg2, arg3, arg4):
        '''
        :param arg1: IFormatProvider
        :type arg1: System.IFormatProvider
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: Object
        :type arg3: System.Object
        :param arg4: Object
        :type arg4: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Format(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: IFormatProvider
        :type arg1: System.IFormatProvider
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: Object
        :type arg3: System.Object
        :param arg4: Object
        :type arg4: System.Object
        :param arg5: Object
        :type arg5: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Format(arg1, arg2, arg3):
        '''
        :param arg1: IFormatProvider
        :type arg1: System.IFormatProvider
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: ObjectArray
        :type arg3: System.ObjectArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def Format(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def Copy(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1, arg2, arg3):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: System.Object
        :param arg3: Object
        :type arg3: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: System.Object
        :param arg3: Object
        :type arg3: System.Object
        :param arg4: Object
        :type arg4: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1):
        '''
        :param arg1: ObjectArray
        :type arg1: System.ObjectArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericIEnumerable.SystemCollectionsGenericIEnumerable
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericIEnumerable.SystemCollectionsGenericIEnumerable
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: String
        :type arg3: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: String
        :type arg4: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def Concat(arg1):
        '''
        :param arg1: StringArray
        :type arg1: System.StringArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def Concat(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def Intern(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def IsInterned(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def GetTypeCode():
        '''
        :returns: TypeCode
        :rtype: System.TypeCode
        '''
        pass

    @staticmethod
    def GetEnumerator():
        '''
        :returns: CharEnumerator
        :rtype: System.CharEnumerator
        '''
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
