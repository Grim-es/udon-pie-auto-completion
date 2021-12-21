from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class AnimatorOverrideController:
    def __new__(cls, arg1=None):
        '''
        :returns: AnimatorOverrideController
        :rtype: UnityEngine.AnimatorOverrideController
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
    def get_runtimeAnimatorController():
        '''
        :returns: RuntimeAnimatorController
        :rtype: UnityEngine.RuntimeAnimatorController
        '''
        pass

    @staticmethod
    def set_runtimeAnimatorController(arg1):
        '''
        :param arg1: RuntimeAnimatorController
        :type arg1: UnityEngine.RuntimeAnimatorController
        '''
        pass

    @staticmethod
    @overload
    def get_Item(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: AnimationClip
        :rtype: UnityEngine.AnimationClip
        '''
        pass

    @staticmethod
    @overload
    def get_Item(arg1):
        '''
        :param arg1: AnimationClip
        :type arg1: UnityEngine.AnimationClip
        :returns: AnimationClip
        :rtype: UnityEngine.AnimationClip
        '''
        pass

    @staticmethod
    def get_Item(arg1=None):
        pass

    @staticmethod
    @overload
    def set_Item(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: AnimationClip
        :type arg2: UnityEngine.AnimationClip
        '''
        pass

    @staticmethod
    @overload
    def set_Item(arg1, arg2):
        '''
        :param arg1: AnimationClip
        :type arg1: UnityEngine.AnimationClip
        :param arg2: AnimationClip
        :type arg2: UnityEngine.AnimationClip
        '''
        pass

    @staticmethod
    def set_Item(arg1=None, arg2=None):
        pass

    @staticmethod
    def get_overridesCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetOverrides(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def ApplyOverrides(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericIList.SystemCollectionsGenericIList
        '''
        pass

    @staticmethod
    def get_animationClips():
        '''
        :returns: AnimationClipArray
        :rtype: UnityEngine.AnimationClipArray
        '''
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
