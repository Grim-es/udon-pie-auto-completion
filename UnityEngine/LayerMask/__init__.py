from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class LayerMask:
    def __new__(cls, arg1=None):
        '''
        :returns: LayerMask
        :rtype: UnityEngine.LayerMask
        '''
        pass

    @staticmethod
    @overload
    def op_Implicit(arg1):
        '''
        :param arg1: LayerMask
        :type arg1: UnityEngine.LayerMask
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    @overload
    def op_Implicit(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: LayerMask
        :rtype: UnityEngine.LayerMask
        '''
        pass

    @staticmethod
    def op_Implicit(arg1=None):
        pass

    @staticmethod
    def get_value():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_value(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def LayerToName(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def NameToLayer(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetMask(arg1):
        '''
        :param arg1: StringArray
        :type arg1: System.StringArray
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
