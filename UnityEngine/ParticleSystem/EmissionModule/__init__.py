from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class EmissionModule:
    def __new__(cls, arg1=None):
        '''
        :returns: EmissionModule
        :rtype: UnityEngine.ParticleSystem.EmissionModule
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
    def set_rateOverTime(arg1):
        '''
        :param arg1: MinMaxCurve
        :type arg1: UnityEngine.MinMaxCurve
        '''
        pass

    @staticmethod
    def get_rateOverTime():
        '''
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    def get_rateOverTimeMultiplier():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_rateOverTimeMultiplier(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def set_rateOverDistance(arg1):
        '''
        :param arg1: MinMaxCurve
        :type arg1: UnityEngine.MinMaxCurve
        '''
        pass

    @staticmethod
    def get_rateOverDistance():
        '''
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    def get_rateOverDistanceMultiplier():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_rateOverDistanceMultiplier(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def SetBursts(arg1):
        '''
        :param arg1: BurstArray
        :type arg1: UnityEngine.BurstArray
        '''
        pass

    @staticmethod
    @overload
    def SetBursts(arg1, arg2):
        '''
        :param arg1: BurstArray
        :type arg1: UnityEngine.BurstArray
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def SetBursts(arg1=None, arg2=None):
        pass

    @staticmethod
    def GetBursts(arg1):
        '''
        :param arg1: BurstArray
        :type arg1: UnityEngine.BurstArray
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def SetBurst(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Burst
        :type arg2: UnityEngine.Burst
        '''
        pass

    @staticmethod
    def GetBurst(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: ParticleSystem+Burst
        :rtype: UnityEngine.ParticleSystem+Burst
        '''
        pass

    @staticmethod
    def get_burstCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_burstCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
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
