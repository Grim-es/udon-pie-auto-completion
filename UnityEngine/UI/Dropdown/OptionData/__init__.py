from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class OptionData:
    def __new__(cls, arg1=None):
        '''
        :returns: OptionData
        :rtype: UnityEngine.UI.Dropdown.OptionData
        '''
        pass

    @staticmethod
    @overload
    def ctor():
        '''
        :returns: Dropdown+OptionData
        :rtype: UnityEngine.Dropdown+OptionData
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Dropdown+OptionData
        :rtype: UnityEngine.Dropdown+OptionData
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1):
        '''
        :param arg1: Sprite
        :type arg1: UnityEngine.Sprite
        :returns: Dropdown+OptionData
        :rtype: UnityEngine.Dropdown+OptionData
        '''
        pass

    @staticmethod
    @overload
    def ctor(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: Sprite
        :type arg2: UnityEngine.Sprite
        :returns: Dropdown+OptionData
        :rtype: UnityEngine.Dropdown+OptionData
        '''
        pass

    @staticmethod
    def ctor(arg1=None, arg2=None):
        pass

    @staticmethod
    def get_text():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def set_text(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        '''
        pass

    @staticmethod
    def get_image():
        '''
        :returns: Sprite
        :rtype: UnityEngine.Sprite
        '''
        pass

    @staticmethod
    def set_image(arg1):
        '''
        :param arg1: Sprite
        :type arg1: UnityEngine.Sprite
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
