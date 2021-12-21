from typing import overload

from UdonPie import System
from UdonPie.Undefined import *


class TimeZoneInfo:
    def __new__(cls, arg1=None):
        '''
        :returns: TimeZoneInfo
        :rtype: System.TimeZoneInfo
        '''
        pass

    @staticmethod
    def get_Id():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_DisplayName():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_StandardName():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_DaylightName():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_BaseUtcOffset():
        '''
        :returns: TimeSpan
        :rtype: System.TimeSpan
        '''
        pass

    @staticmethod
    def get_SupportsDaylightSavingTime():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetAdjustmentRules():
        '''
        :returns: TimeZoneInfo+AdjustmentRuleArray
        :rtype: System.TimeZoneInfo+AdjustmentRuleArray
        '''
        pass

    @staticmethod
    @overload
    def GetAmbiguousTimeOffsets(arg1):
        '''
        :param arg1: DateTimeOffset
        :type arg1: System.DateTimeOffset
        :returns: TimeSpanArray
        :rtype: System.TimeSpanArray
        '''
        pass

    @staticmethod
    @overload
    def GetAmbiguousTimeOffsets(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: TimeSpanArray
        :rtype: System.TimeSpanArray
        '''
        pass

    @staticmethod
    def GetAmbiguousTimeOffsets(arg1=None):
        pass

    @staticmethod
    @overload
    def GetUtcOffset(arg1):
        '''
        :param arg1: DateTimeOffset
        :type arg1: System.DateTimeOffset
        :returns: TimeSpan
        :rtype: System.TimeSpan
        '''
        pass

    @staticmethod
    @overload
    def GetUtcOffset(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: TimeSpan
        :rtype: System.TimeSpan
        '''
        pass

    @staticmethod
    def GetUtcOffset(arg1=None):
        pass

    @staticmethod
    @overload
    def IsAmbiguousTime(arg1):
        '''
        :param arg1: DateTimeOffset
        :type arg1: System.DateTimeOffset
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsAmbiguousTime(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsAmbiguousTime(arg1=None):
        pass

    @staticmethod
    @overload
    def IsDaylightSavingTime(arg1):
        '''
        :param arg1: DateTimeOffset
        :type arg1: System.DateTimeOffset
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsDaylightSavingTime(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsDaylightSavingTime(arg1=None):
        pass

    @staticmethod
    def IsInvalidTime(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def ClearCachedData():
        pass

    @staticmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(arg1, arg2):
        '''
        :param arg1: DateTimeOffset
        :type arg1: System.DateTimeOffset
        :param arg2: String
        :type arg2: System.String or str
        :returns: DateTimeOffset
        :rtype: System.DateTimeOffset
        '''
        pass

    @staticmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: String
        :type arg2: System.String or str
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(arg1, arg2, arg3):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: String
        :type arg3: System.String or str
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def ConvertTimeBySystemTimeZoneId(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def ConvertTime(arg1, arg2):
        '''
        :param arg1: DateTimeOffset
        :type arg1: System.DateTimeOffset
        :param arg2: TimeZoneInfo
        :type arg2: System.TimeZoneInfo
        :returns: DateTimeOffset
        :rtype: System.DateTimeOffset
        '''
        pass

    @staticmethod
    @overload
    def ConvertTime(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: TimeZoneInfo
        :type arg2: System.TimeZoneInfo
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ConvertTime(arg1, arg2, arg3):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: TimeZoneInfo
        :type arg2: System.TimeZoneInfo
        :param arg3: TimeZoneInfo
        :type arg3: System.TimeZoneInfo
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def ConvertTime(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def ConvertTimeFromUtc(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: TimeZoneInfo
        :type arg2: System.TimeZoneInfo
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ConvertTimeToUtc(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ConvertTimeToUtc(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: TimeZoneInfo
        :type arg2: System.TimeZoneInfo
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def ConvertTimeToUtc(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def Equals(arg1):
        '''
        :param arg1: TimeZoneInfo
        :type arg1: System.TimeZoneInfo
        :returns: Boolean
        :rtype: System.Boolean
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
    def Equals(arg1=None):
        pass

    @staticmethod
    def FromSerializedString(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: TimeZoneInfo
        :rtype: System.TimeZoneInfo
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
    def HasSameRules(arg1):
        '''
        :param arg1: TimeZoneInfo
        :type arg1: System.TimeZoneInfo
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_Local():
        '''
        :returns: TimeZoneInfo
        :rtype: System.TimeZoneInfo
        '''
        pass

    @staticmethod
    def ToSerializedString():
        '''
        :returns: String
        :rtype: System.String
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
    def get_Utc():
        '''
        :returns: TimeZoneInfo
        :rtype: System.TimeZoneInfo
        '''
        pass

    @staticmethod
    @overload
    def CreateCustomTimeZone(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: TimeSpan
        :type arg2: System.TimeSpan
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: String
        :type arg4: System.String or str
        :returns: TimeZoneInfo
        :rtype: System.TimeZoneInfo
        '''
        pass

    @staticmethod
    @overload
    def CreateCustomTimeZone(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: TimeSpan
        :type arg2: System.TimeSpan
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: String
        :type arg4: System.String or str
        :param arg5: String
        :type arg5: System.String or str
        :param arg6: AdjustmentRuleArray
        :type arg6: System.AdjustmentRuleArray
        :returns: TimeZoneInfo
        :rtype: System.TimeZoneInfo
        '''
        pass

    @staticmethod
    @overload
    def CreateCustomTimeZone(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: TimeSpan
        :type arg2: System.TimeSpan
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: String
        :type arg4: System.String or str
        :param arg5: String
        :type arg5: System.String or str
        :param arg6: AdjustmentRuleArray
        :type arg6: System.AdjustmentRuleArray
        :param arg7: Boolean
        :type arg7: System.Boolean or bool
        :returns: TimeZoneInfo
        :rtype: System.TimeZoneInfo
        '''
        pass

    @staticmethod
    def CreateCustomTimeZone(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    def GetSystemTimeZones():
        '''
        :returns: ReadOnlyCollection
        :rtype: System.ReadOnlyCollection
        '''
        pass

    @staticmethod
    def FindSystemTimeZoneById(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: TimeZoneInfo
        :rtype: System.TimeZoneInfo
        '''
        pass

    @staticmethod
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
