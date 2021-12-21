from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class AvatarMask:
    def __new__(cls, arg1=None):
        '''
        :returns: AvatarMask
        :rtype: UnityEngine.AvatarMask
        '''
        pass

    @staticmethod
    def op_Implicit(arg1):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Equality(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def op_Inequality(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def GetHumanoidBodyPartActive(arg1):
        '''
        :param arg1: AvatarMaskBodyPart
        :type arg1: UnityEngine.AvatarMaskBodyPart
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def SetHumanoidBodyPartActive(arg1, arg2):
        '''
        :param arg1: AvatarMaskBodyPart
        :type arg1: UnityEngine.AvatarMaskBodyPart
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_transformCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_transformCount(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def AddTransformPath(arg1):
        '''
        :param arg1: Transform
        :type arg1: UnityEngine.Transform
        '''
        pass

    @staticmethod
    @overload
    def AddTransformPath(arg1, arg2):
        '''
        :param arg1: Transform
        :type arg1: UnityEngine.Transform
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    def AddTransformPath(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def RemoveTransformPath(arg1):
        '''
        :param arg1: Transform
        :type arg1: UnityEngine.Transform
        '''
        pass

    @staticmethod
    @overload
    def RemoveTransformPath(arg1, arg2):
        '''
        :param arg1: Transform
        :type arg1: UnityEngine.Transform
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    def RemoveTransformPath(arg1=None, arg2=None):
        pass

    @staticmethod
    def GetTransformPath(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def SetTransformPath(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: String
        :type arg2: System.String or str
        '''
        pass

    @staticmethod
    def GetTransformActive(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def SetTransformActive(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        '''
        pass

    @staticmethod
    def GetInstanceID():
        '''
        :returns: Int32
        :rtype: System.Int32
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
    def Equals(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_name():
        '''
        :returns: String
        :rtype: System.String
        '''
        pass

    @staticmethod
    def set_name(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
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
    def GetType():
        '''
        :returns: Type
        :rtype: System.Type
        '''
        pass
