from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class ConstraintSource:
    def __new__(cls, arg1=None):
        '''
        :returns: ConstraintSource
        :rtype: UnityEngine.Animations.ConstraintSource
        '''
        pass

    @staticmethod
    def get_sourceTransform():
        '''
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def set_sourceTransform(arg1):
        '''
        :param arg1: Transform
        :type arg1: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def get_weight():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_weight(arg1):
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
