from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie import VRC
from UdonPie.Undefined import *


class VRCPlayerApi:
    def __new__(cls, arg1=None):
        '''
        :returns: VRCPlayerApi
        :rtype: VRC.SDKBase.VRCPlayerApi
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: VRCPlayerApi
        :rtype: VRC.VRCPlayerApi
        '''
        pass

    @staticmethod
    def get_isLocal():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_isLocal():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_displayName():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def set_displayName():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_isMaster():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsPlayerGrounded():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_AllPlayers():
        '''
        :returns: List
        :rtype: System.List
        '''
        pass

    @staticmethod
    def GetPlayerId(arg1):
        '''
        :param arg1: VRCPlayerApi
        :type arg1: VRC.VRCPlayerApi
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_playerId():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetPlayerById(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: VRCPlayerApi
        :rtype: VRC.VRCPlayerApi
        '''
        pass

    @staticmethod
    def IsOwner(arg1):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetTrackingData(arg1):
        '''
        :param arg1: TrackingDataType
        :type arg1: VRC.TrackingDataType
        :returns: VRCPlayerApi+TrackingData
        :rtype: VRC.VRCPlayerApi+TrackingData
        '''
        pass

    @staticmethod
    @overload
    def TeleportTo(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    @overload
    def TeleportTo(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Quaternion
        :type arg2: UnityEngine.Quaternion
        :param arg3: Undefined variable
        :type arg3: VRCSDKBaseVRC.VRCSDKBaseVRC
        :param arg4: Undefined variable
        :type arg4: SceneDescriptorSpawnOrientation.SceneDescriptorSpawnOrientation
        '''
        pass

    @staticmethod
    def TeleportTo(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def EnablePickups(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def SetPlayerTag(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        '''
        pass

    @staticmethod
    def GetPlayerTag(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def GetPlayersWithTag(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: String
        :type arg2: System.String or str
        :returns: List
        :rtype: System.List
        '''
        pass

    @staticmethod
    def ClearPlayerTags():
        pass

    @staticmethod
    def SetSilencedToTagged(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: String
        :type arg3: System.String or str
        '''
        pass

    @staticmethod
    def SetSilencedToUntagged(arg1, arg2, arg3):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: String
        :type arg3: System.String or str
        '''
        pass

    @staticmethod
    def SetRunSpeed(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def SetWalkSpeed(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def SetJumpImpulse(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def SetGravityStrength(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def UseLegacyLocomotion():
        pass

    @staticmethod
    def ClearSilence():
        pass

    @staticmethod
    def AddToList():
        pass

    @staticmethod
    def RemoveFromList():
        pass

    @staticmethod
    def PushAnimations(arg1):
        '''
        :param arg1: RuntimeAnimatorController
        :type arg1: UnityEngine.RuntimeAnimatorController
        '''
        pass

    @staticmethod
    def PopAnimations():
        pass

    @staticmethod
    def Immobilize(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def SetVelocity(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def GetVelocity():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def GetPosition():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
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
