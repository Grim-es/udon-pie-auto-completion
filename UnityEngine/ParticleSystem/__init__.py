from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class ParticleSystem:
    def __new__(cls, arg1=None):
        '''
        :returns: ParticleSystem
        :rtype: UnityEngine.ParticleSystem
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
    def Simulate(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        :param arg4: Boolean
        :type arg4: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def Simulate(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def Simulate(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def Simulate(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def Simulate(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def Play(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def Play():
        pass

    @staticmethod
    def Play(arg1=None):
        pass

    @staticmethod
    @overload
    def Pause(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def Pause():
        pass

    @staticmethod
    def Pause(arg1=None):
        pass

    @staticmethod
    @overload
    def Stop(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: ParticleSystemStopBehavior
        :type arg2: UnityEngine.ParticleSystemStopBehavior
        '''
        pass

    @staticmethod
    @overload
    def Stop(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def Stop():
        pass

    @staticmethod
    def Stop(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def Clear(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def Clear():
        pass

    @staticmethod
    def Clear(arg1=None):
        pass

    @staticmethod
    @overload
    def IsAlive(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def IsAlive():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def IsAlive(arg1=None):
        pass

    @staticmethod
    @overload
    def Emit(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def Emit(arg1, arg2):
        '''
        :param arg1: EmitParams
        :type arg1: UnityEngine.EmitParams
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def Emit(arg1=None, arg2=None):
        pass

    @staticmethod
    def SetCustomParticleData(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: ParticleSystemCustomData
        :type arg2: UnityEngine.ParticleSystemCustomData
        '''
        pass

    @staticmethod
    def GetCustomParticleData(arg1, arg2):
        '''
        :param arg1: Undefined variable
        :type arg1: SystemCollectionsGenericList.SystemCollectionsGenericList
        :param arg2: ParticleSystemCustomData
        :type arg2: UnityEngine.ParticleSystemCustomData
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def TriggerSubEmitter(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def TriggerSubEmitter(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: ParticleSystemParticleRef.ParticleSystemParticleRef
        '''
        pass

    @staticmethod
    @overload
    def TriggerSubEmitter(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    def TriggerSubEmitter(arg1=None, arg2=None):
        pass

    @staticmethod
    def get_isPlaying():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_isEmitting():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_isStopped():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_isPaused():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_particleCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_time():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_time(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_randomSeed():
        '''
        :returns: UInt32
        :rtype: System.UInt32
        '''
        pass

    @staticmethod
    def set_randomSeed(arg1):
        '''
        :param arg1: UInt32
        :type arg1: System.UInt32
        '''
        pass

    @staticmethod
    def get_useAutoRandomSeed():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useAutoRandomSeed(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_proceduralSimulationSupported():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_main():
        '''
        :returns: ParticleSystem+MainModule
        :rtype: UnityEngine.ParticleSystem+MainModule
        '''
        pass

    @staticmethod
    def get_emission():
        '''
        :returns: ParticleSystem+EmissionModule
        :rtype: UnityEngine.ParticleSystem+EmissionModule
        '''
        pass

    @staticmethod
    def get_shape():
        '''
        :returns: ParticleSystem+ShapeModule
        :rtype: UnityEngine.ParticleSystem+ShapeModule
        '''
        pass

    @staticmethod
    def get_velocityOverLifetime():
        '''
        :returns: ParticleSystem+VelocityOverLifetimeModule
        :rtype: UnityEngine.ParticleSystem+VelocityOverLifetimeModule
        '''
        pass

    @staticmethod
    def get_limitVelocityOverLifetime():
        '''
        :returns: ParticleSystem+LimitVelocityOverLifetimeModule
        :rtype: UnityEngine.ParticleSystem+LimitVelocityOverLifetimeModule
        '''
        pass

    @staticmethod
    def get_inheritVelocity():
        '''
        :returns: ParticleSystem+InheritVelocityModule
        :rtype: UnityEngine.ParticleSystem+InheritVelocityModule
        '''
        pass

    @staticmethod
    def get_forceOverLifetime():
        '''
        :returns: ParticleSystem+ForceOverLifetimeModule
        :rtype: UnityEngine.ParticleSystem+ForceOverLifetimeModule
        '''
        pass

    @staticmethod
    def get_colorOverLifetime():
        '''
        :returns: ParticleSystem+ColorOverLifetimeModule
        :rtype: UnityEngine.ParticleSystem+ColorOverLifetimeModule
        '''
        pass

    @staticmethod
    def get_colorBySpeed():
        '''
        :returns: ParticleSystem+ColorBySpeedModule
        :rtype: UnityEngine.ParticleSystem+ColorBySpeedModule
        '''
        pass

    @staticmethod
    def get_sizeOverLifetime():
        '''
        :returns: ParticleSystem+SizeOverLifetimeModule
        :rtype: UnityEngine.ParticleSystem+SizeOverLifetimeModule
        '''
        pass

    @staticmethod
    def get_sizeBySpeed():
        '''
        :returns: ParticleSystem+SizeBySpeedModule
        :rtype: UnityEngine.ParticleSystem+SizeBySpeedModule
        '''
        pass

    @staticmethod
    def get_rotationOverLifetime():
        '''
        :returns: ParticleSystem+RotationOverLifetimeModule
        :rtype: UnityEngine.ParticleSystem+RotationOverLifetimeModule
        '''
        pass

    @staticmethod
    def get_rotationBySpeed():
        '''
        :returns: ParticleSystem+RotationBySpeedModule
        :rtype: UnityEngine.ParticleSystem+RotationBySpeedModule
        '''
        pass

    @staticmethod
    def get_externalForces():
        '''
        :returns: ParticleSystem+ExternalForcesModule
        :rtype: UnityEngine.ParticleSystem+ExternalForcesModule
        '''
        pass

    @staticmethod
    def get_noise():
        '''
        :returns: ParticleSystem+NoiseModule
        :rtype: UnityEngine.ParticleSystem+NoiseModule
        '''
        pass

    @staticmethod
    def get_collision():
        '''
        :returns: ParticleSystem+CollisionModule
        :rtype: UnityEngine.ParticleSystem+CollisionModule
        '''
        pass

    @staticmethod
    def get_trigger():
        '''
        :returns: ParticleSystem+TriggerModule
        :rtype: UnityEngine.ParticleSystem+TriggerModule
        '''
        pass

    @staticmethod
    def get_subEmitters():
        '''
        :returns: ParticleSystem+SubEmittersModule
        :rtype: UnityEngine.ParticleSystem+SubEmittersModule
        '''
        pass

    @staticmethod
    def get_textureSheetAnimation():
        '''
        :returns: ParticleSystem+TextureSheetAnimationModule
        :rtype: UnityEngine.ParticleSystem+TextureSheetAnimationModule
        '''
        pass

    @staticmethod
    def get_lights():
        '''
        :returns: ParticleSystem+LightsModule
        :rtype: UnityEngine.ParticleSystem+LightsModule
        '''
        pass

    @staticmethod
    def get_trails():
        '''
        :returns: ParticleSystem+TrailModule
        :rtype: UnityEngine.ParticleSystem+TrailModule
        '''
        pass

    @staticmethod
    def get_customData():
        '''
        :returns: ParticleSystem+CustomDataModule
        :rtype: UnityEngine.ParticleSystem+CustomDataModule
        '''
        pass

    @staticmethod
    @overload
    def SetParticles(arg1, arg2, arg3):
        '''
        :param arg1: ParticleArray
        :type arg1: UnityEngine.ParticleArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetParticles(arg1, arg2):
        '''
        :param arg1: ParticleArray
        :type arg1: UnityEngine.ParticleArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetParticles(arg1):
        '''
        :param arg1: ParticleArray
        :type arg1: UnityEngine.ParticleArray
        '''
        pass

    @staticmethod
    def SetParticles(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def GetParticles(arg1, arg2, arg3):
        '''
        :param arg1: ParticleArray
        :type arg1: UnityEngine.ParticleArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetParticles(arg1, arg2):
        '''
        :param arg1: ParticleArray
        :type arg1: UnityEngine.ParticleArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def GetParticles(arg1):
        '''
        :param arg1: ParticleArray
        :type arg1: UnityEngine.ParticleArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetParticles(arg1=None, arg2=None, arg3=None):
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
