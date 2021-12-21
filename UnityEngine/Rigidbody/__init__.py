from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Rigidbody:
    def __new__(cls, arg1=None):
        '''
        :returns: Rigidbody
        :rtype: UnityEngine.Rigidbody
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
    def AddRelativeForce(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def AddRelativeForce(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: ForceMode
        :type arg4: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    @overload
    def AddRelativeForce(arg1, arg2, arg3):
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
    def AddRelativeForce(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: ForceMode
        :type arg2: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    def AddRelativeForce(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def AddTorque(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: ForceMode
        :type arg2: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    @overload
    def AddTorque(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def AddTorque(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: ForceMode
        :type arg4: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    @overload
    def AddTorque(arg1, arg2, arg3):
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
    def AddTorque(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def AddRelativeTorque(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: ForceMode
        :type arg2: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    @overload
    def AddRelativeTorque(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def AddRelativeTorque(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: ForceMode
        :type arg4: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    @overload
    def AddRelativeTorque(arg1, arg2, arg3):
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
    def AddRelativeTorque(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def AddForceAtPosition(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: ForceMode
        :type arg3: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    @overload
    def AddForceAtPosition(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def AddForceAtPosition(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def AddExplosionForce(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: ForceMode
        :type arg5: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    @overload
    def AddExplosionForce(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def AddExplosionForce(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Single
        :type arg3: System.Single or float
        '''
        pass

    @staticmethod
    def AddExplosionForce(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def ClosestPointOnBounds(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def SweepTest(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Undefined variable
        :type arg2: RaycastHitRef.RaycastHitRef
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: QueryTriggerInteraction
        :type arg4: UnityEngine.QueryTriggerInteraction
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SweepTest(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
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
    def SweepTest(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Undefined variable
        :type arg2: RaycastHitRef.RaycastHitRef
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def SweepTest(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def SweepTestAll(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: QueryTriggerInteraction
        :type arg3: UnityEngine.QueryTriggerInteraction
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def SweepTestAll(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    @overload
    def SweepTestAll(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: RaycastHitArray
        :rtype: UnityEngine.RaycastHitArray
        '''
        pass

    @staticmethod
    def SweepTestAll(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def get_velocity():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_velocity(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
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
    def set_angularVelocity(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
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
    def SetDensity(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_useGravity():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useGravity(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_maxDepenetrationVelocity():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_maxDepenetrationVelocity(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
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
        :returns: RigidbodyConstraints
        :rtype: UnityEngine.RigidbodyConstraints
        '''
        pass

    @staticmethod
    def set_constraints(arg1):
        '''
        :param arg1: RigidbodyConstraints
        :type arg1: UnityEngine.RigidbodyConstraints
        '''
        pass

    @staticmethod
    def get_collisionDetectionMode():
        '''
        :returns: CollisionDetectionMode
        :rtype: UnityEngine.CollisionDetectionMode
        '''
        pass

    @staticmethod
    def set_collisionDetectionMode(arg1):
        '''
        :param arg1: CollisionDetectionMode
        :type arg1: UnityEngine.CollisionDetectionMode
        '''
        pass

    @staticmethod
    def get_centerOfMass():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_centerOfMass(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_worldCenterOfMass():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_inertiaTensorRotation():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def set_inertiaTensorRotation(arg1):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def get_inertiaTensor():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_inertiaTensor(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_detectCollisions():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_detectCollisions(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_position():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_position(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_rotation():
        '''
        :returns: Quaternion
        :rtype: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def set_rotation(arg1):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def get_interpolation():
        '''
        :returns: RigidbodyInterpolation
        :rtype: UnityEngine.RigidbodyInterpolation
        '''
        pass

    @staticmethod
    def set_interpolation(arg1):
        '''
        :param arg1: RigidbodyInterpolation
        :type arg1: UnityEngine.RigidbodyInterpolation
        '''
        pass

    @staticmethod
    def get_solverIterations():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_solverIterations(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_maxAngularVelocity():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_maxAngularVelocity(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def MovePosition(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def MoveRotation(arg1):
        '''
        :param arg1: Quaternion
        :type arg1: UnityEngine.Quaternion
        '''
        pass

    @staticmethod
    def Sleep():
        pass

    @staticmethod
    def IsSleeping():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def WakeUp():
        pass

    @staticmethod
    def ResetCenterOfMass():
        pass

    @staticmethod
    def ResetInertiaTensor():
        pass

    @staticmethod
    def GetRelativePointVelocity(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def GetPointVelocity(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_solverVelocityIterations():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_solverVelocityIterations(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def AddForce(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: ForceMode
        :type arg2: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    @overload
    def AddForce(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def AddForce(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: ForceMode
        :type arg4: UnityEngine.ForceMode
        '''
        pass

    @staticmethod
    @overload
    def AddForce(arg1, arg2, arg3):
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
    def AddForce(arg1=None, arg2=None, arg3=None, arg4=None):
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
