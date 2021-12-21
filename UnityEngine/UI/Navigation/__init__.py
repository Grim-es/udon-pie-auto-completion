from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Navigation:
    def __new__(cls, arg1=None):
        '''
        :returns: Navigation
        :rtype: UnityEngine.UI.Navigation
        '''
        pass

    @staticmethod
    def get_mode():
        '''
        :returns: Navigation+Mode
        :rtype: UnityEngine.Navigation+Mode
        '''
        pass

    @staticmethod
    def set_mode(arg1):
        '''
        :param arg1: Mode
        :type arg1: UnityEngine.Mode
        '''
        pass

    @staticmethod
    def get_selectOnUp():
        '''
        :returns: Selectable
        :rtype: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def set_selectOnUp(arg1):
        '''
        :param arg1: Selectable
        :type arg1: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def get_selectOnDown():
        '''
        :returns: Selectable
        :rtype: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def set_selectOnDown(arg1):
        '''
        :param arg1: Selectable
        :type arg1: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def get_selectOnLeft():
        '''
        :returns: Selectable
        :rtype: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def set_selectOnLeft(arg1):
        '''
        :param arg1: Selectable
        :type arg1: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def get_selectOnRight():
        '''
        :returns: Selectable
        :rtype: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def set_selectOnRight(arg1):
        '''
        :param arg1: Selectable
        :type arg1: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def get_defaultNavigation():
        '''
        :returns: Navigation
        :rtype: UnityEngine.Navigation
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1):
        '''
        :param arg1: Navigation
        :type arg1: UnityEngine.Navigation
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
    def Equals(arg1=None):
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
