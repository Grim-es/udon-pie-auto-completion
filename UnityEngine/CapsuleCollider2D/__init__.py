from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class CapsuleCollider2D:
    def __new__(cls, arg1=None):
        '''
        :returns: CapsuleCollider2D
        :rtype: UnityEngine.CapsuleCollider2D
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
    def get_size():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_size(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_direction():
        '''
        :returns: CapsuleDirection2D
        :rtype: UnityEngine.CapsuleDirection2D
        '''
        pass

    @staticmethod
    def set_direction(arg1):
        '''
        :param arg1: CapsuleDirection2D
        :type arg1: UnityEngine.CapsuleDirection2D
        '''
        pass

    @staticmethod
    def get_density():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_density(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_isTrigger():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_isTrigger(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_usedByEffector():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_usedByEffector(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_usedByComposite():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_usedByComposite(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_composite():
        '''
        :returns: CompositeCollider2D
        :rtype: UnityEngine.CompositeCollider2D
        '''
        pass

    @staticmethod
    def get_offset():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_offset(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_attachedRigidbody():
        '''
        :returns: Rigidbody2D
        :rtype: UnityEngine.Rigidbody2D
        '''
        pass

    @staticmethod
    def get_shapeCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_bounds():
        '''
        :returns: Bounds
        :rtype: UnityEngine.Bounds
        '''
        pass

    @staticmethod
    def get_sharedMaterial():
        '''
        :returns: PhysicsMaterial2D
        :rtype: UnityEngine.PhysicsMaterial2D
        '''
        pass

    @staticmethod
    def set_sharedMaterial(arg1):
        '''
        :param arg1: PhysicsMaterial2D
        :type arg1: UnityEngine.PhysicsMaterial2D
        '''
        pass

    @staticmethod
    def get_friction():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_bounciness():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def IsTouching(arg1):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
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
    @overload
    def IsTouching(arg1):
        '''
        :param arg1: ContactFilter2D
        :type arg1: UnityEngine.ContactFilter2D
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsTouching(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def IsTouchingLayers():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsTouchingLayers(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsTouchingLayers(arg1=None):
        pass

    @staticmethod
    def OverlapPoint(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Distance(arg1):
        '''
        :param arg1: Collider2D
        :type arg1: UnityEngine.Collider2D
        :returns: ColliderDistance2D
        :rtype: UnityEngine.ColliderDistance2D
        '''
        pass

    @staticmethod
    def OverlapCollider(arg1, arg2):
        '''
        :param arg1: ContactFilter2D
        :type arg1: UnityEngine.ContactFilter2D
        :param arg2: Collider2DArray
        :type arg2: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1):
        '''
        :param arg1: ContactPoint2DArray
        :type arg1: UnityEngine.ContactPoint2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2):
        '''
        :param arg1: ContactFilter2D
        :type arg1: UnityEngine.ContactFilter2D
        :param arg2: ContactPoint2DArray
        :type arg2: UnityEngine.ContactPoint2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1):
        '''
        :param arg1: Collider2DArray
        :type arg1: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetContacts(arg1, arg2):
        '''
        :param arg1: ContactFilter2D
        :type arg1: UnityEngine.ContactFilter2D
        :param arg2: Collider2DArray
        :type arg2: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetContacts(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def Cast(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: RaycastHit2DArray
        :type arg2: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Cast(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
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
    def Cast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: RaycastHit2DArray
        :type arg2: UnityEngine.RaycastHit2DArray
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Boolean
        :type arg4: System.Boolean or bool
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Cast(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Cast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
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
    def Cast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Boolean
        :type arg5: System.Boolean or bool
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Cast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: RaycastHit2DArray
        :type arg2: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
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
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
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
    @overload
    def Raycast(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: RaycastHit2DArray
        :type arg2: UnityEngine.RaycastHit2DArray
        :param arg3: Single
        :type arg3: System.Single or float
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
    def Raycast(arg1, arg2, arg3, arg4, arg5, arg6):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: RaycastHit2DArray
        :type arg2: UnityEngine.RaycastHit2DArray
        :param arg3: Single
        :type arg3: System.Single or float
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
    def Raycast(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: ContactFilter2D
        :type arg2: UnityEngine.ContactFilter2D
        :param arg3: RaycastHit2DArray
        :type arg3: UnityEngine.RaycastHit2DArray
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def Raycast(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None):
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
