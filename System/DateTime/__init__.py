from typing import overload

from UdonPie import System
from UdonPie.Undefined import *


class DateTime:
    def __new__(cls, arg1=None):
        '''
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :param arg2: DateTimeKind
        :type arg2: System.DateTimeKind
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Undefined variable
        :type arg4: SystemGlobalizationCalendar.SystemGlobalizationCalendar
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: DateTimeKind
        :type arg7: System.DateTimeKind
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Undefined variable
        :type arg7: SystemGlobalizationCalendar.SystemGlobalizationCalendar
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: DateTimeKind
        :type arg8: System.DateTimeKind
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: Undefined variable
        :type arg8: SystemGlobalizationCalendar.SystemGlobalizationCalendar
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: Undefined variable
        :type arg8: SystemGlobalizationCalendar.SystemGlobalizationCalendar
        :param arg9: DateTimeKind
        :type arg9: System.DateTimeKind
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def ctor(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None):
        pass

    @staticmethod
    def op_Addition(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: TimeSpan
        :type arg2: System.TimeSpan
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def op_Subtraction(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: TimeSpan
        :type arg2: System.TimeSpan
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def op_Subtraction(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTime
        :type arg2: System.DateTime
        :returns: TimeSpan
        :rtype: System.TimeSpan
        '''
        pass

    @staticmethod
    def op_Subtraction(arg1=None, arg2=None):
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTime
        :type arg2: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTime
        :type arg2: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_LessThan(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTime
        :type arg2: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_LessThanOrEqual(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTime
        :type arg2: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_GreaterThan(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTime
        :type arg2: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_GreaterThanOrEqual(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTime
        :type arg2: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_MinValue():
        '''
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def get_MaxValue():
        '''
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def Add(arg1):
        '''
        :param arg1: TimeSpan
        :type arg1: System.TimeSpan
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def AddDays(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def AddHours(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def AddMilliseconds(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def AddMinutes(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def AddMonths(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def AddSeconds(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def AddTicks(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def AddYears(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def Compare(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTime
        :type arg2: System.DateTime
        :returns: Int32
        :rtype: System.Int32
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
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CompareTo(arg1=None):
        pass

    @staticmethod
    def DaysInMonth(arg1, arg2):
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
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTime
        :type arg2: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None, arg2=None):
        pass

    @staticmethod
    def FromBinary(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def FromFileTime(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def FromFileTimeUtc(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def FromOADate(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def IsDaylightSavingTime():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def SpecifyKind(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: DateTimeKind
        :type arg2: System.DateTimeKind
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def ToBinary():
        '''
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    def get_Date():
        '''
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def get_Day():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_DayOfWeek():
        '''
        :returns: DayOfWeek
        :rtype: System.DayOfWeek
        '''
        pass

    @staticmethod
    def get_DayOfYear():
        '''
        :returns: Int32
        :rtype: System.Int32
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
    def get_Hour():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_Kind():
        '''
        :returns: DateTimeKind
        :rtype: System.DateTimeKind
        '''
        pass

    @staticmethod
    def get_Millisecond():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_Minute():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_Month():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_Now():
        '''
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def get_UtcNow():
        '''
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def get_Second():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_Ticks():
        '''
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    def get_TimeOfDay():
        '''
        :returns: TimeSpan
        :rtype: System.TimeSpan
        '''
        pass

    @staticmethod
    def get_Today():
        '''
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def get_Year():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def IsLeapYear(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Parse(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: DateTime
        :rtype: System.DateTime
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
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def Parse(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :param arg3: DateTimeStyles
        :type arg3: System.DateTimeStyles
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def Parse(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def ParseExact(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: IFormatProvider
        :type arg3: System.IFormatProvider
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ParseExact(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: IFormatProvider
        :type arg3: System.IFormatProvider
        :param arg4: DateTimeStyles
        :type arg4: System.DateTimeStyles
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ParseExact(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: StringArray
        :type arg2: System.StringArray
        :param arg3: IFormatProvider
        :type arg3: System.IFormatProvider
        :param arg4: DateTimeStyles
        :type arg4: System.DateTimeStyles
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def ParseExact(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def Subtract(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: TimeSpan
        :rtype: System.TimeSpan
        '''
        pass

    @staticmethod
    @overload
    def Subtract(arg1):
        '''
        :param arg1: TimeSpan
        :type arg1: System.TimeSpan
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def Subtract(arg1=None):
        pass

    @staticmethod
    def ToOADate():
        '''
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    def ToFileTime():
        '''
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    def ToFileTimeUtc():
        '''
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    def ToLocalTime():
        '''
        :returns: DateTime
        :rtype: System.DateTime
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
    def ToUniversalTime():
        '''
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def TryParse(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Undefined variable
        :type arg2: DateTimeRef.DateTimeRef
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
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :param arg3: DateTimeStyles
        :type arg3: System.DateTimeStyles
        :param arg4: Undefined variable
        :type arg4: DateTimeRef.DateTimeRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def TryParse(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def GetDateTimeFormats():
        '''
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def GetDateTimeFormats(arg1):
        '''
        :param arg1: IFormatProvider
        :type arg1: System.IFormatProvider
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def GetDateTimeFormats(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def GetDateTimeFormats(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    def GetDateTimeFormats(arg1=None, arg2=None):
        pass

    @staticmethod
    def ToLongDateString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ToLongTimeString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ToShortTimeString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def TryParseExact(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: IFormatProvider
        :type arg3: System.IFormatProvider
        :param arg4: DateTimeStyles
        :type arg4: System.DateTimeStyles
        :param arg5: Undefined variable
        :type arg5: DateTimeRef.DateTimeRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def TryParseExact(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: StringArray
        :type arg2: System.StringArray
        :param arg3: IFormatProvider
        :type arg3: System.IFormatProvider
        :param arg4: DateTimeStyles
        :type arg4: System.DateTimeStyles
        :param arg5: Undefined variable
        :type arg5: DateTimeRef.DateTimeRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def TryParseExact(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def ToShortDateString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
