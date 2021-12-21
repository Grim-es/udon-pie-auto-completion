from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class LayoutUtility:
    def __new__(cls, arg1=None):
        '''
        :returns: LayoutUtility
        :rtype: UnityEngine.UI.LayoutUtility
        '''
        pass

    @staticmethod
    def GetMinSize(arg1, arg2):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetPreferredSize(arg1, arg2):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetFlexibleSize(arg1, arg2):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetMinWidth(arg1):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetPreferredWidth(arg1):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetFlexibleWidth(arg1):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetMinHeight(arg1):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetPreferredHeight(arg1):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetFlexibleHeight(arg1):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def GetLayoutProperty(arg1, arg2, arg3):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :param arg2: Undefined variable
        :type arg2: SystemFunc.SystemFunc
        :param arg3: Single
        :type arg3: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    @overload
    def GetLayoutProperty(arg1, arg2, arg3, arg4):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        :param arg2: Undefined variable
        :type arg2: SystemFunc.SystemFunc
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Undefined variable
        :type arg4: UIILayoutElementRef.UIILayoutElementRef
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetLayoutProperty(arg1=None, arg2=None, arg3=None, arg4=None):
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
