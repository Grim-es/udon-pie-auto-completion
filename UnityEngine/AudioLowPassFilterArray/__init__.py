from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class AudioLowPassFilterArray:
    def __new__(cls, arg1=None):
        '''
        :returns: AudioLowPassFilterArray
        :rtype: UnityEngine.AudioLowPassFilterArray
        '''
        pass

    def __setitem__(self, key, value):
        '''
        :param key: Int32
        :type key: System.Int32 or int
        :param value: AudioLowPassFilter
        :type value: UnityEngine.AudioLowPassFilter
        '''
        pass

    def __getitem__(self, key):
        '''
        :param key: Int32
        :type key: System.Int32 or int
        :returns: AudioLowPassFilter
        :rtype: UnityEngine.AudioLowPassFilter
        '''
        pass

    @staticmethod
    def ctor(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: AudioLowPassFilterArray
        :rtype: UnityEngine.AudioLowPassFilterArray
        '''
        pass

    @staticmethod
    def Set(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: AudioLowPassFilter
        :type arg2: UnityEngine.AudioLowPassFilter
        '''
        pass

    @staticmethod
    def Get(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: AudioLowPassFilter
        :rtype: UnityEngine.AudioLowPassFilter
        '''
        pass

    @staticmethod
    @overload
    def GetValue(arg1):
        '''
        :param arg1: Int32Array
        :type arg1: System.Int32Array
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    @overload
    def GetValue(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    @overload
    def GetValue(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    @overload
    def GetValue(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    @overload
    def GetValue(arg1):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    @overload
    def GetValue(arg1, arg2):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :param arg2: Int64
        :type arg2: System.Int64
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    @overload
    def GetValue(arg1, arg2, arg3):
        '''
        :param arg1: Int64
        :type arg1: System.Int64
        :param arg2: Int64
        :type arg2: System.Int64
        :param arg3: Int64
        :type arg3: System.Int64
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    @overload
    def GetValue(arg1):
        '''
        :param arg1: Int64Array
        :type arg1: System.Int64Array
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    def GetValue(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def SetValue(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetValue(arg1, arg2, arg3):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetValue(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetValue(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Int32Array
        :type arg2: System.Int32Array
        '''
        pass

    @staticmethod
    @overload
    def SetValue(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Int64
        :type arg2: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def SetValue(arg1, arg2, arg3):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Int64
        :type arg2: System.Int64
        :param arg3: Int64
        :type arg3: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def SetValue(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Int64
        :type arg2: System.Int64
        :param arg3: Int64
        :type arg3: System.Int64
        :param arg4: Int64
        :type arg4: System.Int64
        '''
        pass

    @staticmethod
    @overload
    def SetValue(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Int64Array
        :type arg2: System.Int64Array
        '''
        pass

    @staticmethod
    def SetValue(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def GetLongLength(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    def get_SyncRoot():
        '''
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    def get_IsReadOnly():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_IsFixedSize():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_IsSynchronized():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Clone():
        '''
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    @overload
    def CopyTo(arg1, arg2):
        '''
        :param arg1: Array
        :type arg1: System.Array
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def CopyTo(arg1, arg2):
        '''
        :param arg1: Array
        :type arg1: System.Array
        :param arg2: Int64
        :type arg2: System.Int64
        '''
        pass

    @staticmethod
    def CopyTo(arg1=None, arg2=None):
        pass

    @staticmethod
    def GetEnumerator():
        '''
        :returns: IEnumerator
        :rtype: System.IEnumerator
        '''
        pass

    @staticmethod
    def get_LongLength():
        '''
        :returns: Int64
        :rtype: System.Int64
        '''
        pass

    @staticmethod
    def Initialize():
        pass

    @staticmethod
    def get_Length():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetLength(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_Rank():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetUpperBound(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetLowerBound(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
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

    @staticmethod
    def ToString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass
