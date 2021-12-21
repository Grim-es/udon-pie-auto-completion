from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class AudioClip:
    def __new__(cls, arg1=None):
        '''
        :returns: AudioClip
        :rtype: UnityEngine.AudioClip
        '''
        pass

    @staticmethod
    def op_Implicit(arg1):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_length():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_samples():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_channels():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_frequency():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_loadType():
        '''
        :returns: AudioClipLoadType
        :rtype: UnityEngine.AudioClipLoadType
        '''
        pass

    @staticmethod
    def LoadAudioData():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def UnloadAudioData():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_preloadAudioData():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_ambisonic():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_loadState():
        '''
        :returns: AudioDataLoadState
        :rtype: UnityEngine.AudioDataLoadState
        '''
        pass

    @staticmethod
    def get_loadInBackground():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetData(arg1, arg2):
        '''
        :param arg1: SingleArray
        :type arg1: System.SingleArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def SetData(arg1, arg2):
        '''
        :param arg1: SingleArray
        :type arg1: System.SingleArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Create(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Boolean
        :type arg5: System.Boolean or bool
        :returns: AudioClip
        :rtype: UnityEngine.AudioClip
        '''
        pass

    @staticmethod
    @overload
    def Create(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Boolean
        :type arg5: System.Boolean or bool
        :param arg6: PCMReaderCallback
        :type arg6: UnityEngine.PCMReaderCallback
        :returns: AudioClip
        :rtype: UnityEngine.AudioClip
        '''
        pass

    @staticmethod
    @overload
    def Create(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Boolean
        :type arg5: System.Boolean or bool
        :param arg6: PCMReaderCallback
        :type arg6: UnityEngine.PCMReaderCallback
        :param arg7: PCMSetPositionCallback
        :type arg7: UnityEngine.PCMSetPositionCallback
        :returns: AudioClip
        :rtype: UnityEngine.AudioClip
        '''
        pass

    @staticmethod
    def Create(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    def GetInstanceID():
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
    def Equals(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_name():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def set_name(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
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
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
