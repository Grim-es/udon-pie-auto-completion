from typing import overload

from UdonPie import System
from UdonPie.Undefined import *


class Object:
    def __new__(cls, arg1=None):
        '''
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: Object
        :rtype: System.Object
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None, arg2=None):
        pass

    @staticmethod
    def ReferenceEquals(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: System.Object
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
