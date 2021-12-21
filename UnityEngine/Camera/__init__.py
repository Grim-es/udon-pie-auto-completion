from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class Camera:
    def __new__(cls, arg1=None):
        '''
        :returns: Camera
        :rtype: UnityEngine.Camera
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
    def get_onPreCull():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineCameraCameraCallback
        '''
        pass

    @staticmethod
    def set_onPreCull():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineCameraCameraCallback
        '''
        pass

    @staticmethod
    def get_onPreRender():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineCameraCameraCallback
        '''
        pass

    @staticmethod
    def set_onPreRender():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineCameraCameraCallback
        '''
        pass

    @staticmethod
    def get_onPostRender():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineCameraCameraCallback
        '''
        pass

    @staticmethod
    def set_onPostRender():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineCameraCameraCallback
        '''
        pass

    @staticmethod
    def get_areVRStereoViewMatricesWithinSingleCullTolerance():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_stereoTargetEye():
        '''
        :returns: StereoTargetEyeMask
        :rtype: UnityEngine.StereoTargetEyeMask
        '''
        pass

    @staticmethod
    def set_stereoTargetEye(arg1):
        '''
        :param arg1: StereoTargetEyeMask
        :type arg1: UnityEngine.StereoTargetEyeMask
        '''
        pass

    @staticmethod
    def get_stereoActiveEye():
        '''
        :returns: Camera+MonoOrStereoscopicEye
        :rtype: UnityEngine.Camera+MonoOrStereoscopicEye
        '''
        pass

    @staticmethod
    def GetStereoNonJitteredProjectionMatrix(arg1):
        '''
        :param arg1: StereoscopicEye
        :type arg1: UnityEngine.StereoscopicEye
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def GetStereoViewMatrix(arg1):
        '''
        :param arg1: StereoscopicEye
        :type arg1: UnityEngine.StereoscopicEye
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def CopyStereoDeviceProjectionMatrixToNonJittered(arg1):
        '''
        :param arg1: StereoscopicEye
        :type arg1: UnityEngine.StereoscopicEye
        '''
        pass

    @staticmethod
    def GetStereoProjectionMatrix(arg1):
        '''
        :param arg1: StereoscopicEye
        :type arg1: UnityEngine.StereoscopicEye
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def SetStereoProjectionMatrix(arg1, arg2):
        '''
        :param arg1: StereoscopicEye
        :type arg1: UnityEngine.StereoscopicEye
        :param arg2: Matrix4x4
        :type arg2: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def ResetStereoProjectionMatrices():
        pass

    @staticmethod
    def SetStereoViewMatrix(arg1, arg2):
        '''
        :param arg1: StereoscopicEye
        :type arg1: UnityEngine.StereoscopicEye
        :param arg2: Matrix4x4
        :type arg2: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def ResetStereoViewMatrices():
        pass

    @staticmethod
    @overload
    def RenderToCubemap(arg1, arg2):
        '''
        :param arg1: Cubemap
        :type arg1: UnityEngine.Cubemap
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def RenderToCubemap(arg1):
        '''
        :param arg1: Cubemap
        :type arg1: UnityEngine.Cubemap
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def RenderToCubemap(arg1, arg2):
        '''
        :param arg1: RenderTexture
        :type arg1: UnityEngine.RenderTexture
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def RenderToCubemap(arg1):
        '''
        :param arg1: RenderTexture
        :type arg1: UnityEngine.RenderTexture
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def RenderToCubemap(arg1, arg2, arg3):
        '''
        :param arg1: RenderTexture
        :type arg1: UnityEngine.RenderTexture
        :param arg2: Int32
        :type arg2: System.Int32 or int
        :param arg3: MonoOrStereoscopicEye
        :type arg3: UnityEngine.MonoOrStereoscopicEye
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def RenderToCubemap(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def Render():
        pass

    @staticmethod
    def RenderWithShader(arg1, arg2):
        '''
        :param arg1: Shader
        :type arg1: UnityEngine.Shader
        :param arg2: String
        :type arg2: System.String or str
        '''
        pass

    @staticmethod
    def RenderDontRestore():
        pass

    @staticmethod
    def SetupCurrent(arg1):
        '''
        :param arg1: Camera
        :type arg1: UnityEngine.Camera
        '''
        pass

    @staticmethod
    def CopyFrom(arg1):
        '''
        :param arg1: Camera
        :type arg1: UnityEngine.Camera
        '''
        pass

    @staticmethod
    def set_usePhysicalProperties(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_sensorSize():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_sensorSize(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_lensShift():
        '''
        :returns: Vector2
        :rtype: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def set_lensShift(arg1):
        '''
        :param arg1: Vector2
        :type arg1: UnityEngine.Vector2
        '''
        pass

    @staticmethod
    def get_focalLength():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_focalLength(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_gateFit():
        '''
        :returns: Camera+GateFitMode
        :rtype: UnityEngine.Camera+GateFitMode
        '''
        pass

    @staticmethod
    def set_gateFit(arg1):
        '''
        :param arg1: GateFitMode
        :type arg1: UnityEngine.GateFitMode
        '''
        pass

    @staticmethod
    def get_rect():
        '''
        :returns: Rect
        :rtype: UnityEngine.Rect
        '''
        pass

    @staticmethod
    def set_rect(arg1):
        '''
        :param arg1: Rect
        :type arg1: UnityEngine.Rect
        '''
        pass

    @staticmethod
    def get_pixelRect():
        '''
        :returns: Rect
        :rtype: UnityEngine.Rect
        '''
        pass

    @staticmethod
    def set_pixelRect(arg1):
        '''
        :param arg1: Rect
        :type arg1: UnityEngine.Rect
        '''
        pass

    @staticmethod
    def get_pixelWidth():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_pixelHeight():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_scaledPixelWidth():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_scaledPixelHeight():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def get_targetTexture():
        '''
        :returns: RenderTexture
        :rtype: UnityEngine.RenderTexture
        '''
        pass

    @staticmethod
    def set_targetTexture(arg1):
        '''
        :param arg1: RenderTexture
        :type arg1: UnityEngine.RenderTexture
        '''
        pass

    @staticmethod
    def get_activeTexture():
        '''
        :returns: RenderTexture
        :rtype: UnityEngine.RenderTexture
        '''
        pass

    @staticmethod
    def get_targetDisplay():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_targetDisplay(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    @overload
    def SetTargetBuffers(arg1, arg2):
        '''
        :param arg1: RenderBuffer
        :type arg1: UnityEngine.RenderBuffer
        :param arg2: RenderBuffer
        :type arg2: UnityEngine.RenderBuffer
        '''
        pass

    @staticmethod
    @overload
    def SetTargetBuffers(arg1, arg2):
        '''
        :param arg1: RenderBufferArray
        :type arg1: UnityEngine.RenderBufferArray
        :param arg2: RenderBuffer
        :type arg2: UnityEngine.RenderBuffer
        '''
        pass

    @staticmethod
    def SetTargetBuffers(arg1=None, arg2=None):
        pass

    @staticmethod
    def get_cameraToWorldMatrix():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_worldToCameraMatrix():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def set_worldToCameraMatrix(arg1):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_projectionMatrix():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def set_projectionMatrix(arg1):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_nonJitteredProjectionMatrix():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def set_nonJitteredProjectionMatrix(arg1):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def get_useJitteredProjectionMatrixForTransparentRendering():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useJitteredProjectionMatrixForTransparentRendering(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_previousViewProjectionMatrix():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def ResetWorldToCameraMatrix():
        pass

    @staticmethod
    def ResetProjectionMatrix():
        pass

    @staticmethod
    def CalculateObliqueMatrix(arg1):
        '''
        :param arg1: Vector4
        :type arg1: UnityEngine.Vector4
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    @overload
    def WorldToScreenPoint(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: MonoOrStereoscopicEye
        :type arg2: UnityEngine.MonoOrStereoscopicEye
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def WorldToScreenPoint(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def WorldToScreenPoint(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def WorldToViewportPoint(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: MonoOrStereoscopicEye
        :type arg2: UnityEngine.MonoOrStereoscopicEye
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def WorldToViewportPoint(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def WorldToViewportPoint(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ViewportToWorldPoint(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: MonoOrStereoscopicEye
        :type arg2: UnityEngine.MonoOrStereoscopicEye
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def ViewportToWorldPoint(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def ViewportToWorldPoint(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ScreenToWorldPoint(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: MonoOrStereoscopicEye
        :type arg2: UnityEngine.MonoOrStereoscopicEye
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def ScreenToWorldPoint(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def ScreenToWorldPoint(arg1=None, arg2=None):
        pass

    @staticmethod
    def ScreenToViewportPoint(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def ViewportToScreenPoint(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    @overload
    def ViewportPointToRay(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: MonoOrStereoscopicEye
        :type arg2: UnityEngine.MonoOrStereoscopicEye
        :returns: Ray
        :rtype: UnityEngine.Ray
        '''
        pass

    @staticmethod
    @overload
    def ViewportPointToRay(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Ray
        :rtype: UnityEngine.Ray
        '''
        pass

    @staticmethod
    def ViewportPointToRay(arg1=None, arg2=None):
        pass

    @staticmethod
    @overload
    def ScreenPointToRay(arg1, arg2):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: MonoOrStereoscopicEye
        :type arg2: UnityEngine.MonoOrStereoscopicEye
        :returns: Ray
        :rtype: UnityEngine.Ray
        '''
        pass

    @staticmethod
    @overload
    def ScreenPointToRay(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :returns: Ray
        :rtype: UnityEngine.Ray
        '''
        pass

    @staticmethod
    def ScreenPointToRay(arg1=None, arg2=None):
        pass

    @staticmethod
    def CalculateFrustumCorners(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Rect
        :type arg1: UnityEngine.Rect
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: MonoOrStereoscopicEye
        :type arg3: UnityEngine.MonoOrStereoscopicEye
        :param arg4: Vector3Array
        :type arg4: UnityEngine.Vector3Array
        '''
        pass

    @staticmethod
    def CalculateProjectionMatrixFromPhysicalProperties(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        '''
        :param arg1: Undefined variable
        :type arg1: Matrix4x4Ref.Matrix4x4Ref
        :param arg2: Single
        :type arg2: System.Single or float
        :param arg3: Vector2
        :type arg3: UnityEngine.Vector2
        :param arg4: Vector2
        :type arg4: UnityEngine.Vector2
        :param arg5: Single
        :type arg5: System.Single or float
        :param arg6: Single
        :type arg6: System.Single or float
        :param arg7: GateFitParameters
        :type arg7: UnityEngine.GateFitParameters
        '''
        pass

    @staticmethod
    def FocalLengthToFOV(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def FOVToFocalLength(arg1, arg2):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        :param arg2: Single
        :type arg2: System.Single or float
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def get_stereoEnabled():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def get_stereoSeparation():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_stereoSeparation(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_stereoConvergence():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_stereoConvergence(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_nearClipPlane():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_nearClipPlane(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_farClipPlane():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_farClipPlane(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_fieldOfView():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_fieldOfView(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_renderingPath():
        '''
        :returns: RenderingPath
        :rtype: UnityEngine.RenderingPath
        '''
        pass

    @staticmethod
    def set_renderingPath(arg1):
        '''
        :param arg1: RenderingPath
        :type arg1: UnityEngine.RenderingPath
        '''
        pass

    @staticmethod
    def get_actualRenderingPath():
        '''
        :returns: RenderingPath
        :rtype: UnityEngine.RenderingPath
        '''
        pass

    @staticmethod
    def Reset():
        pass

    @staticmethod
    def get_allowHDR():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_allowHDR(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_allowMSAA():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_allowMSAA(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_allowDynamicResolution():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_allowDynamicResolution(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_forceIntoRenderTexture():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_forceIntoRenderTexture(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_orthographicSize():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_orthographicSize(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_orthographic():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_orthographic(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_opaqueSortMode():
        '''
        :returns: OpaqueSortMode
        :rtype: UnityEngine.OpaqueSortMode
        '''
        pass

    @staticmethod
    def set_opaqueSortMode(arg1):
        '''
        :param arg1: OpaqueSortMode
        :type arg1: UnityEngine.OpaqueSortMode
        '''
        pass

    @staticmethod
    def get_transparencySortMode():
        '''
        :returns: TransparencySortMode
        :rtype: UnityEngine.TransparencySortMode
        '''
        pass

    @staticmethod
    def set_transparencySortMode(arg1):
        '''
        :param arg1: TransparencySortMode
        :type arg1: UnityEngine.TransparencySortMode
        '''
        pass

    @staticmethod
    def get_transparencySortAxis():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def set_transparencySortAxis(arg1):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def ResetTransparencySortSettings():
        pass

    @staticmethod
    def get_depth():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_depth(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def get_aspect():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_aspect(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    def ResetAspect():
        pass

    @staticmethod
    def get_velocity():
        '''
        :returns: Vector3
        :rtype: UnityEngine.Vector3
        '''
        pass

    @staticmethod
    def get_cullingMask():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_cullingMask(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_eventMask():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def set_eventMask(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def get_layerCullSpherical():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_layerCullSpherical(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_cameraType():
        '''
        :returns: CameraType
        :rtype: UnityEngine.CameraType
        '''
        pass

    @staticmethod
    def set_cameraType(arg1):
        '''
        :param arg1: CameraType
        :type arg1: UnityEngine.CameraType
        '''
        pass

    @staticmethod
    def get_layerCullDistances():
        '''
        :returns: SingleArray
        :rtype: System.SingleArray
        '''
        pass

    @staticmethod
    def set_layerCullDistances(arg1):
        '''
        :param arg1: SingleArray
        :type arg1: System.SingleArray
        '''
        pass

    @staticmethod
    def get_useOcclusionCulling():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_useOcclusionCulling(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def get_cullingMatrix():
        '''
        :returns: Matrix4x4
        :rtype: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def set_cullingMatrix(arg1):
        '''
        :param arg1: Matrix4x4
        :type arg1: UnityEngine.Matrix4x4
        '''
        pass

    @staticmethod
    def ResetCullingMatrix():
        pass

    @staticmethod
    def get_backgroundColor():
        '''
        :returns: Color
        :rtype: UnityEngine.Color
        '''
        pass

    @staticmethod
    def set_backgroundColor(arg1):
        '''
        :param arg1: Color
        :type arg1: UnityEngine.Color
        '''
        pass

    @staticmethod
    def get_clearFlags():
        '''
        :returns: CameraClearFlags
        :rtype: UnityEngine.CameraClearFlags
        '''
        pass

    @staticmethod
    def set_clearFlags(arg1):
        '''
        :param arg1: CameraClearFlags
        :type arg1: UnityEngine.CameraClearFlags
        '''
        pass

    @staticmethod
    def get_depthTextureMode():
        '''
        :returns: DepthTextureMode
        :rtype: UnityEngine.DepthTextureMode
        '''
        pass

    @staticmethod
    def set_depthTextureMode(arg1):
        '''
        :param arg1: DepthTextureMode
        :type arg1: UnityEngine.DepthTextureMode
        '''
        pass

    @staticmethod
    def get_clearStencilAfterLightingPass():
        '''
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def set_clearStencilAfterLightingPass(arg1):
        '''
        :param arg1: Boolean
        :type arg1: System.Boolean or bool
        '''
        pass

    @staticmethod
    def SetReplacementShader(arg1, arg2):
        '''
        :param arg1: Shader
        :type arg1: UnityEngine.Shader
        :param arg2: String
        :type arg2: System.String or str
        '''
        pass

    @staticmethod
    def ResetReplacementShader():
        pass

    @staticmethod
    def get_usePhysicalProperties():
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
