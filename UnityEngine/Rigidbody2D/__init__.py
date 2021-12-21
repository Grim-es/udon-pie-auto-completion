from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Rigidbody2D:
    def __new__(cls, arg1=None):
        '''
        :returns: Rigidbody2D
        :rtype: UnityEngine.Rigidbody2D
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
    @overload
    def AddTorque(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def AddTorque(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: ForceMode2D
        :type arg2: UnityEngine.ForceMode2D
        '''
        pass

    @staticmethod
    def AddTorque(arg1=None, arg2=None):
        pass

    @staticmethod
    def GetPoint(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def GetRelativePoint(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def GetVector(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def GetRelativeVector(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def GetPointVelocity(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def GetRelativePointVelocity(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :returns: Vector2
        :rtype: UnityEngine.Vector2
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
    def GetAttachedColliders(arg1):
        '''
        :param arg1: Collider2DArray
        :type arg1: UnityEngine.Collider2DArray
        :returns: Int32
        :rtype: System.Int32
        '''
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
    def Cast(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def get_position():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_position(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_rotation():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_rotation(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def MovePosition(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def MoveRotation(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_velocity():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_velocity(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_angularVelocity():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_angularVelocity(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_useAutoMass():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useAutoMass(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_mass():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_mass(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
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
    def get_centerOfMass():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_centerOfMass(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_worldCenterOfMass():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_inertia():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_inertia(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_drag():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_drag(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_angularDrag():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_angularDrag(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_gravityScale():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_gravityScale(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_bodyType():
        '''
        :returns: RigidbodyType2D
        :rtype: UnityEngine.RigidbodyType2D
        '''
        pass

    @staticmethod
    def set_bodyType(arg1):
        '''
        :param arg1: RigidbodyType2D
        :type arg1: UnityEngine.RigidbodyType2D
        '''
        pass

    @staticmethod
    def get_useFullKinematicContacts():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useFullKinematicContacts(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_isKinematic():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_isKinematic(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_freezeRotation():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_freezeRotation(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_constraints():
        '''
        :returns: RigidbodyConstraints2D
        :rtype: UnityEngine.RigidbodyConstraints2D
        '''
        pass

    @staticmethod
    def set_constraints(arg1):
        '''
        :param arg1: RigidbodyConstraints2D
        :type arg1: UnityEngine.RigidbodyConstraints2D
        '''
        pass

    @staticmethod
    def IsSleeping():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsAwake():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Sleep():
        pass

    @staticmethod
    def WakeUp():
        pass

    @staticmethod
    def get_simulated():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_simulated(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_interpolation():
        '''
        :returns: RigidbodyInterpolation2D
        :rtype: UnityEngine.RigidbodyInterpolation2D
        '''
        pass

    @staticmethod
    def set_interpolation(arg1):
        '''
        :param arg1: RigidbodyInterpolation2D
        :type arg1: UnityEngine.RigidbodyInterpolation2D
        '''
        pass

    @staticmethod
    def get_sleepMode():
        '''
        :returns: RigidbodySleepMode2D
        :rtype: UnityEngine.RigidbodySleepMode2D
        '''
        pass

    @staticmethod
    def set_sleepMode(arg1):
        '''
        :param arg1: RigidbodySleepMode2D
        :type arg1: UnityEngine.RigidbodySleepMode2D
        '''
        pass

    @staticmethod
    def get_collisionDetectionMode():
        '''
        :returns: CollisionDetectionMode2D
        :rtype: UnityEngine.CollisionDetectionMode2D
        '''
        pass

    @staticmethod
    def set_collisionDetectionMode(arg1):
        '''
        :param arg1: CollisionDetectionMode2D
        :type arg1: UnityEngine.CollisionDetectionMode2D
        '''
        pass

    @staticmethod
    def get_attachedColliderCount():
        '''
        :returns: Int32
        :rtype: System.Int32
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
    @overload
    def AddForce(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    @overload
    def AddForce(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: ForceMode2D
        :type arg2: UnityEngine.ForceMode2D
        '''
        pass

    @staticmethod
    def AddForce(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def AddRelativeForce(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    @overload
    def AddRelativeForce(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: ForceMode2D
        :type arg2: UnityEngine.ForceMode2D
        '''
        pass

    @staticmethod
    def AddRelativeForce(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def AddForceAtPosition(arg1, arg2):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    @overload
    def AddForceAtPosition(arg1, arg2, arg3):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        :param arg2: Vector2
        :type arg2: UnityEngine.Vector2
        :param arg3: ForceMode2D
        :type arg3: UnityEngine.ForceMode2D
        '''
        pass

    @staticmethod
    def AddForceAtPosition(arg1=None, arg2=None, arg3=None):
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
