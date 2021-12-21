from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class MuscleHandle:
    def __new__(cls, arg1=None):
        '''
        :returns: MuscleHandle
        :rtype: UnityEngine.Experimental.Animations.MuscleHandle
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: UnityEngineBodyDof.UnityEngineBodyDof
        :returns: MuscleHandle
        :rtype: UnityEngine.MuscleHandle
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: UnityEngineHeadDof.UnityEngineHeadDof
        :returns: MuscleHandle
        :rtype: UnityEngine.MuscleHandle
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: HumanPartDof
        :type arg1: UnityEngine.HumanPartDof
        :param arg2: Undefined variable
        :type arg2: UnityEngineLegDof.UnityEngineLegDof
        :returns: MuscleHandle
        :rtype: UnityEngine.MuscleHandle
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: HumanPartDof
        :type arg1: UnityEngine.HumanPartDof
        :param arg2: Undefined variable
        :type arg2: UnityEngineArmDof.UnityEngineArmDof
        :returns: MuscleHandle
        :rtype: UnityEngine.MuscleHandle
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: HumanPartDof
        :type arg1: UnityEngine.HumanPartDof
        :param arg2: Undefined variable
        :type arg2: UnityEngineFingerDof.UnityEngineFingerDof
        :returns: MuscleHandle
        :rtype: UnityEngine.MuscleHandle
        '''
        pass

    @staticmethod
    def ctor(arg1=None, arg2=None):
        pass

    @staticmethod
    def get_humanPartDof():
        '''
        :returns: HumanPartDof
        :rtype: UnityEngine.HumanPartDof
        '''
        pass

    @staticmethod
    def get_dof():
        '''
        :returns: Int32
        :rtype: System.Int32
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
    def get_muscleHandleCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetMuscleHandles(arg1):
        '''
        :param arg1: MuscleHandleArray
        :type arg1: UnityEngine.MuscleHandleArray
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
