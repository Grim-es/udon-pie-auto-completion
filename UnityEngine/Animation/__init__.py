from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Animation:
    def __new__(cls, arg1=None):
        '''
        :returns: Animation
        :rtype: UnityEngine.Animation
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
    def get_clip():
        '''
        :returns: AnimationClip
        :rtype: UnityEngine.AnimationClip
        '''
        pass

    @staticmethod
    def set_clip(arg1):
        '''
        :param arg1: AnimationClip
        :type arg1: UnityEngine.AnimationClip
        '''
        pass

    @staticmethod
    def get_playAutomatically():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_playAutomatically(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
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
    @overload
    def Stop():
        pass

    @staticmethod
    @overload
    def Stop(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def Stop(arg1=None):
        pass

    @staticmethod
    @overload
    def Rewind(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    @overload
    def Rewind():
        pass

    @staticmethod
    def Rewind(arg1=None):
        pass

    @staticmethod
    def Sample():
        pass

    @staticmethod
    def get_isPlaying():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsPlaying(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_Item(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    @overload
    def Play():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Play(arg1):
        '''
        :param arg1: PlayMode
        :type arg1: UnityEngine.PlayMode
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Play(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: PlayMode
        :type arg2: UnityEngine.PlayMode
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Play(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Play(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def CrossFade(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: PlayMode
        :type arg3: UnityEngine.PlayMode
        '''
        pass

    @staticmethod
    @overload
    def CrossFade(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFade(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def CrossFade(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def Blend(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def Blend(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def Blend(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def Blend(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def CrossFadeQueued(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: QueueMode
        :type arg3: UnityEngine.QueueMode
        :param arg4: PlayMode
        :type arg4: UnityEngine.PlayMode
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeQueued(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: QueueMode
        :type arg3: UnityEngine.QueueMode
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeQueued(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeQueued(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    def CrossFadeQueued(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def PlayQueued(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: QueueMode
        :type arg2: UnityEngine.QueueMode
        :param arg3: PlayMode
        :type arg3: UnityEngine.PlayMode
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    @overload
    def PlayQueued(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: QueueMode
        :type arg2: UnityEngine.QueueMode
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    @overload
    def PlayQueued(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: AnimationState
        :rtype: UnityEngine.AnimationState
        '''
        pass

    @staticmethod
    def PlayQueued(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def AddClip(arg1, arg2):
        '''
        :param arg1: AnimationClip
        :type arg1: UnityEngine.AnimationClip
        :param arg2: String
        :type arg2: System.String or str
        '''
        pass

    @staticmethod
    @overload
    def AddClip(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: AnimationClip
        :type arg1: UnityEngine.AnimationClip
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Boolean
        :type arg5: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def AddClip(arg1, arg2, arg3, arg4):
        '''
        :param arg1: AnimationClip
        :type arg1: UnityEngine.AnimationClip
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Int32
        :type arg4: System.Int32 or int
        '''
        pass

    @staticmethod
    def AddClip(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def RemoveClip(arg1):
        '''
        :param arg1: AnimationClip
        :type arg1: UnityEngine.AnimationClip
        '''
        pass

    @staticmethod
    @overload
    def RemoveClip(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def RemoveClip(arg1=None):
        pass

    @staticmethod
    def GetClipCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def SyncLayer(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def GetEnumerator():
        '''
        :returns: IEnumerator
        :rtype: System.IEnumerator
        '''
        pass

    @staticmethod
    def GetClip(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: AnimationClip
        :rtype: UnityEngine.AnimationClip
        '''
        pass

    @staticmethod
    def get_animatePhysics():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_animatePhysics(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_cullingType():
        '''
        :returns: AnimationCullingType
        :rtype: UnityEngine.AnimationCullingType
        '''
        pass

    @staticmethod
    def set_cullingType(arg1):
        '''
        :param arg1: AnimationCullingType
        :type arg1: UnityEngine.AnimationCullingType
        '''
        pass

    @staticmethod
    def get_localBounds():
        '''
        :returns: Bounds
        :rtype: UnityEngine.Bounds
        '''
        pass

    @staticmethod
    def set_localBounds(arg1):
        '''
        :param arg1: Bounds
        :type arg1: UnityEngine.Bounds
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
    def get_transform():
        '''
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def get_gameObject():
        '''
        :returns: GameObject
        :rtype: UnityEngine.GameObject
        '''
        pass

    @staticmethod
    @overload
    def GetComponent(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    @overload
    def GetComponent(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def GetComponent(arg1=None):
        pass

    @staticmethod
    @overload
    def GetComponentInChildren(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    @overload
    def GetComponentInChildren(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def GetComponentInChildren(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Undefined variable
        :type arg2: ListT.ListT
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: ListT.ListT
        '''
        pass

    @staticmethod
    def GetComponentsInChildren(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetComponentInParent(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def GetComponentInParent(arg1=None):
        pass

    @staticmethod
    @overload
    def GetComponentsInParent(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInParent(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInParent(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Undefined variable
        :type arg2: ListT.ListT
        '''
        pass

    @staticmethod
    def GetComponentsInParent(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetComponents(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponents(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetComponents(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: ListT.ListT
        '''
        pass

    @staticmethod
    def GetComponents(arg1=None, arg2=None):
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
