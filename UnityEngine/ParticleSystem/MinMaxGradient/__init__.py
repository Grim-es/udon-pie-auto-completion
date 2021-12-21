from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class MinMaxGradient:
    def __new__(cls, arg1=None):
        '''
        :returns: MinMaxGradient
        :rtype: UnityEngine.ParticleSystem.MinMaxGradient
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :returns: ParticleSystem+MinMaxGradient
        :rtype: UnityEngine.ParticleSystem+MinMaxGradient
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Gradient
        :type arg1: UnityEngine.Gradient
        :returns: ParticleSystem+MinMaxGradient
        :rtype: UnityEngine.ParticleSystem+MinMaxGradient
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :param arg2: Color
        :type arg2: UnityEngine.Color
        :returns: ParticleSystem+MinMaxGradient
        :rtype: UnityEngine.ParticleSystem+MinMaxGradient
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: Gradient
        :type arg1: UnityEngine.Gradient
        :param arg2: Gradient
        :type arg2: UnityEngine.Gradient
        :returns: ParticleSystem+MinMaxGradient
        :rtype: UnityEngine.ParticleSystem+MinMaxGradient
        '''
        pass

    @staticmethod
    def ctor(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def op_Implicit(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        :returns: ParticleSystem+MinMaxGradient
        :rtype: UnityEngine.ParticleSystem+MinMaxGradient
        '''
        pass

    @staticmethod
    @overload
    def op_Implicit(arg1):
        '''
        :param arg1: Gradient
        :type arg1: UnityEngine.Gradient
        :returns: ParticleSystem+MinMaxGradient
        :rtype: UnityEngine.ParticleSystem+MinMaxGradient
        '''
        pass

    @staticmethod
    def op_Implicit(arg1=None):
        pass

    @staticmethod
    def get_mode():
        '''
        :returns: ParticleSystemGradientMode
        :rtype: UnityEngine.ParticleSystemGradientMode
        '''
        pass

    @staticmethod
    def set_mode(arg1):
        '''
        :param arg1: ParticleSystemGradientMode
        :type arg1: UnityEngine.ParticleSystemGradientMode
        '''
        pass

    @staticmethod
    def get_gradientMax():
        '''
        :returns: Gradient
        :rtype: UnityEngine.Gradient
        '''
        pass

    @staticmethod
    def set_gradientMax(arg1):
        '''
        :param arg1: Gradient
        :type arg1: UnityEngine.Gradient
        '''
        pass

    @staticmethod
    def get_gradientMin():
        '''
        :returns: Gradient
        :rtype: UnityEngine.Gradient
        '''
        pass

    @staticmethod
    def set_gradientMin(arg1):
        '''
        :param arg1: Gradient
        :type arg1: UnityEngine.Gradient
        '''
        pass

    @staticmethod
    def get_colorMax():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_colorMax(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_colorMin():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_colorMin(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_color():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_color(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_gradient():
        '''
        :returns: Gradient
        :rtype: UnityEngine.Gradient
        '''
        pass

    @staticmethod
    def set_gradient(arg1):
        '''
        :param arg1: Gradient
        :type arg1: UnityEngine.Gradient
        '''
        pass

    @staticmethod
    @overload
    def Evaluate(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :returns: Color
        :rtype: UnityEngine.Color
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
        :returns: Color
        :rtype: UnityEngine.Color
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
