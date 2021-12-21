from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Debug:
    def __new__(cls, arg1=None):
        '''
        :returns: Debug
        :rtype: UnityEngine.Debug
        '''
        pass

    @staticmethod
    def ctor():
        '''
        :returns: Debug
        :rtype: UnityEngine.Debug
        '''
        pass

    @staticmethod
    @overload
    def DrawLine(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Color
        :type arg3: UnityEngine.Color
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def DrawLine(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Color
        :type arg3: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def DrawLine(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def DrawLine(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Color
        :type arg3: UnityEngine.Color
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Boolean
        :type arg5: System.Boolean or bool
        '''
        pass

    @staticmethod
    def DrawLine(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    @overload
    def DrawRay(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Color
        :type arg3: UnityEngine.Color
        :param arg4: Single
        :type arg4: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def DrawRay(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Color
        :type arg3: UnityEngine.Color
        '''
        pass

    @staticmethod
    @overload
    def DrawRay(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def DrawRay(arg1, arg2, arg3, arg4, arg5):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Color
        :type arg3: UnityEngine.Color
        :param arg4: Single
        :type arg4: System.Single or float
        :param arg5: Boolean
        :type arg5: System.Boolean or bool
        '''
        pass

    @staticmethod
    def DrawRay(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
        pass

    @staticmethod
    def DebugBreak():
        pass

    @staticmethod
    @overload
    def Log(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        '''
        pass

    @staticmethod
    @overload
    def Log(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        '''
        pass

    @staticmethod
    def Log(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def LogFormat(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: ObjectArray
        :type arg2: System.ObjectArray
        '''
        pass

    @staticmethod
    @overload
    def LogFormat(arg1, arg2, arg3):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: ObjectArray
        :type arg3: System.ObjectArray
        '''
        pass

    @staticmethod
    def LogFormat(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def LogError(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        '''
        pass

    @staticmethod
    @overload
    def LogError(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        '''
        pass

    @staticmethod
    def LogError(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def LogErrorFormat(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: ObjectArray
        :type arg2: System.ObjectArray
        '''
        pass

    @staticmethod
    @overload
    def LogErrorFormat(arg1, arg2, arg3):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: ObjectArray
        :type arg3: System.ObjectArray
        '''
        pass

    @staticmethod
    def LogErrorFormat(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def get_developerConsoleVisible():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_developerConsoleVisible(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def LogException(arg1):
        '''
        :param arg1: Exception
        :type arg1: System.Exception
        '''
        pass

    @staticmethod
    @overload
    def LogException(arg1, arg2):
        '''
        :param arg1: Exception
        :type arg1: System.Exception
        :param arg2: Object
        :type arg2: UnityEngine.Object
        '''
        pass

    @staticmethod
    def LogException(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def LogWarning(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        '''
        pass

    @staticmethod
    @overload
    def LogWarning(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        '''
        pass

    @staticmethod
    def LogWarning(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def LogWarningFormat(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: ObjectArray
        :type arg2: System.ObjectArray
        '''
        pass

    @staticmethod
    @overload
    def LogWarningFormat(arg1, arg2, arg3):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: ObjectArray
        :type arg3: System.ObjectArray
        '''
        pass

    @staticmethod
    def LogWarningFormat(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def Assert(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    @overload
    def Assert(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Object
        :type arg2: UnityEngine.Object
        '''
        pass

    @staticmethod
    @overload
    def Assert(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Object
        :type arg2: System.Object
        '''
        pass

    @staticmethod
    @overload
    def Assert(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: String
        :type arg2: System.String or str
        '''
        pass

    @staticmethod
    @overload
    def Assert(arg1, arg2, arg3):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Object
        :type arg2: System.Object
        :param arg3: Object
        :type arg3: UnityEngine.Object
        '''
        pass

    @staticmethod
    @overload
    def Assert(arg1, arg2, arg3):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: Object
        :type arg3: UnityEngine.Object
        '''
        pass

    @staticmethod
    def Assert(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def AssertFormat(arg1, arg2, arg3):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: ObjectArray
        :type arg3: System.ObjectArray
        '''
        pass

    @staticmethod
    @overload
    def AssertFormat(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Object
        :type arg2: UnityEngine.Object
        :param arg3: String
        :type arg3: System.String or str
        :param arg4: ObjectArray
        :type arg4: System.ObjectArray
        '''
        pass

    @staticmethod
    def AssertFormat(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def LogAssertion(arg1):
        '''
        :param arg1: Object
        :type arg1: System.Object
        '''
        pass

    @staticmethod
    @overload
    def LogAssertion(arg1, arg2):
        '''
        :param arg1: Object
        :type arg1: System.Object
        :param arg2: Object
        :type arg2: UnityEngine.Object
        '''
        pass

    @staticmethod
    def LogAssertion(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def LogAssertionFormat(arg1, arg2):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :param arg2: ObjectArray
        :type arg2: System.ObjectArray
        '''
        pass

    @staticmethod
    @overload
    def LogAssertionFormat(arg1, arg2, arg3):
        '''
        :param arg1: Object
        :type arg1: UnityEngine.Object
        :param arg2: String
        :type arg2: System.String or str
        :param arg3: ObjectArray
        :type arg3: System.ObjectArray
        '''
        pass

    @staticmethod
    def LogAssertionFormat(arg1=None, arg2=None, arg3=None):
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
