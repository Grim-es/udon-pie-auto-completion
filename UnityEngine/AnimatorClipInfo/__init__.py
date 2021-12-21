from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class AnimatorClipInfo:
    def __new__(cls, arg1=None):
        '''
        :returns: AnimatorClipInfo
        :rtype: UnityEngine.AnimatorClipInfo
        '''
        pass

    @staticmethod
    def get_clip():
        '''
        :returns: AnimationClip
        :rtype: UnityEngine.AnimationClip
        '''
        pass

    @staticmethod
    def get_weight():
        '''
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
