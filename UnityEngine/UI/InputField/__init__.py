from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class InputField:
    def __new__(cls, arg1=None):
        '''
        :returns: InputField
        :rtype: UnityEngine.UI.InputField
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
    def ProcessEvent(arg1):
        '''
        :param arg1: Event
        :type arg1: UnityEngine.Event
        '''
        pass

    @staticmethod
    def OnUpdateSelected(arg1):
        '''
        :param arg1: BaseEventData
        :type arg1: UnityEngine.BaseEventData
        '''
        pass

    @staticmethod
    def ForceLabelUpdate():
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
    def ActivateInputField():
        pass

    @staticmethod
    def OnSelect(arg1):
        '''
        :param arg1: BaseEventData
        :type arg1: UnityEngine.BaseEventData
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
    def DeactivateInputField():
        pass

    @staticmethod
    def OnDeselect(arg1):
        '''
        :param arg1: BaseEventData
        :type arg1: UnityEngine.BaseEventData
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
    def set_shouldHideMobileInput(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_shouldHideMobileInput():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
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
    def get_isFocused():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_caretBlinkRate():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_caretBlinkRate(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_caretWidth():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_caretWidth(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_textComponent():
        '''
        :returns: Text
        :rtype: UnityEngine.Text
        '''
        pass

    @staticmethod
    def set_textComponent(arg1):
        '''
        :param arg1: Text
        :type arg1: UnityEngine.Text
        '''
        pass

    @staticmethod
    def get_placeholder():
        '''
        :returns: Graphic
        :rtype: UnityEngine.Graphic
        '''
        pass

    @staticmethod
    def set_placeholder(arg1):
        '''
        :param arg1: Graphic
        :type arg1: UnityEngine.Graphic
        '''
        pass

    @staticmethod
    def get_caretColor():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_caretColor(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_customCaretColor():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_customCaretColor(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_selectionColor():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_selectionColor(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_onEndEdit():
        '''
        :returns: InputField+SubmitEvent
        :rtype: UnityEngine.InputField+SubmitEvent
        '''
        pass

    @staticmethod
    def set_onEndEdit(arg1):
        '''
        :param arg1: SubmitEvent
        :type arg1: UnityEngine.SubmitEvent
        '''
        pass

    @staticmethod
    def get_onValueChanged():
        '''
        :returns: InputField+OnChangeEvent
        :rtype: UnityEngine.InputField+OnChangeEvent
        '''
        pass

    @staticmethod
    def set_onValueChanged(arg1):
        '''
        :param arg1: OnChangeEvent
        :type arg1: UnityEngine.OnChangeEvent
        '''
        pass

    @staticmethod
    def get_onValidateInput():
        '''
        :returns: InputField+OnValidateInput
        :rtype: UnityEngine.InputField+OnValidateInput
        '''
        pass

    @staticmethod
    def set_onValidateInput(arg1):
        '''
        :param arg1: OnValidateInput
        :type arg1: UnityEngine.OnValidateInput
        '''
        pass

    @staticmethod
    def get_characterLimit():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_characterLimit(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_contentType():
        '''
        :returns: InputField+ContentType
        :rtype: UnityEngine.InputField+ContentType
        '''
        pass

    @staticmethod
    def set_contentType(arg1):
        '''
        :param arg1: ContentType
        :type arg1: UnityEngine.ContentType
        '''
        pass

    @staticmethod
    def get_lineType():
        '''
        :returns: InputField+LineType
        :rtype: UnityEngine.InputField+LineType
        '''
        pass

    @staticmethod
    def set_lineType(arg1):
        '''
        :param arg1: LineType
        :type arg1: UnityEngine.LineType
        '''
        pass

    @staticmethod
    def get_inputType():
        '''
        :returns: InputField+InputType
        :rtype: UnityEngine.InputField+InputType
        '''
        pass

    @staticmethod
    def set_inputType(arg1):
        '''
        :param arg1: InputType
        :type arg1: UnityEngine.InputType
        '''
        pass

    @staticmethod
    def get_touchScreenKeyboard():
        '''
        :returns: TouchScreenKeyboard
        :rtype: UnityEngine.TouchScreenKeyboard
        '''
        pass

    @staticmethod
    def get_keyboardType():
        '''
        :returns: TouchScreenKeyboardType
        :rtype: UnityEngine.TouchScreenKeyboardType
        '''
        pass

    @staticmethod
    def set_keyboardType(arg1):
        '''
        :param arg1: TouchScreenKeyboardType
        :type arg1: UnityEngine.TouchScreenKeyboardType
        '''
        pass

    @staticmethod
    def get_characterValidation():
        '''
        :returns: InputField+CharacterValidation
        :rtype: UnityEngine.InputField+CharacterValidation
        '''
        pass

    @staticmethod
    def set_characterValidation(arg1):
        '''
        :param arg1: CharacterValidation
        :type arg1: UnityEngine.CharacterValidation
        '''
        pass

    @staticmethod
    def get_readOnly():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_readOnly(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_multiLine():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_asteriskChar():
        '''
        :returns: Char
        :rtype: System.Char
        '''
        pass

    @staticmethod
    def set_asteriskChar(arg1):
        '''
        :param arg1: Char
        :type arg1: System.Char
        '''
        pass

    @staticmethod
    def get_wasCanceled():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_caretPosition():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_caretPosition(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_selectionAnchorPosition():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_selectionAnchorPosition(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_selectionFocusPosition():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_selectionFocusPosition(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def MoveTextEnd(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def MoveTextStart(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
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
    def OnDrag(arg1):
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
    def OnPointerDown(arg1):
        '''
        :param arg1: PointerEventData
        :type arg1: UnityEngine.PointerEventData
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
