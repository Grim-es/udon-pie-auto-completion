from typing import overload

from UdonPie import System
from UdonPie.Undefined import *


class Type:
    def __new__(cls, arg1=None):
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Type
        :type arg2: System.Type
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Type
        :type arg2: System.Type
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def GetType(arg1, arg2, arg3):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :param arg3: Boolean
        :type arg3: System.Boolean or bool
        :returns: Type
        :rtype: System.Type
        '''
        pass

    @staticmethod
    @overload
    def GetType(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Type
        :rtype: System.Type
        '''
        pass

    @staticmethod
    @overload
    def GetType(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Type
        :rtype: System.Type
        '''
        pass

    @staticmethod
    @overload
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass

    @staticmethod
    def GetType(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def get_GUID():
        '''
        :returns: Guid
        :rtype: System.Guid
        '''
        pass

    @staticmethod
    def get_FullName():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_Namespace():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_AssemblyQualifiedName():
        '''
        :returns: String
        :rtype: System.String
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
    def Equals(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Equals(arg1=None):
        pass

    @staticmethod
    def GetHashCode():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_Name():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass
