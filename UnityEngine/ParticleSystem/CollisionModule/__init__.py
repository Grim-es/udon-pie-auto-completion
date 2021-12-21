from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class CollisionModule:
    def __new__(cls, arg1=None):
        '''
        :returns: CollisionModule
        :rtype: UnityEngine.ParticleSystem.CollisionModule
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
    def get_enabled():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_type(arg1):
        '''
        :param arg1: ParticleSystemCollisionType
        :type arg1: UnityEngine.ParticleSystemCollisionType
        '''
        pass

    @staticmethod
    def get_type():
        '''
        :returns: ParticleSystemCollisionType
        :rtype: UnityEngine.ParticleSystemCollisionType
        '''
        pass

    @staticmethod
    def set_mode(arg1):
        '''
        :param arg1: ParticleSystemCollisionMode
        :type arg1: UnityEngine.ParticleSystemCollisionMode
        '''
        pass

    @staticmethod
    def get_mode():
        '''
        :returns: ParticleSystemCollisionMode
        :rtype: UnityEngine.ParticleSystemCollisionMode
        '''
        pass

    @staticmethod
    def set_dampen(arg1):
        '''
        :param arg1: MinMaxCurve
        :type arg1: UnityEngine.MinMaxCurve
        '''
        pass

    @staticmethod
    def get_dampen():
        '''
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    def get_dampenMultiplier():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_dampenMultiplier(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def set_bounce(arg1):
        '''
        :param arg1: MinMaxCurve
        :type arg1: UnityEngine.MinMaxCurve
        '''
        pass

    @staticmethod
    def get_bounce():
        '''
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    def get_bounceMultiplier():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_bounceMultiplier(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def set_lifetimeLoss(arg1):
        '''
        :param arg1: MinMaxCurve
        :type arg1: UnityEngine.MinMaxCurve
        '''
        pass

    @staticmethod
    def get_lifetimeLoss():
        '''
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    def get_lifetimeLossMultiplier():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_lifetimeLossMultiplier(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_minKillSpeed():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_minKillSpeed(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_maxKillSpeed():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_maxKillSpeed(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_collidesWith():
        '''
        :returns: LayerMask
        :rtype: UnityEngine.LayerMask
        '''
        pass

    @staticmethod
    def set_collidesWith(arg1):
        '''
        :param arg1: LayerMask
        :type arg1: UnityEngine.LayerMask
        '''
        pass

    @staticmethod
    def get_enableDynamicColliders():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_enableDynamicColliders(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_maxCollisionShapes():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_maxCollisionShapes(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def set_quality(arg1):
        '''
        :param arg1: ParticleSystemCollisionQuality
        :type arg1: UnityEngine.ParticleSystemCollisionQuality
        '''
        pass

    @staticmethod
    def get_quality():
        '''
        :returns: ParticleSystemCollisionQuality
        :rtype: UnityEngine.ParticleSystemCollisionQuality
        '''
        pass

    @staticmethod
    def get_voxelSize():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_voxelSize(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_radiusScale():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_radiusScale(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_sendCollisionMessages():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_sendCollisionMessages(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_colliderForce():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_colliderForce(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_multiplyColliderForceByCollisionAngle():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_multiplyColliderForceByCollisionAngle(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_multiplyColliderForceByParticleSpeed():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_multiplyColliderForceByParticleSpeed(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_multiplyColliderForceByParticleSize():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_multiplyColliderForceByParticleSize(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def SetPlane(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Transform
        :type arg2: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def GetPlane(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def get_maxPlaneCount():
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
    def ToString():
        '''
        :returns: String
        :rtype: System.String
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
