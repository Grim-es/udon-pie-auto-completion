from typing import overload

from UdonPie import System
from UdonPie.Undefined import *


class Convert:
    def __new__(cls, arg1=None):
        '''
        :returns: Convert
        :rtype: System.Convert
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def ToBoolean(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def ToBoolean(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    @overload
    def ToChar(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    def ToChar(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    @overload
    def ToSByte(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: SByte
        :rtype: System.SByte
        '''
        pass

    @staticmethod
    def ToSByte(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    @overload
    def ToByte(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Byte
        :rtype: System.Byte
        '''
        pass

    @staticmethod
    def ToByte(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    @overload
    def ToInt16(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    def ToInt16(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    @overload
    def ToUInt16(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: UInt16
        :rtype: System.UInt16
        '''
        pass

    @staticmethod
    def ToUInt16(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToInt32(arg1, arg2):
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
    def ToInt32(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    @overload
    def ToUInt32(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    def ToUInt32(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def ToInt64(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    def ToInt64(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    @overload
    def ToUInt64(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: UInt64
        :rtype: System.UInt64
        '''
        pass

    @staticmethod
    def ToUInt64(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1, arg2):
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
    def ToSingle(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def ToSingle(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def ToSingle(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    @overload
    def ToDouble(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Double
        :rtype: System.Double
        '''
        pass

    @staticmethod
    def ToDouble(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    @overload
    def ToDecimal(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: Decimal
        :rtype: System.Decimal
        '''
        pass

    @staticmethod
    def ToDecimal(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1, arg2):
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
    def ToDateTime(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    @overload
    def ToDateTime(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: DateTime
        :rtype: System.DateTime
        '''
        pass

    @staticmethod
    def ToDateTime(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
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
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Char
        :type arg1: System.Char
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: SByte
        :type arg1: System.SByte
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: UInt16
        :type arg1: System.UInt16
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: UInt64
        :type arg1: System.UInt64
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Double
        :type arg1: System.Double
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Decimal
        :type arg1: System.Decimal
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: DateTime
        :type arg1: System.DateTime
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
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
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Byte
        :type arg1: System.Byte
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
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
    def ToString(arg1, arg2):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToString(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: IFormatProvider
        :type arg2: System.IFormatProvider
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
    def ToString(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ToBase64String(arg1):
        '''
        :param arg1: ByteArray
        :type arg1: System.ByteArray
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToBase64String(arg1, arg2):
        '''
        :param arg1: ByteArray
        :type arg1: System.ByteArray
        :param arg2: Base64FormattingOptions
        :type arg2: System.Base64FormattingOptions
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    @overload
    def ToBase64String(arg1, arg2, arg3):
        '''
        :param arg1: ByteArray
        :type arg1: System.ByteArray
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
    def ToBase64String(arg1, arg2, arg3, arg4):
        '''
        :param arg1: ByteArray
        :type arg1: System.ByteArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Base64FormattingOptions
        :type arg4: System.Base64FormattingOptions
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def ToBase64String(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def ToBase64CharArray(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: ByteArray
        :type arg1: System.ByteArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: CharArray
        :type arg4: System.CharArray
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def ToBase64CharArray(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: ByteArray
        :type arg1: System.ByteArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: CharArray
        :type arg4: System.CharArray
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Base64FormattingOptions
        :type arg6: System.Base64FormattingOptions
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def ToBase64CharArray(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    def FromBase64String(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: ByteArray
        :rtype: System.ByteArray
        '''
        pass

    @staticmethod
    def FromBase64CharArray(arg1, arg2, arg3):
        '''
        :param arg1: CharArray
        :type arg1: System.CharArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: ByteArray
        :rtype: System.ByteArray
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
