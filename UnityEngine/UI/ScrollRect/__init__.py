from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class ScrollRect:
    def __new__(cls, arg1=None):
        '''
        :returns: ScrollRect
        :rtype: UnityEngine.UI.ScrollRect
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
    def get_content():
        '''
        :returns: RectTransform
        :rtype: UnityEngine.RectTransform
        '''
        pass

    @staticmethod
    def set_content(arg1):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        '''
        pass

    @staticmethod
    def get_horizontal():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_horizontal(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_vertical():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_vertical(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_movementType():
        '''
        :returns: ScrollRect+MovementType
        :rtype: UnityEngine.ScrollRect+MovementType
        '''
        pass

    @staticmethod
    def set_movementType(arg1):
        '''
        :param arg1: MovementType
        :type arg1: UnityEngine.MovementType
        '''
        pass

    @staticmethod
    def get_elasticity():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_elasticity(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_inertia():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_inertia(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_decelerationRate():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_decelerationRate(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_scrollSensitivity():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_scrollSensitivity(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_viewport():
        '''
        :returns: RectTransform
        :rtype: UnityEngine.RectTransform
        '''
        pass

    @staticmethod
    def set_viewport(arg1):
        '''
        :param arg1: RectTransform
        :type arg1: UnityEngine.RectTransform
        '''
        pass

    @staticmethod
    def get_horizontalScrollbar():
        '''
        :returns: Scrollbar
        :rtype: UnityEngine.Scrollbar
        '''
        pass

    @staticmethod
    def set_horizontalScrollbar(arg1):
        '''
        :param arg1: Scrollbar
        :type arg1: UnityEngine.Scrollbar
        '''
        pass

    @staticmethod
    def get_verticalScrollbar():
        '''
        :returns: Scrollbar
        :rtype: UnityEngine.Scrollbar
        '''
        pass

    @staticmethod
    def set_verticalScrollbar(arg1):
        '''
        :param arg1: Scrollbar
        :type arg1: UnityEngine.Scrollbar
        '''
        pass

    @staticmethod
    def get_horizontalScrollbarVisibility():
        '''
        :returns: ScrollRect+ScrollbarVisibility
        :rtype: UnityEngine.ScrollRect+ScrollbarVisibility
        '''
        pass

    @staticmethod
    def set_horizontalScrollbarVisibility(arg1):
        '''
        :param arg1: ScrollbarVisibility
        :type arg1: UnityEngine.ScrollbarVisibility
        '''
        pass

    @staticmethod
    def get_verticalScrollbarVisibility():
        '''
        :returns: ScrollRect+ScrollbarVisibility
        :rtype: UnityEngine.ScrollRect+ScrollbarVisibility
        '''
        pass

    @staticmethod
    def set_verticalScrollbarVisibility(arg1):
        '''
        :param arg1: ScrollbarVisibility
        :type arg1: UnityEngine.ScrollbarVisibility
        '''
        pass

    @staticmethod
    def get_horizontalScrollbarSpacing():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_horizontalScrollbarSpacing(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_verticalScrollbarSpacing():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_verticalScrollbarSpacing(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_onValueChanged():
        '''
        :returns: ScrollRect+ScrollRectEvent
        :rtype: UnityEngine.ScrollRect+ScrollRectEvent
        '''
        pass

    @staticmethod
    def set_onValueChanged(arg1):
        '''
        :param arg1: ScrollRectEvent
        :type arg1: UnityEngine.ScrollRectEvent
        '''
        pass

    @staticmethod
    def get_velocity():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_velocity(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def Rebuild(arg1):
        '''
        :param arg1: CanvasUpdate
        :type arg1: UnityEngine.CanvasUpdate
        '''
        pass

    @staticmethod
    def LayoutComplete():
        pass

    @staticmethod
    def GraphicUpdateComplete():
        pass

    @staticmethod
    def IsActive():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def StopMovement():
        pass

    @staticmethod
    def OnScroll(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def OnInitializePotentialDrag(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def OnBeginDrag(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def OnEndDrag(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def OnDrag(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def get_normalizedPosition():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_normalizedPosition(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_horizontalNormalizedPosition():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_horizontalNormalizedPosition(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_verticalNormalizedPosition():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_verticalNormalizedPosition(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def CalculateLayoutInputHorizontal():
        pass

    @staticmethod
    def CalculateLayoutInputVertical():
        pass

    @staticmethod
    def get_minWidth():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_preferredWidth():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_flexibleWidth():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_minHeight():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_preferredHeight():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_flexibleHeight():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_layoutPriority():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def SetLayoutHorizontal():
        pass

    @staticmethod
    def SetLayoutVertical():
        pass

    @staticmethod
    def IsDestroyed():
        '''
        :returns: Boolean
        :rtype: System.Boolean
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
