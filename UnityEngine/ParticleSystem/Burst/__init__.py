from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Burst:
    def __new__(cls, arg1=None):
        '''
        :returns: Burst
        :rtype: UnityEngine.ParticleSystem.Burst
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Int16
        :type arg2: System.Int16
        :returns: ParticleSystem+Burst
        :rtype: UnityEngine.ParticleSystem+Burst
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Int16
        :type arg2: System.Int16
        :param arg3: Int16
        :type arg3: System.Int16
        :returns: ParticleSystem+Burst
        :rtype: UnityEngine.ParticleSystem+Burst
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Int16
        :type arg2: System.Int16
        :param arg3: Int16
        :type arg3: System.Int16
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :param arg5: Single
        :type arg5: System.Single or float
        :returns: ParticleSystem+Burst
        :rtype: UnityEngine.ParticleSystem+Burst
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: MinMaxCurve
        :type arg2: UnityEngine.MinMaxCurve
        :returns: ParticleSystem+Burst
        :rtype: UnityEngine.ParticleSystem+Burst
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: MinMaxCurve
        :type arg2: UnityEngine.MinMaxCurve
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: Single
        :type arg4: System.Single or float
        :returns: ParticleSystem+Burst
        :rtype: UnityEngine.ParticleSystem+Burst
        '''
        pass

    @staticmethod
    def ctor(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
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
    def get_count():
        '''
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    def set_count(arg1):
        '''
        :param arg1: MinMaxCurve
        :type arg1: UnityEngine.MinMaxCurve
        '''
        pass

    @staticmethod
    def get_minCount():
        '''
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    def set_minCount(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        '''
        pass

    @staticmethod
    def get_maxCount():
        '''
        :returns: Int16
        :rtype: System.Int16
        '''
        pass

    @staticmethod
    def set_maxCount(arg1):
        '''
        :param arg1: Int16
        :type arg1: System.Int16
        '''
        pass

    @staticmethod
    def get_cycleCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_cycleCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_repeatInterval():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_repeatInterval(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_probability():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_probability(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
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
