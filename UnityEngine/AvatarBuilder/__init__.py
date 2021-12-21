from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class AvatarBuilder:
    def __new__(cls, arg1=None):
        '''
        :returns: AvatarBuilder
        :rtype: UnityEngine.AvatarBuilder
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: AvatarBuilder
        :rtype: UnityEngine.AvatarBuilder
        '''
        pass

    @staticmethod
    def BuildHumanAvatar(arg1, arg2):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        :param arg2: HumanDescription
        :type arg2: UnityEngine.HumanDescription
        :returns: Avatar
        :rtype: UnityEngine.Avatar
        '''
        pass

    @staticmethod
    def BuildGenericAvatar(arg1, arg2):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        :param arg2: String
        :type arg2: System.String or str
        :returns: Avatar
        :rtype: UnityEngine.Avatar
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
