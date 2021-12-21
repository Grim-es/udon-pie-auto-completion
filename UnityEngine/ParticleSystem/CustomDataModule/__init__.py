from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class CustomDataModule:
    def __new__(cls, arg1=None):
        '''
        :returns: CustomDataModule
        :rtype: UnityEngine.ParticleSystem.CustomDataModule
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
    def SetMode(arg1, arg2):
        '''
        :param arg1: ParticleSystemCustomData
        :type arg1: UnityEngine.ParticleSystemCustomData
        :param arg2: ParticleSystemCustomDataMode
        :type arg2: UnityEngine.ParticleSystemCustomDataMode
        '''
        pass

    @staticmethod
    def GetMode(arg1):
        '''
        :param arg1: ParticleSystemCustomData
        :type arg1: UnityEngine.ParticleSystemCustomData
        :returns: ParticleSystemCustomDataMode
        :rtype: UnityEngine.ParticleSystemCustomDataMode
        '''
        pass

    @staticmethod
    def SetVectorComponentCount(arg1, arg2):
        '''
        :param arg1: ParticleSystemCustomData
        :type arg1: UnityEngine.ParticleSystemCustomData
        :param arg2: Int32
        :type arg2: System.Int32 or int
        '''
        pass

    @staticmethod
    def GetVectorComponentCount(arg1):
        '''
        :param arg1: ParticleSystemCustomData
        :type arg1: UnityEngine.ParticleSystemCustomData
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def SetVector(arg1, arg2, arg3):
        '''
        :param arg1: ParticleSystemCustomData
        :type arg1: UnityEngine.ParticleSystemCustomData
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: MinMaxCurve
        :type arg3: UnityEngine.MinMaxCurve
        '''
        pass

    @staticmethod
    def GetVector(arg1, arg2):
        '''
        :param arg1: ParticleSystemCustomData
        :type arg1: UnityEngine.ParticleSystemCustomData
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    def SetColor(arg1, arg2):
        '''
        :param arg1: ParticleSystemCustomData
        :type arg1: UnityEngine.ParticleSystemCustomData
        :param arg2: MinMaxGradient
        :type arg2: UnityEngine.MinMaxGradient
        '''
        pass

    @staticmethod
    def GetColor(arg1):
        '''
        :param arg1: ParticleSystemCustomData
        :type arg1: UnityEngine.ParticleSystemCustomData
        :returns: ParticleSystem+MinMaxGradient
        :rtype: UnityEngine.ParticleSystem+MinMaxGradient
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
