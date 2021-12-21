from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Toggle:
    def __new__(cls, arg1=None):
        '''
        :returns: Toggle
        :rtype: UnityEngine.UI.Toggle
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
    def get_toggleTransition():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineUIToggleToggleTransition
        '''
        pass

    @staticmethod
    def set_toggleTransition():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineUIToggleToggleTransition
        '''
        pass

    @staticmethod
    def get_graphic():
        '''
        :returns: Graphic
        :rtype: UnityEngine.Graphic
        '''
        pass

    @staticmethod
    def set_graphic():
        '''
        :returns: Graphic
        :rtype: UnityEngine.Graphic
        '''
        pass

    @staticmethod
    def get_onValueChanged():
        '''
        :returns: Toggle+ToggleEvent
        :rtype: UnityEngine.Toggle+ToggleEvent
        '''
        pass

    @staticmethod
    def set_onValueChanged():
        '''
        :returns: Toggle+ToggleEvent
        :rtype: UnityEngine.Toggle+ToggleEvent
        '''
        pass

    @staticmethod
    def get_group():
        '''
        :returns: ToggleGroup
        :rtype: UnityEngine.ToggleGroup
        '''
        pass

    @staticmethod
    def set_group(arg1):
        '''
        :param arg1: ToggleGroup
        :type arg1: UnityEngine.ToggleGroup
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
    def get_isOn():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_isOn(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def OnPointerClick(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def OnSubmit(arg1):
        '''
        :param arg1: BaseEventData
        :type arg1: UnityEngine.BaseEventData
        '''
        pass

    @staticmethod
    def get_navigation():
        '''
        :returns: Navigation
        :rtype: UnityEngine.Navigation
        '''
        pass

    @staticmethod
    def set_navigation(arg1):
        '''
        :param arg1: Navigation
        :type arg1: UnityEngine.Navigation
        '''
        pass

    @staticmethod
    def get_transition():
        '''
        :returns: Selectable+Transition
        :rtype: UnityEngine.Selectable+Transition
        '''
        pass

    @staticmethod
    def set_transition(arg1):
        '''
        :param arg1: Transition
        :type arg1: UnityEngine.Transition
        '''
        pass

    @staticmethod
    def get_colors():
        '''
        :returns: ColorBlock
        :rtype: UnityEngine.ColorBlock
        '''
        pass

    @staticmethod
    def set_colors(arg1):
        '''
        :param arg1: ColorBlock
        :type arg1: UnityEngine.ColorBlock
        '''
        pass

    @staticmethod
    def get_spriteState():
        '''
        :returns: SpriteState
        :rtype: UnityEngine.SpriteState
        '''
        pass

    @staticmethod
    def set_spriteState(arg1):
        '''
        :param arg1: SpriteState
        :type arg1: UnityEngine.SpriteState
        '''
        pass

    @staticmethod
    def get_animationTriggers():
        '''
        :returns: AnimationTriggers
        :rtype: UnityEngine.AnimationTriggers
        '''
        pass

    @staticmethod
    def set_animationTriggers(arg1):
        '''
        :param arg1: AnimationTriggers
        :type arg1: UnityEngine.AnimationTriggers
        '''
        pass

    @staticmethod
    def get_targetGraphic():
        '''
        :returns: Graphic
        :rtype: UnityEngine.Graphic
        '''
        pass

    @staticmethod
    def set_targetGraphic(arg1):
        '''
        :param arg1: Graphic
        :type arg1: UnityEngine.Graphic
        '''
        pass

    @staticmethod
    def get_interactable():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_interactable(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_image():
        '''
        :returns: Image
        :rtype: UnityEngine.Image
        '''
        pass

    @staticmethod
    def set_image(arg1):
        '''
        :param arg1: Image
        :type arg1: UnityEngine.Image
        '''
        pass

    @staticmethod
    def get_animator():
        '''
        :returns: Animator
        :rtype: UnityEngine.Animator
        '''
        pass

    @staticmethod
    def IsInteractable():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def FindSelectable(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Selectable
        :rtype: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def FindSelectableOnLeft():
        '''
        :returns: Selectable
        :rtype: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def FindSelectableOnRight():
        '''
        :returns: Selectable
        :rtype: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def FindSelectableOnUp():
        '''
        :returns: Selectable
        :rtype: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def FindSelectableOnDown():
        '''
        :returns: Selectable
        :rtype: UnityEngine.Selectable
        '''
        pass

    @staticmethod
    def OnMove(arg1):
        '''
        :param arg1: AxisEventData
        :type arg1: UnityEngine.AxisEventData
        '''
        pass

    @staticmethod
    def OnPointerDown(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def OnPointerUp(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def OnPointerEnter(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def OnPointerExit(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
        '''
        pass

    @staticmethod
    def OnSelect(arg1):
        '''
        :param arg1: BaseEventData
        :type arg1: UnityEngine.BaseEventData
        '''
        pass

    @staticmethod
    def OnDeselect(arg1):
        '''
        :param arg1: BaseEventData
        :type arg1: UnityEngine.BaseEventData
        '''
        pass

    @staticmethod
    def Select():
        pass

    @staticmethod
    def IsActive():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
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
