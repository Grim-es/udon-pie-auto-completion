from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class MinMaxCurve:
    def __new__(cls, arg1=None):
        '''
        :returns: MinMaxCurve
        :rtype: UnityEngine.ParticleSystem.MinMaxCurve
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: AnimationCurve
        :type arg2: UnityEngine.AnimationCurve
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2, arg3):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: AnimationCurve
        :type arg2: UnityEngine.AnimationCurve
        :param arg3: AnimationCurve
        :type arg3: UnityEngine.AnimationCurve
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    def ctor(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def op_Implicit(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: ParticleSystem+MinMaxCurve
        :rtype: UnityEngine.ParticleSystem+MinMaxCurve
        '''
        pass

    @staticmethod
    def get_mode():
        '''
        :returns: ParticleSystemCurveMode
        :rtype: UnityEngine.ParticleSystemCurveMode
        '''
        pass

    @staticmethod
    def set_mode(arg1):
        '''
        :param arg1: ParticleSystemCurveMode
        :type arg1: UnityEngine.ParticleSystemCurveMode
        '''
        pass

    @staticmethod
    def get_curveMultiplier():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_curveMultiplier(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_curveMax():
        '''
        :returns: AnimationCurve
        :rtype: UnityEngine.AnimationCurve
        '''
        pass

    @staticmethod
    def set_curveMax(arg1):
        '''
        :param arg1: AnimationCurve
        :type arg1: UnityEngine.AnimationCurve
        '''
        pass

    @staticmethod
    def get_curveMin():
        '''
        :returns: AnimationCurve
        :rtype: UnityEngine.AnimationCurve
        '''
        pass

    @staticmethod
    def set_curveMin(arg1):
        '''
        :param arg1: AnimationCurve
        :type arg1: UnityEngine.AnimationCurve
        '''
        pass

    @staticmethod
    def get_constantMax():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_constantMax(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_constantMin():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_constantMin(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_constant():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_constant(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_curve():
        '''
        :returns: AnimationCurve
        :rtype: UnityEngine.AnimationCurve
        '''
        pass

    @staticmethod
    def set_curve(arg1):
        '''
        :param arg1: AnimationCurve
        :type arg1: UnityEngine.AnimationCurve
        '''
        pass

    @staticmethod
    @overload
    def Evaluate(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def Evaluate(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def Evaluate(arg1=None, arg2=None):
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
