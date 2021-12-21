from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Animator:
    def __new__(cls, arg1=None):
        '''
        :returns: Animator
        :rtype: UnityEngine.Animator
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
    def get_layersAffectMassCenter():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_layersAffectMassCenter(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_leftFeetBottomHeight():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_rightFeetBottomHeight():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Rebind():
        pass

    @staticmethod
    def ApplyBuiltinRootMotion():
        pass

    @staticmethod
    def get_logWarnings():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_logWarnings(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_keepAnimatorControllerStateOnDisable():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_keepAnimatorControllerStateOnDisable(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def CrossFade(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFade(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFade(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
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
    def CrossFade(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFade(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFade(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFade(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        '''
        pass

    @staticmethod
    def CrossFade(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def PlayInFixedTime(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def PlayInFixedTime(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    @overload
    def PlayInFixedTime(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Single
        :type arg3: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def PlayInFixedTime(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Single
        :type arg3: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def PlayInFixedTime(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def PlayInFixedTime(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def PlayInFixedTime(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def Play(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def Play(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    @overload
    def Play(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Single
        :type arg3: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def Play(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Single
        :type arg3: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def Play(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def Play(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def Play(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def SetTarget(arg1, arg2):
        '''
        :param arg1: AvatarTarget
        :type arg1: UnityEngine.AvatarTarget
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    def get_targetPosition():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_targetRotation():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def get_cullingMode():
        '''
        :returns: AnimatorCullingMode
        :rtype: UnityEngine.AnimatorCullingMode
        '''
        pass

    @staticmethod
    def set_cullingMode(arg1):
        '''
        :param arg1: AnimatorCullingMode
        :type arg1: UnityEngine.AnimatorCullingMode
        '''
        pass

    @staticmethod
    def StartPlayback():
        pass

    @staticmethod
    def StopPlayback():
        pass

    @staticmethod
    def get_playbackTime():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_playbackTime(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def StartRecording(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def StopRecording():
        pass

    @staticmethod
    def get_recorderStartTime():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_recorderStartTime(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_recorderStopTime():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_recorderStopTime(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_recorderMode():
        '''
        :returns: AnimatorRecorderMode
        :rtype: UnityEngine.AnimatorRecorderMode
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
    def get_hasBoundPlayables():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def HasState(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def StringToHash(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_avatar():
        '''
        :returns: Avatar
        :rtype: UnityEngine.Avatar
        '''
        pass

    @staticmethod
    def set_avatar(arg1):
        '''
        :param arg1: Avatar
        :type arg1: UnityEngine.Avatar
        '''
        pass

    @staticmethod
    def get_playableGraph():
        '''
        :returns: PlayableGraph
        :rtype: UnityEngine.PlayableGraph
        '''
        pass

    @staticmethod
    def SetLookAtPosition(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def SetLookAtWeight(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def SetLookAtWeight(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def SetLookAtWeight(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def SetLookAtWeight(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def SetLookAtWeight(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        '''
        pass

    @staticmethod
    def SetLookAtWeight(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def SetBoneLocalRotation(arg1, arg2):
        '''
        :param arg1: HumanBodyBones
        :type arg1: UnityEngine.HumanBodyBones
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def get_stabilizeFeet():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_stabilizeFeet(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_layerCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetLayerName(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def GetLayerIndex(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetLayerWeight(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def SetLayerWeight(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    def GetCurrentAnimatorStateInfo(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: AnimatorStateInfo
        :rtype: UnityEngine.AnimatorStateInfo
        '''
        pass

    @staticmethod
    def GetNextAnimatorStateInfo(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: AnimatorStateInfo
        :rtype: UnityEngine.AnimatorStateInfo
        '''
        pass

    @staticmethod
    def GetAnimatorTransitionInfo(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: AnimatorTransitionInfo
        :rtype: UnityEngine.AnimatorTransitionInfo
        '''
        pass

    @staticmethod
    def GetCurrentAnimatorClipInfoCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetNextAnimatorClipInfoCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetCurrentAnimatorClipInfo(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: AnimatorClipInfoArray
        :rtype: UnityEngine.AnimatorClipInfoArray
        '''
        pass

    @staticmethod
    @overload
    def GetCurrentAnimatorClipInfo(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetCurrentAnimatorClipInfo(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetNextAnimatorClipInfo(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: AnimatorClipInfoArray
        :rtype: UnityEngine.AnimatorClipInfoArray
        '''
        pass

    @staticmethod
    @overload
    def GetNextAnimatorClipInfo(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def GetNextAnimatorClipInfo(arg1=None, arg2=None):
        pass

    @staticmethod
    def IsInTransition(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_parameters():
        '''
        :returns: AnimatorControllerParameterArray
        :rtype: UnityEngine.AnimatorControllerParameterArray
        '''
        pass

    @staticmethod
    def get_parameterCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetParameter(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: AnimatorControllerParameter
        :rtype: UnityEngine.AnimatorControllerParameter
        '''
        pass

    @staticmethod
    def get_feetPivotActive():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_feetPivotActive(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_pivotWeight():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_pivotPosition():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def MatchTarget(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: AvatarTarget
        :type arg3: UnityEngine.AvatarTarget
        :param arg4: MatchTargetWeightMask
        :type arg4: UnityEngine.MatchTargetWeightMask
        :param arg5: Single
        :type arg5: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def MatchTarget(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: AvatarTarget
        :type arg3: UnityEngine.AvatarTarget
        :param arg4: MatchTargetWeightMask
        :type arg4: UnityEngine.MatchTargetWeightMask
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        '''
        pass

    @staticmethod
    def MatchTarget(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def InterruptMatchTarget():
        pass

    @staticmethod
    @overload
    def InterruptMatchTarget(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def InterruptMatchTarget(arg1=None):
        pass

    @staticmethod
    def get_isMatchingTarget():
        '''
        :returns: Boolean
        :rtype: System.Boolean
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
    @overload
    def CrossFadeInFixedTime(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeInFixedTime(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeInFixedTime(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeInFixedTime(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeInFixedTime(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeInFixedTime(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeInFixedTime(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def CrossFadeInFixedTime(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        '''
        pass

    @staticmethod
    def CrossFadeInFixedTime(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def WriteDefaultValues():
        pass

    @staticmethod
    def get_isOptimizable():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_isHuman():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_hasRootMotion():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_humanScale():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_isInitialized():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def GetFloat(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def GetFloat(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetFloat(arg1=None):
        pass

    @staticmethod
    @overload
    def SetFloat(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def SetFloat(arg1, arg2, arg3, arg4):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def SetFloat(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def SetFloat(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    def SetFloat(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def GetBool(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def GetBool(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetBool(arg1=None):
        pass

    @staticmethod
    @overload
    def SetBool(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def SetBool(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    def SetBool(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetInteger(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetInteger(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetInteger(arg1=None):
        pass

    @staticmethod
    @overload
    def SetInteger(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetInteger(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def SetInteger(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def SetTrigger(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    @overload
    def SetTrigger(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def SetTrigger(arg1=None):
        pass

    @staticmethod
    @overload
    def ResetTrigger(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    @overload
    def ResetTrigger(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def ResetTrigger(arg1=None):
        pass

    @staticmethod
    @overload
    def IsParameterControlledByCurve(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsParameterControlledByCurve(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsParameterControlledByCurve(arg1=None):
        pass

    @staticmethod
    def get_deltaPosition():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_deltaRotation():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def get_velocity():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_angularVelocity():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_rootPosition():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_rootPosition(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_rootRotation():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def set_rootRotation(arg1):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def get_applyRootMotion():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_applyRootMotion(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_updateMode():
        '''
        :returns: AnimatorUpdateMode
        :rtype: UnityEngine.AnimatorUpdateMode
        '''
        pass

    @staticmethod
    def set_updateMode(arg1):
        '''
        :param arg1: AnimatorUpdateMode
        :type arg1: UnityEngine.AnimatorUpdateMode
        '''
        pass

    @staticmethod
    def get_hasTransformHierarchy():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_gravityWeight():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_bodyPosition():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_bodyPosition(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_bodyRotation():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def set_bodyRotation(arg1):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def GetIKPosition(arg1):
        '''
        :param arg1: AvatarIKGoal
        :type arg1: UnityEngine.AvatarIKGoal
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def SetIKPosition(arg1, arg2):
        '''
        :param arg1: AvatarIKGoal
        :type arg1: UnityEngine.AvatarIKGoal
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def GetIKRotation(arg1):
        '''
        :param arg1: AvatarIKGoal
        :type arg1: UnityEngine.AvatarIKGoal
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def SetIKRotation(arg1, arg2):
        '''
        :param arg1: AvatarIKGoal
        :type arg1: UnityEngine.AvatarIKGoal
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def GetIKPositionWeight(arg1):
        '''
        :param arg1: AvatarIKGoal
        :type arg1: UnityEngine.AvatarIKGoal
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def SetIKPositionWeight(arg1, arg2):
        '''
        :param arg1: AvatarIKGoal
        :type arg1: UnityEngine.AvatarIKGoal
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    def GetIKRotationWeight(arg1):
        '''
        :param arg1: AvatarIKGoal
        :type arg1: UnityEngine.AvatarIKGoal
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def SetIKRotationWeight(arg1, arg2):
        '''
        :param arg1: AvatarIKGoal
        :type arg1: UnityEngine.AvatarIKGoal
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    def GetIKHintPosition(arg1):
        '''
        :param arg1: AvatarIKHint
        :type arg1: UnityEngine.AvatarIKHint
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def SetIKHintPosition(arg1, arg2):
        '''
        :param arg1: AvatarIKHint
        :type arg1: UnityEngine.AvatarIKHint
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def GetIKHintPositionWeight(arg1):
        '''
        :param arg1: AvatarIKHint
        :type arg1: UnityEngine.AvatarIKHint
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def SetIKHintPositionWeight(arg1, arg2):
        '''
        :param arg1: AvatarIKHint
        :type arg1: UnityEngine.AvatarIKHint
        :param arg2: Single
        :type arg2: System.Single or float
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
