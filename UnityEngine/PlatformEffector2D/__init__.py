from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class PlatformEffector2D:
    def __new__(cls, arg1=None):
        '''
        :returns: PlatformEffector2D
        :rtype: UnityEngine.PlatformEffector2D
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
    def get_useOneWay():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useOneWay(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_useOneWayGrouping():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useOneWayGrouping(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_useSideFriction():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useSideFriction(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_useSideBounce():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useSideBounce(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_surfaceArc():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_surfaceArc(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_sideArc():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_sideArc(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_rotationalOffset():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_rotationalOffset(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_useColliderMask():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useColliderMask(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_colliderMask():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_colliderMask(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_enabled():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_enabled(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_transform():
        '''
        :returns: Transform
        :rtype: UnityEngine.Transform
        '''
        pass

    @staticmethod
    def get_gameObject():
        '''
        :returns: GameObject
        :rtype: UnityEngine.GameObject
        '''
        pass

    @staticmethod
    @overload
    def GetComponent(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    @overload
    def GetComponent(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def GetComponent(arg1=None):
        pass

    @staticmethod
    @overload
    def GetComponentInChildren(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    @overload
    def GetComponentInChildren(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def GetComponentInChildren(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Undefined variable
        :type arg2: ListT.ListT
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInChildren(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: ListT.ListT
        '''
        pass

    @staticmethod
    def GetComponentsInChildren(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetComponentInParent(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: Component
        :rtype: UnityEngine.Component
        '''
        pass

    @staticmethod
    def GetComponentInParent(arg1=None):
        pass

    @staticmethod
    @overload
    def GetComponentsInParent(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Boolean
        :type arg2: System.Boolean or bool
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInParent(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponentsInParent(arg1, arg2):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        :param arg2: Undefined variable
        :type arg2: ListT.ListT
        '''
        pass

    @staticmethod
    def GetComponentsInParent(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def GetComponents(arg1):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :returns: ComponentArray
        :rtype: UnityEngine.ComponentArray
        '''
        pass

    @staticmethod
    @overload
    def GetComponents(arg1, arg2):
        '''
        :param arg1: Type
        :type arg1: System.Type
        :param arg2: Undefined variable
        :type arg2: SystemCollectionsGenericList.SystemCollectionsGenericList
        '''
        pass

    @staticmethod
    @overload
    def GetComponents(arg1):
        '''
        :param arg1: Undefined variable
        :type arg1: ListT.ListT
        '''
        pass

    @staticmethod
    def GetComponents(arg1=None, arg2=None):
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
