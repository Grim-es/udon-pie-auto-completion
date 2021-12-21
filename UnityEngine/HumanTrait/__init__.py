from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class HumanTrait:
    def __new__(cls, arg1=None):
        '''
        :returns: HumanTrait
        :rtype: UnityEngine.HumanTrait
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: HumanTrait
        :rtype: UnityEngine.HumanTrait
        '''
        pass

    @staticmethod
    def get_MuscleCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_MuscleName():
        '''
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    def get_BoneCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_BoneName():
        '''
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    def MuscleFromBone(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def BoneFromMuscle(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def RequiredBone(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_RequiredBoneCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetMuscleDefaultMin(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetMuscleDefaultMax(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetBoneDefaultHierarchyMass(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetParentBone(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
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

    @staticmethod
    def ToString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass
