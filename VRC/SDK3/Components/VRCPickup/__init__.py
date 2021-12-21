from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie import VRC
from UdonPie.Undefined import *


class VRCPickup:
    def __new__(cls, arg1=None):
        '''
        :returns: VRCPickup
        :rtype: VRC.SDK3.Components.VRCPickup
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
    def get_MomentumTransferMethod():
        '''
        :returns: ForceMode
        :rtype: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    def set_MomentumTransferMethod():
        '''
        :returns: ForceMode
        :rtype: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    def get_DisallowTheft():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_DisallowTheft():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_ExactGun():
        '''
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def set_ExactGun():
        '''
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def get_ExactGrip():
        '''
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def set_ExactGrip():
        '''
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def get_allowManipulationWhenEquipped():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_allowManipulationWhenEquipped():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_InteractionText():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def set_InteractionText():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_UseText():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def set_UseText():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_ThrowVelocityBoostMinSpeed():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_ThrowVelocityBoostMinSpeed():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_ThrowVelocityBoostScale():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_ThrowVelocityBoostScale():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_currentlyHeldBy():
        '''
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def set_currentlyHeldBy():
        '''
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def get_currentLocalPlayer():
        '''
        :returns: VRCPlayerApi
        :rtype: VRC.VRCPlayerApi
        '''
        pass

    @staticmethod
    def set_currentLocalPlayer():
        '''
        :returns: VRCPlayerApi
        :rtype: VRC.VRCPlayerApi
        '''
        pass

    @staticmethod
    def get_pickupable():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_pickupable():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_proximity():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_proximity():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_currentPlayer():
        '''
        :returns: VRCPlayerApi
        :rtype: VRC.VRCPlayerApi
        '''
        pass

    @staticmethod
    def get_IsHeld():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Drop():
        pass

    @staticmethod
    @overload
    def Drop(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def Drop(arg1=None):
        pass

    @staticmethod
    def GenerateHapticEvent(arg1, arg2, arg3):
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
    def PlayHaptics():
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
