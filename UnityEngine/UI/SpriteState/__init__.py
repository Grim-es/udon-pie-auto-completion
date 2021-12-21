from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class SpriteState:
    def __new__(cls, arg1=None):
        '''
        :returns: SpriteState
        :rtype: UnityEngine.UI.SpriteState
        '''
        pass

    @staticmethod
    def get_highlightedSprite():
        '''
        :returns: Sprite
        :rtype: UnityEngine.Sprite
        '''
        pass

    @staticmethod
    def set_highlightedSprite(arg1):
        '''
        :param arg1: Sprite
        :type arg1: UnityEngine.Sprite
        '''
        pass

    @staticmethod
    def get_pressedSprite():
        '''
        :returns: Sprite
        :rtype: UnityEngine.Sprite
        '''
        pass

    @staticmethod
    def set_pressedSprite(arg1):
        '''
        :param arg1: Sprite
        :type arg1: UnityEngine.Sprite
        '''
        pass

    @staticmethod
    def get_disabledSprite():
        '''
        :returns: Sprite
        :rtype: UnityEngine.Sprite
        '''
        pass

    @staticmethod
    def set_disabledSprite(arg1):
        '''
        :param arg1: Sprite
        :type arg1: UnityEngine.Sprite
        '''
        pass

    @staticmethod
    @overload
    def Equals(arg1):
        '''
        :param arg1: SpriteState
        :type arg1: UnityEngine.SpriteState
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
