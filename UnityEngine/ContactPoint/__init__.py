from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class ContactPoint:
    def __new__(cls, arg1=None):
        '''
        :returns: ContactPoint
        :rtype: UnityEngine.ContactPoint
        '''
        pass

    @staticmethod
    def get_point():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_normal():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_thisCollider():
        '''
        :returns: Collider
        :rtype: UnityEngine.Collider
        '''
        pass

    @staticmethod
    def get_otherCollider():
        '''
        :returns: Collider
        :rtype: UnityEngine.Collider
        '''
        pass

    @staticmethod
    def get_separation():
        '''
        :returns: Single
        :rtype: System.Single
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
