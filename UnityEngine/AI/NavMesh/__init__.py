from typing import overload

from UdonPie import System
from UdonPie import UnityEngine
from UdonPie.Undefined import *


class NavMesh:
    def __new__(cls, arg1=None):
        '''
        :returns: NavMesh
        :rtype: UnityEngine.AI.NavMesh
        '''
        pass

    @staticmethod
    def get_onPreUpdate():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineAINavMeshOnNavMeshPreUpdate
        '''
        pass

    @staticmethod
    def set_onPreUpdate():
        '''
        :returns: Undefined variable
        :rtype: UnityEngineAINavMeshOnNavMeshPreUpdate
        '''
        pass

    @staticmethod
    def get_AllAreas():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def RemoveAllNavMeshData():
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Undefined variable
        :type arg3: AINavMeshHitRef.AINavMeshHitRef
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def Raycast(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Undefined variable
        :type arg3: AINavMeshHitRef.AINavMeshHitRef
        :param arg4: NavMeshQueryFilter
        :type arg4: UnityEngine.NavMeshQueryFilter
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def Raycast(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def CalculatePath(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :param arg4: NavMeshPath
        :type arg4: UnityEngine.NavMeshPath
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def CalculatePath(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: NavMeshQueryFilter
        :type arg3: UnityEngine.NavMeshQueryFilter
        :param arg4: NavMeshPath
        :type arg4: UnityEngine.NavMeshPath
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def CalculatePath(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    @overload
    def FindClosestEdge(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Undefined variable
        :type arg2: AINavMeshHitRef.AINavMeshHitRef
        :param arg3: Int32
        :type arg3: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def FindClosestEdge(arg1, arg2, arg3):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Undefined variable
        :type arg2: AINavMeshHitRef.AINavMeshHitRef
        :param arg3: NavMeshQueryFilter
        :type arg3: UnityEngine.NavMeshQueryFilter
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def FindClosestEdge(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    @overload
    def SamplePosition(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Undefined variable
        :type arg2: AINavMeshHitRef.AINavMeshHitRef
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: Int32
        :type arg4: System.Int32 or int
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    @overload
    def SamplePosition(arg1, arg2, arg3, arg4):
        '''
        :param arg1: Vector3
        :type arg1: UnityEngine.Vector3
        :param arg2: Undefined variable
        :type arg2: AINavMeshHitRef.AINavMeshHitRef
        :param arg3: Single
        :type arg3: System.Single or float
        :param arg4: NavMeshQueryFilter
        :type arg4: UnityEngine.NavMeshQueryFilter
        :returns: Boolean
        :rtype: System.Boolean
        '''
        pass

    @staticmethod
    def SamplePosition(arg1=None, arg2=None, arg3=None, arg4=None):
        pass

    @staticmethod
    def SetAreaCost(arg1, arg2):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :param arg2: Single
        :type arg2: System.Single or float
        '''
        pass

    @staticmethod
    def GetAreaCost(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def GetAreaFromName(arg1):
        '''
        :param arg1: String
        :type arg1: System.String or str
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def CalculateTriangulation():
        '''
        :returns: NavMeshTriangulation
        :rtype: UnityEngine.NavMeshTriangulation
        '''
        pass

    @staticmethod
    def get_avoidancePredictionTime():
        '''
        :returns: Single
        :rtype: System.Single
        '''
        pass

    @staticmethod
    def set_avoidancePredictionTime(arg1):
        '''
        :param arg1: Single
        :type arg1: System.Single or float
        '''
        pass

    @staticmethod
    @overload
    def AddNavMeshData(arg1):
        '''
        :param arg1: NavMeshData
        :type arg1: UnityEngine.NavMeshData
        :returns: NavMeshDataInstance
        :rtype: UnityEngine.NavMeshDataInstance
        '''
        pass

    @staticmethod
    @overload
    def AddNavMeshData(arg1, arg2, arg3):
        '''
        :param arg1: NavMeshData
        :type arg1: UnityEngine.NavMeshData
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Quaternion
        :type arg3: UnityEngine.Quaternion
        :returns: NavMeshDataInstance
        :rtype: UnityEngine.NavMeshDataInstance
        '''
        pass

    @staticmethod
    def AddNavMeshData(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def RemoveNavMeshData(arg1):
        '''
        :param arg1: NavMeshDataInstance
        :type arg1: UnityEngine.NavMeshDataInstance
        '''
        pass

    @staticmethod
    @overload
    def AddLink(arg1):
        '''
        :param arg1: NavMeshLinkData
        :type arg1: UnityEngine.NavMeshLinkData
        :returns: NavMeshLinkInstance
        :rtype: UnityEngine.NavMeshLinkInstance
        '''
        pass

    @staticmethod
    @overload
    def AddLink(arg1, arg2, arg3):
        '''
        :param arg1: NavMeshLinkData
        :type arg1: UnityEngine.NavMeshLinkData
        :param arg2: Vector3
        :type arg2: UnityEngine.Vector3
        :param arg3: Quaternion
        :type arg3: UnityEngine.Quaternion
        :returns: NavMeshLinkInstance
        :rtype: UnityEngine.NavMeshLinkInstance
        '''
        pass

    @staticmethod
    def AddLink(arg1=None, arg2=None, arg3=None):
        pass

    @staticmethod
    def RemoveLink(arg1):
        '''
        :param arg1: NavMeshLinkInstance
        :type arg1: UnityEngine.NavMeshLinkInstance
        '''
        pass

    @staticmethod
    def CreateSettings():
        '''
        :returns: NavMeshBuildSettings
        :rtype: UnityEngine.NavMeshBuildSettings
        '''
        pass

    @staticmethod
    def RemoveSettings(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        '''
        pass

    @staticmethod
    def GetSettingsByID(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: NavMeshBuildSettings
        :rtype: UnityEngine.NavMeshBuildSettings
        '''
        pass

    @staticmethod
    def GetSettingsCount():
        '''
        :returns: Int32
        :rtype: System.Int32
        '''
        pass

    @staticmethod
    def GetSettingsByIndex(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: NavMeshBuildSettings
        :rtype: UnityEngine.NavMeshBuildSettings
        '''
        pass

    @staticmethod
    def GetSettingsNameFromID(arg1):
        '''
        :param arg1: Int32
        :type arg1: System.Int32 or int
        :returns: String
        :rtype: System.String
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
