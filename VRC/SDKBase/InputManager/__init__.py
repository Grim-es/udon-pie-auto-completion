from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie import VRC
from UdonPie.Undefined import *


class InputManager:
    def __new__(cls, arg1=None):
        '''
        :returns: InputManager
        :rtype: VRC.SDKBase.InputManager
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: InputManager
        :rtype: VRC.InputManager
        '''
        pass

    @staticmethod
    def get():
        pass

    @staticmethod
    def set():
        pass

    @staticmethod
    def IsUsingHandController():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetLastUsedInputMethod():
        '''
        :returns: VRCInputMethod
        :rtype: VRC.VRCInputMethod
        '''
        pass

    @staticmethod
    @overload
    def EnableObjectHighlight(arg1, arg2):
        '''
        :param arg1: GameObject
        :type arg1: UnityEngine.GameObject
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def EnableObjectHighlight(arg1, arg2):
        '''
        :param arg1: Renderer
        :type arg1: UnityEngine.Renderer
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    def EnableObjectHighlight(arg1=None, arg2=None):
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
