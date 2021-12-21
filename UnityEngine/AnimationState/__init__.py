from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class AnimationState:
    def __new__(cls, arg1=None):
        '''
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: UnityEngineTrackedReference.UnityEngineTrackedReference
        :param arg2: Undefined variable
        :type arg2: UnityEngineTrackedReference.UnityEngineTrackedReference
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: UnityEngineTrackedReference.UnityEngineTrackedReference
        :param arg2: Undefined variable
        :type arg2: UnityEngineTrackedReference.UnityEngineTrackedReference
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Implicit(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: UnityEngineTrackedReference.UnityEngineTrackedReference
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_enabled():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_enabled(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
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
    def set_weight(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_wrapMode():
        '''
        :returns: WrapMode
        :rtype: UnityEngine.WrapMode
        '''
        pass

    @staticmethod
    def set_wrapMode(arg1):
        '''
        :param arg1: WrapMode
        :type arg1: UnityEngine.WrapMode
        '''
        pass

    @staticmethod
    def get_time():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_time(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_normalizedTime():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_normalizedTime(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_speed():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_speed(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_normalizedSpeed():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_normalizedSpeed(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
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
    def get_layer():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_layer(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
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
    @overload
    def AddMixingTransform(arg1, arg2):
        '''
        :param arg1: Transform
        :type arg1: UnityEngine.Transform
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def AddMixingTransform(arg1):
        '''
        :param arg1: Transform
        :type arg1: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def AddMixingTransform(arg1=None, arg2=None):
        pass

    @staticmethod
    def RemoveMixingTransform(arg1):
        '''
        :param arg1: Transform
        :type arg1: UnityEngine.Transform
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
    def get_blendMode():
        '''
        :returns: AnimationBlendMode
        :rtype: UnityEngine.AnimationBlendMode
        '''
        pass

    @staticmethod
    def set_blendMode(arg1):
        '''
        :param arg1: AnimationBlendMode
        :type arg1: UnityEngine.AnimationBlendMode
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
