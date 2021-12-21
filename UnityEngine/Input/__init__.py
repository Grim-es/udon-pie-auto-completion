from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Input:
    def __new__(cls, arg1=None):
        '''
        :returns: Input
        :rtype: UnityEngine.Input
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: Input
        :rtype: UnityEngine.Input
        '''
        pass

    @staticmethod
    def GetAxis(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetAxisRaw(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetButton(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetButtonDown(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetButtonUp(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetMouseButton(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetMouseButtonDown(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetMouseButtonUp(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetJoystickNames():
        '''
        :returns: StringArray
        :rtype: System.StringArray
        '''
        pass

    @staticmethod
    @overload
    def GetKey(arg1):
        '''
        :param arg1: KeyCode
        :type arg1: UnityEngine.KeyCode
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def GetKey(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetKey(arg1=None):
        pass

    @staticmethod
    @overload
    def GetKeyUp(arg1):
        '''
        :param arg1: KeyCode
        :type arg1: UnityEngine.KeyCode
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def GetKeyUp(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetKeyUp(arg1=None):
        pass

    @staticmethod
    @overload
    def GetKeyDown(arg1):
        '''
        :param arg1: KeyCode
        :type arg1: UnityEngine.KeyCode
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def GetKeyDown(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetKeyDown(arg1=None):
        pass

    @staticmethod
    def get_anyKey():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_anyKeyDown():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_inputString():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def get_mousePosition():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_mouseScrollDelta():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_imeIsSelected():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_mousePresent():
        '''
        :returns: Boolean
        :rtype: System.Boolean
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
