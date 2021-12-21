from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class SubEmittersModule:
    def __new__(cls, arg1=None):
        '''
        :returns: SubEmittersModule
        :rtype: UnityEngine.ParticleSystem.SubEmittersModule
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
    def get_subEmittersCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def AddSubEmitter(arg1, arg2, arg3):
        '''
        :param arg1: ParticleSystem
        :type arg1: UnityEngine.ParticleSystem
        :param arg2: ParticleSystemSubEmitterType
        :type arg2: UnityEngine.ParticleSystemSubEmitterType
        :param arg3: ParticleSystemSubEmitterProperties
        :type arg3: UnityEngine.ParticleSystemSubEmitterProperties
        '''
        pass

    @staticmethod
    @overload
    def AddSubEmitter(arg1, arg2, arg3, arg4):
        '''
        :param arg1: ParticleSystem
        :type arg1: UnityEngine.ParticleSystem
        :param arg2: ParticleSystemSubEmitterType
        :type arg2: UnityEngine.ParticleSystemSubEmitterType
        :param arg3: ParticleSystemSubEmitterProperties
        :type arg3: UnityEngine.ParticleSystemSubEmitterProperties
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    def AddSubEmitter(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def RemoveSubEmitter(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def SetSubEmitterSystem(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: ParticleSystem
        :type arg2: UnityEngine.ParticleSystem
        '''
        pass

    @staticmethod
    def SetSubEmitterType(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: ParticleSystemSubEmitterType
        :type arg2: UnityEngine.ParticleSystemSubEmitterType
        '''
        pass

    @staticmethod
    def SetSubEmitterEmitProbability(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    def SetSubEmitterProperties(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: ParticleSystemSubEmitterProperties
        :type arg2: UnityEngine.ParticleSystemSubEmitterProperties
        '''
        pass

    @staticmethod
    def GetSubEmitterSystem(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: ParticleSystem
        :rtype: UnityEngine.ParticleSystem
        '''
        pass

    @staticmethod
    def GetSubEmitterType(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: ParticleSystemSubEmitterType
        :rtype: UnityEngine.ParticleSystemSubEmitterType
        '''
        pass

    @staticmethod
    def GetSubEmitterEmitProbability(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetSubEmitterProperties(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: ParticleSystemSubEmitterProperties
        :rtype: UnityEngine.ParticleSystemSubEmitterProperties
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
