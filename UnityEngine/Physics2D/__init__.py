from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Physics2D:
    def __new__(cls, arg1=None):
        '''
        :returns: Physics2D
        :rtype: UnityEngine.Physics2D
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
    def OverlapAreaNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapAreaNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapAreaNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapAreaNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapAreaNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def OverlapCapsule(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsule(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsule(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsule(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsule(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: ContactFilter2D
        :type arg5: UnityEngine.ContactFilter2D
        :param arg6: Collider2DArray
        :type arg6: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapCapsule(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def OverlapCapsuleAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsuleAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsuleAll(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsuleAll(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    def OverlapCapsuleAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def OverlapCapsuleNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Collider2DArray
        :type arg5: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsuleNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Collider2DArray
        :type arg5: UnityEngine.Collider2DArray
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsuleNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Collider2DArray
        :type arg5: UnityEngine.Collider2DArray
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapCapsuleNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Collider2DArray
        :type arg5: UnityEngine.Collider2DArray
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Single
        :type arg7: System.Single or float
        :param arg8: Single
        :type arg8: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapCapsuleNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None):
        pass

    @staticmethod
    def OverlapCollider(arg1, arg2, arg3):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: Collider2D
        :type arg2: UnityEngine.Collider2D
        :param arg3: ContactFilter2D
        :type arg3: UnityEngine.ContactFilter2D
        :param arg4: ContactPoint2DArray
        :type arg4: UnityEngine.ContactPoint2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: ContactPoint2DArray
        :type arg2: UnityEngine.ContactPoint2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2, arg3):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: ContactPoint2DArray
        :type arg3: UnityEngine.ContactPoint2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: Collider2DArray
        :type arg2: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2, arg3):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2):
        '''
        :param arg1: Rigidbody2D
        :type arg1: UnityEngine.Rigidbody2D
        :param arg2: ContactPoint2DArray
        :type arg2: UnityEngine.ContactPoint2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2, arg3):
        '''
        :param arg1: Rigidbody2D
        :type arg1: UnityEngine.Rigidbody2D
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: ContactPoint2DArray
        :type arg3: UnityEngine.ContactPoint2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2):
        '''
        :param arg1: Rigidbody2D
        :type arg1: UnityEngine.Rigidbody2D
        :param arg2: Collider2DArray
        :type arg2: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2, arg3):
        '''
        :param arg1: Rigidbody2D
        :type arg1: UnityEngine.Rigidbody2D
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetContacts(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: RaycastHit2DArray
        :type arg5: UnityEngine.RaycastHit2DArray
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
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: RaycastHit2DArray
        :type arg5: UnityEngine.RaycastHit2DArray
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: Single
        :type arg8: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: RaycastHit2DArray
        :type arg5: UnityEngine.RaycastHit2DArray
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: Single
        :type arg8: System.Single or float
        :param arg9: Single
        :type arg9: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: RaycastHit2DArray
        :type arg5: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def BoxCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: RaycastHit2DArray
        :type arg5: UnityEngine.RaycastHit2DArray
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def BoxCastNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None):
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: Single
        :type arg8: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: Single
        :type arg8: System.Single or float
        :param arg9: Single
        :type arg9: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: ContactFilter2D
        :type arg6: UnityEngine.ContactFilter2D
        :param arg7: RaycastHit2DArray
        :type arg7: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: ContactFilter2D
        :type arg6: UnityEngine.ContactFilter2D
        :param arg7: RaycastHit2DArray
        :type arg7: UnityEngine.RaycastHit2DArray
        :param arg8: Single
        :type arg8: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CapsuleCast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None):
        pass

    @staticmethod
    @overload
    def CapsuleCastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastAll(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastAll(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastAll(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: Single
        :type arg8: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastAll(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Int32
        :type arg7: System.Int32 or int
        :param arg8: Single
        :type arg8: System.Single or float
        :param arg9: Single
        :type arg9: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    def CapsuleCastAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None):
        pass

    @staticmethod
    @overload
    def CapsuleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: RaycastHit2DArray
        :type arg6: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: RaycastHit2DArray
        :type arg6: UnityEngine.RaycastHit2DArray
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: RaycastHit2DArray
        :type arg6: UnityEngine.RaycastHit2DArray
        :param arg7: Single
        :type arg7: System.Single or float
        :param arg8: Int32
        :type arg8: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: RaycastHit2DArray
        :type arg6: UnityEngine.RaycastHit2DArray
        :param arg7: Single
        :type arg7: System.Single or float
        :param arg8: Int32
        :type arg8: System.Int32 or int
        :param arg9: Single
        :type arg9: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CapsuleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: CapsuleDirection2D
        :type arg3: UnityEngine.CapsuleDirection2D
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Vector2
        :type arg5: UnityEngine.Vector2
        :param arg6: RaycastHit2DArray
        :type arg6: UnityEngine.RaycastHit2DArray
        :param arg7: Single
        :type arg7: System.Single or float
        :param arg8: Int32
        :type arg8: System.Int32 or int
        :param arg9: Single
        :type arg9: System.Single or float
        :param arg10: Single
        :type arg10: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CapsuleCastNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None, arg10=None):
        pass

    @staticmethod
    @overload
    def GetRayIntersection(arg1):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def GetRayIntersection(arg1, arg2):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def GetRayIntersection(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    def GetRayIntersection(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def GetRayIntersectionAll(arg1):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def GetRayIntersectionAll(arg1, arg2):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def GetRayIntersectionAll(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    def GetRayIntersectionAll(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def GetRayIntersectionNonAlloc(arg1, arg2):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: RaycastHit2DArray
        :type arg2: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetRayIntersectionNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: RaycastHit2DArray
        :type arg2: UnityEngine.RaycastHit2DArray
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetRayIntersectionNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Ray
        :type arg1: UnityEngine.Ray
        :param arg2: RaycastHit2DArray
        :type arg2: UnityEngine.RaycastHit2DArray
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetRayIntersectionNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def OverlapPoint(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapPoint(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapPoint(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapPoint(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapPoint(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapPoint(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def OverlapPointAll(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapPointAll(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapPointAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapPointAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    def OverlapPointAll(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def OverlapPointNonAlloc(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Collider2DArray
        :type arg2: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapPointNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Collider2DArray
        :type arg2: UnityEngine.Collider2DArray
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapPointNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Collider2DArray
        :type arg2: UnityEngine.Collider2DArray
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapPointNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Collider2DArray
        :type arg2: UnityEngine.Collider2DArray
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapPointNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def OverlapCircle(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircle(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircle(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircle(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircle(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: ContactFilter2D
        :type arg3: UnityEngine.ContactFilter2D
        :param arg4: Collider2DArray
        :type arg4: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapCircle(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def OverlapCircleAll(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircleAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircleAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircleAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    def OverlapCircleAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def OverlapCircleNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircleNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircleNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapCircleNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Collider2DArray
        :type arg3: UnityEngine.Collider2DArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapCircleNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def OverlapBox(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapBox(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapBox(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapBox(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapBox(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: ContactFilter2D
        :type arg4: UnityEngine.ContactFilter2D
        :param arg5: Collider2DArray
        :type arg5: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapBox(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def OverlapBoxAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapBoxAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapBoxAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapBoxAll(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    def OverlapBoxAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def OverlapBoxNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Collider2DArray
        :type arg4: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapBoxNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Collider2DArray
        :type arg4: UnityEngine.Collider2DArray
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapBoxNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Collider2DArray
        :type arg4: UnityEngine.Collider2DArray
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def OverlapBoxNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Collider2DArray
        :type arg4: UnityEngine.Collider2DArray
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapBoxNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def OverlapArea(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapArea(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapArea(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapArea(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Collider2D
        :rtype: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def OverlapArea(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: ContactFilter2D
        :type arg3: UnityEngine.ContactFilter2D
        :param arg4: Collider2DArray
        :type arg4: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def OverlapArea(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def OverlapAreaAll(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapAreaAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapAreaAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    @overload
    def OverlapAreaAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Collider2DArray
        :rtype: UnityEngine.Collider2DArray
        '''
        pass

    @staticmethod
    def OverlapAreaAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
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
    def SetLayerCollisionMask(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def GetLayerCollisionMask(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def IsTouching(arg1, arg2):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: Collider2D
        :type arg2: UnityEngine.Collider2D
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsTouching(arg1, arg2, arg3):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: Collider2D
        :type arg2: UnityEngine.Collider2D
        :param arg3: ContactFilter2D
        :type arg3: UnityEngine.ContactFilter2D
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsTouching(arg1, arg2):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsTouching(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def IsTouchingLayers(arg1):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsTouchingLayers(arg1, arg2):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsTouchingLayers(arg1=None, arg2=None):
        pass

    @staticmethod
    def Distance(arg1, arg2):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: Collider2D
        :type arg2: UnityEngine.Collider2D
        :returns: ColliderDistance2D
        :rtype: UnityEngine.ColliderDistance2D
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def Linecast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: ContactFilter2D
        :type arg3: UnityEngine.ContactFilter2D
        :param arg4: RaycastHit2DArray
        :type arg4: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Linecast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def LinecastAll(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def LinecastAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def LinecastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def LinecastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    def LinecastAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def LinecastNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LinecastNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LinecastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def LinecastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def LinecastNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: ContactFilter2D
        :type arg3: UnityEngine.ContactFilter2D
        :param arg4: RaycastHit2DArray
        :type arg4: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: ContactFilter2D
        :type arg3: UnityEngine.ContactFilter2D
        :param arg4: RaycastHit2DArray
        :type arg4: UnityEngine.RaycastHit2DArray
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Raycast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
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
    def RaycastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def RaycastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def RaycastNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def RaycastAll(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    def RaycastAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
        pass

    @staticmethod
    @overload
    def CircleCast(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CircleCast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CircleCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CircleCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CircleCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def CircleCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: ContactFilter2D
        :type arg4: UnityEngine.ContactFilter2D
        :param arg5: RaycastHit2DArray
        :type arg5: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CircleCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: ContactFilter2D
        :type arg4: UnityEngine.ContactFilter2D
        :param arg5: RaycastHit2DArray
        :type arg5: UnityEngine.RaycastHit2DArray
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CircleCast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def CircleCastAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def CircleCastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def CircleCastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def CircleCastAll(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def CircleCastAll(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Int32
        :type arg5: System.Int32 or int
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    def CircleCastAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        pass

    @staticmethod
    @overload
    def CircleCastNonAlloc(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: RaycastHit2DArray
        :type arg4: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CircleCastNonAlloc(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: RaycastHit2DArray
        :type arg4: UnityEngine.RaycastHit2DArray
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CircleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: RaycastHit2DArray
        :type arg4: UnityEngine.RaycastHit2DArray
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
    def CircleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: RaycastHit2DArray
        :type arg4: UnityEngine.RaycastHit2DArray
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def CircleCastNonAlloc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: RaycastHit2DArray
        :type arg4: UnityEngine.RaycastHit2DArray
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Single
        :type arg7: System.Single or float
        :param arg8: Single
        :type arg8: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CircleCastNonAlloc(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None):
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Single
        :type arg7: System.Single or float
        :param arg8: Single
        :type arg8: System.Single or float
        :returns: RaycastHit2D
        :rtype: UnityEngine.RaycastHit2D
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: ContactFilter2D
        :type arg5: UnityEngine.ContactFilter2D
        :param arg6: RaycastHit2DArray
        :type arg6: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def BoxCast(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: ContactFilter2D
        :type arg5: UnityEngine.ContactFilter2D
        :param arg6: RaycastHit2DArray
        :type arg6: UnityEngine.RaycastHit2DArray
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def BoxCast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None):
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Single
        :type arg7: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    @overload
    def BoxCastAll(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Int32
        :type arg6: System.Int32 or int
        :param arg7: Single
        :type arg7: System.Single or float
        :param arg8: Single
        :type arg8: System.Single or float
        :returns: RaycastHit2DArray
        :rtype: UnityEngine.RaycastHit2DArray
        '''
        pass

    @staticmethod
    def BoxCastAll(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None):
        pass

    @staticmethod
    def get_defaultPhysicsScene():
        '''
        :returns: PhysicsScene2D
        :rtype: UnityEngine.PhysicsScene2D
        '''
        pass

    @staticmethod
    def get_velocityIterations():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_velocityIterations(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_positionIterations():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_positionIterations(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_gravity():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_gravity(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_queriesStartInColliders():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_queriesStartInColliders(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_callbacksOnDisable():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_callbacksOnDisable(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
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
    def get_jobOptions():
        '''
        :returns: PhysicsJobOptions2D
        :rtype: UnityEngine.PhysicsJobOptions2D
        '''
        pass

    @staticmethod
    def set_jobOptions(arg1):
        '''
        :param arg1: PhysicsJobOptions2D
        :type arg1: UnityEngine.PhysicsJobOptions2D
        '''
        pass

    @staticmethod
    def get_velocityThreshold():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_velocityThreshold(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_maxLinearCorrection():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_maxLinearCorrection(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_maxAngularCorrection():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_maxAngularCorrection(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_maxTranslationSpeed():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_maxTranslationSpeed(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_maxRotationSpeed():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_maxRotationSpeed(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_baumgarteScale():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_baumgarteScale(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_baumgarteTOIScale():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_baumgarteTOIScale(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_timeToSleep():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_timeToSleep(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_linearSleepTolerance():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_linearSleepTolerance(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_angularSleepTolerance():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_angularSleepTolerance(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_alwaysShowColliders():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_alwaysShowColliders(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_showColliderSleep():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_showColliderSleep(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_showColliderContacts():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_showColliderContacts(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_showColliderAABB():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_showColliderAABB(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_contactArrowScale():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_contactArrowScale(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_colliderAwakeColor():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_colliderAwakeColor(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_colliderAsleepColor():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_colliderAsleepColor(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_colliderContactColor():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_colliderContactColor(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_colliderAABBColor():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_colliderAABBColor(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def Simulate(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def SyncTransforms():
        pass

    @staticmethod
    @overload
    def IgnoreCollision(arg1, arg2):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: Collider2D
        :type arg2: UnityEngine.Collider2D
        '''
        pass

    @staticmethod
    @overload
    def IgnoreCollision(arg1, arg2, arg3):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: Collider2D
        :type arg2: UnityEngine.Collider2D
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        '''
        pass

    @staticmethod
    def IgnoreCollision(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def GetIgnoreCollision(arg1, arg2):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :param arg2: Collider2D
        :type arg2: UnityEngine.Collider2D
        :returns: Boolean
        :rtype: System.Boolean
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
