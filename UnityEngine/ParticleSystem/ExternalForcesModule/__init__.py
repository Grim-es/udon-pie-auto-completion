from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class ExternalForcesModule:
    def __new__(cls, arg1=None):
        '''
        :returns: ExternalForcesModule
        :rtype: UnityEngine.ParticleSystem.ExternalForcesModule
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
    def get_multiplier():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_multiplier(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_influenceFilter():
        '''
        :returns: ParticleSystemGameObjectFilter
        :rtype: UnityEngine.ParticleSystemGameObjectFilter
        '''
        pass

    @staticmethod
    def set_influenceFilter(arg1):
        '''
        :param arg1: ParticleSystemGameObjectFilter
        :type arg1: UnityEngine.ParticleSystemGameObjectFilter
        '''
        pass

    @staticmethod
    def get_influenceCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def AddInfluence(arg1):
        '''
        :param arg1: ParticleSystemForceField
        :type arg1: UnityEngine.ParticleSystemForceField
        '''
        pass

    @staticmethod
    @overload
    def RemoveInfluence(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def RemoveInfluence(arg1):
        '''
        :param arg1: ParticleSystemForceField
        :type arg1: UnityEngine.ParticleSystemForceField
        '''
        pass

    @staticmethod
    def RemoveInfluence(arg1=None):
        pass

    @staticmethod
    def SetInfluence(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: ParticleSystemForceField
        :type arg2: UnityEngine.ParticleSystemForceField
        '''
        pass

    @staticmethod
    def GetInfluence(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: ParticleSystemForceField
        :rtype: UnityEngine.ParticleSystemForceField
        '''
        pass

    @staticmethod
    def IsAffectedBy(arg1):
        '''
        :param arg1: ParticleSystemForceField
        :type arg1: UnityEngine.ParticleSystemForceField
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
