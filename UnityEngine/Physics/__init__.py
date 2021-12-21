from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Physics:
    def __new__(cls, arg1=None):
        '''
        :returns: Physics
        :rtype: UnityEngine.Physics
        '''
        pass

    @staticmethod
    def get_IgnoreRaycastLayer():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_DefaultRaycastLayers():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_AllLayers():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CheckSphere(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CheckSphere(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CheckSphere(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: QueryTriggerInteraction
        :type arg4: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def CheckSphere(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def CapsuleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: RaycastHitArray
        :type arg5: UnityEngine.RaycastHitArray
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: QueryTriggerInteraction
        :type arg8: UnityEngine.QueryTriggerInteraction
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: RaycastHitArray
        :type arg5: UnityEngine.RaycastHitArray
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: RaycastHitArray
        :type arg5: UnityEngine.RaycastHitArray
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: RaycastHitArray
        :type arg5: UnityEngine.RaycastHitArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CapsuleCastNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None):
        pass

    @staticmethod
    @overload
    def SphereCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: RaycastHitArray
        :type arg4: UnityEngine.RaycastHitArray
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: QueryTriggerInteraction
        :type arg7: UnityEngine.QueryTriggerInteraction
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def SphereCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: RaycastHitArray
        :type arg4: UnityEngine.RaycastHitArray
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def SphereCastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: RaycastHitArray
        :type arg4: UnityEngine.RaycastHitArray
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def SphereCastNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: RaycastHitArray
        :type arg4: UnityEngine.RaycastHitArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def SphereCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: RaycastHitArray
        :type arg3: UnityEngine.RaycastHitArray
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: QueryTriggerInteraction
        :type arg6: UnityEngine.QueryTriggerInteraction
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def SphereCastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: RaycastHitArray
        :type arg3: UnityEngine.RaycastHitArray
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def SphereCastNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: RaycastHitArray
        :type arg3: UnityEngine.RaycastHitArray
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def SphereCastNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: RaycastHitArray
        :type arg3: UnityEngine.RaycastHitArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def SphereCastNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def CheckCapsule(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CheckCapsule(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CheckCapsule(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def CheckCapsule(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def CheckBox(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Quaternion
        :type arg3: UnityEngine.Quaternion
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CheckBox(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Quaternion
        :type arg3: UnityEngine.Quaternion
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CheckBox(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Quaternion
        :type arg3: UnityEngine.Quaternion
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CheckBox(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def CheckBox(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def OverlapBox(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Quaternion
        :type arg3: UnityEngine.Quaternion
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapBox(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Quaternion
        :type arg3: UnityEngine.Quaternion
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapBox(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Quaternion
        :type arg3: UnityEngine.Quaternion
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapBox(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    def OverlapBox(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def OverlapBoxNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: ColliderArray
        :type arg3: UnityEngine.ColliderArray
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: QueryTriggerInteraction
        :type arg6: UnityEngine.QueryTriggerInteraction
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapBoxNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: ColliderArray
        :type arg3: UnityEngine.ColliderArray
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapBoxNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: ColliderArray
        :type arg3: UnityEngine.ColliderArray
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapBoxNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: ColliderArray
        :type arg3: UnityEngine.ColliderArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapBoxNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: RaycastHitArray
        :type arg4: UnityEngine.RaycastHitArray
        :param arg5: Quaternion
        :type arg5: UnityEngine.Quaternion
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: QueryTriggerInteraction
        :type arg8: UnityEngine.QueryTriggerInteraction
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: RaycastHitArray
        :type arg4: UnityEngine.RaycastHitArray
        :param arg5: Quaternion
        :type arg5: UnityEngine.Quaternion
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: RaycastHitArray
        :type arg4: UnityEngine.RaycastHitArray
        :param arg5: Quaternion
        :type arg5: UnityEngine.Quaternion
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: RaycastHitArray
        :type arg4: UnityEngine.RaycastHitArray
        :param arg5: Quaternion
        :type arg5: UnityEngine.Quaternion
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: RaycastHitArray
        :type arg4: UnityEngine.RaycastHitArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def BoxCastNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None):
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: QueryTriggerInteraction
        :type arg7: UnityEngine.QueryTriggerInteraction
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    def BoxCastAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def OverlapCapsuleNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: ColliderArray
        :type arg4: UnityEngine.ColliderArray
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: QueryTriggerInteraction
        :type arg6: UnityEngine.QueryTriggerInteraction
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsuleNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: ColliderArray
        :type arg4: UnityEngine.ColliderArray
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsuleNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: ColliderArray
        :type arg4: UnityEngine.ColliderArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapCapsuleNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    def RebuildBroadphaseRegions(arg1, arg2):
        '''
        :param arg1: Bounds
        :type arg1: UnityEngine.Bounds
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: QueryTriggerInteraction
        :type arg6: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Undefined variable
        :type arg4: RaycastHitRef.RaycastHitRef
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: QueryTriggerInteraction
        :type arg7: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Undefined variable
        :type arg4: RaycastHitRef.RaycastHitRef
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Undefined variable
        :type arg4: RaycastHitRef.RaycastHitRef
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Undefined variable
        :type arg4: RaycastHitRef.RaycastHitRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SphereCast(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def SphereCast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: QueryTriggerInteraction
        :type arg7: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Undefined variable
        :type arg4: RaycastHitRef.RaycastHitRef
        :param arg5: Quaternion
        :type arg5: UnityEngine.Quaternion
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: QueryTriggerInteraction
        :type arg8: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Undefined variable
        :type arg4: RaycastHitRef.RaycastHitRef
        :param arg5: Quaternion
        :type arg5: UnityEngine.Quaternion
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Undefined variable
        :type arg4: RaycastHitRef.RaycastHitRef
        :param arg5: Quaternion
        :type arg5: UnityEngine.Quaternion
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Undefined variable
        :type arg4: RaycastHitRef.RaycastHitRef
        :param arg5: Quaternion
        :type arg5: UnityEngine.Quaternion
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Undefined variable
        :type arg4: RaycastHitRef.RaycastHitRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def BoxCast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None):
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: QueryTriggerInteraction
        :type arg4: UnityEngine.QueryTriggerInteraction
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    def RaycastAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: RaycastHitArray
        :type arg2: UnityEngine.RaycastHitArray
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: RaycastHitArray
        :type arg2: UnityEngine.RaycastHitArray
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: RaycastHitArray
        :type arg2: UnityEngine.RaycastHitArray
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: RaycastHitArray
        :type arg2: UnityEngine.RaycastHitArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: RaycastHitArray
        :type arg3: UnityEngine.RaycastHitArray
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: QueryTriggerInteraction
        :type arg6: UnityEngine.QueryTriggerInteraction
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: RaycastHitArray
        :type arg3: UnityEngine.RaycastHitArray
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: RaycastHitArray
        :type arg3: UnityEngine.RaycastHitArray
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: RaycastHitArray
        :type arg3: UnityEngine.RaycastHitArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def RaycastNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def CapsuleCastAll(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: QueryTriggerInteraction
        :type arg7: UnityEngine.QueryTriggerInteraction
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastAll(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    def CapsuleCastAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def SphereCastAll(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: QueryTriggerInteraction
        :type arg6: UnityEngine.QueryTriggerInteraction
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def SphereCastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def SphereCastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def SphereCastAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def SphereCastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def SphereCastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def SphereCastAll(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def SphereCastAll(arg1, arg2):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    def SphereCastAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def OverlapCapsule(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsule(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsule(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    def OverlapCapsule(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def OverlapSphere(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: QueryTriggerInteraction
        :type arg4: UnityEngine.QueryTriggerInteraction
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapSphere(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapSphere(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: ColliderArray
        :rtype: UnityEngine.ColliderArray
        '''
        pass

    @staticmethod
    def OverlapSphere(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def Simulate(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def SyncTransforms():
        pass

    @staticmethod
    def get_reuseCollisionCallbacks():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_reuseCollisionCallbacks(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def ComputePenetration(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Collider
        :type arg1: UnityEngine.Collider
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Quaternion
        :type arg3: UnityEngine.Quaternion
        :param arg4: Collider
        :type arg4: UnityEngine.Collider
        :param arg5: Vector3
        :type arg5: UnityEngine.Vector3
        :param arg6: Quaternion
        :type arg6: UnityEngine.Quaternion
        :param arg7: Undefined variable
        :type arg7: Vector3Ref.Vector3Ref
        :param arg8: Undefined variable
        :type arg8: SingleRef.SingleRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def ClosestPoint(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Collider
        :type arg2: UnityEngine.Collider
        :param arg3: Vector3
        :type arg3: UnityEngine.Vector3
        :param arg4: Quaternion
        :type arg4: UnityEngine.Quaternion
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_interCollisionDistance():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_interCollisionDistance(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_interCollisionStiffness():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_interCollisionStiffness(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_interCollisionSettingsToggle():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_interCollisionSettingsToggle(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def OverlapSphereNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: ColliderArray
        :type arg3: UnityEngine.ColliderArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapSphereNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: ColliderArray
        :type arg3: UnityEngine.ColliderArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapSphereNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: ColliderArray
        :type arg3: UnityEngine.ColliderArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapSphereNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def get_gravity():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_gravity(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_defaultPhysicsScene():
        '''
        :returns: PhysicsScene
        :rtype: UnityEngine.PhysicsScene
        '''
        pass

    @staticmethod
    @overload
    def IgnoreCollision(arg1, arg2, arg3):
        '''
        :param arg1: Collider
        :type arg1: UnityEngine.Collider
        :param arg2: Collider
        :type arg2: UnityEngine.Collider
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def IgnoreCollision(arg1, arg2):
        '''
        :param arg1: Collider
        :type arg1: UnityEngine.Collider
        :param arg2: Collider
        :type arg2: UnityEngine.Collider
        '''
        pass

    @staticmethod
    def IgnoreCollision(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def GetIgnoreLayerCollision(arg1, arg2):
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
    @overload
    def Raycast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: QueryTriggerInteraction
        :type arg6: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: QueryTriggerInteraction
        :type arg4: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Undefined variable
        :type arg2: RaycastHitRef.RaycastHitRef
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Undefined variable
        :type arg2: RaycastHitRef.RaycastHitRef
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Undefined variable
        :type arg2: RaycastHitRef.RaycastHitRef
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Undefined variable
        :type arg2: RaycastHitRef.RaycastHitRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Raycast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: QueryTriggerInteraction
        :type arg4: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: QueryTriggerInteraction
        :type arg5: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Undefined variable
        :type arg3: RaycastHitRef.RaycastHitRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Linecast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: QueryTriggerInteraction
        :type arg7: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Undefined variable
        :type arg5: RaycastHitRef.RaycastHitRef
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: QueryTriggerInteraction
        :type arg8: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Undefined variable
        :type arg5: RaycastHitRef.RaycastHitRef
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Undefined variable
        :type arg5: RaycastHitRef.RaycastHitRef
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector3
        :type arg4: UnityEngine.Vector3
        :param arg5: Undefined variable
        :type arg5: RaycastHitRef.RaycastHitRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def CapsuleCast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None):
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
