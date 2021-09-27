from typing import List, Generic, TypeVar, overload
from enum import Enum

class SortContextCollection:
    pass

class FilterContextCollection:
    pass

class ILabeled:
    @property
    def Label(self) -> str:
        pass
    @Label.setter
    def Label(self, label: str) -> None:
        pass


class IElement(object):
    """ Base element interface """
    @property
    def Id(self) -> int:
        pass

    @property
    def Label(self) -> str:
        pass
    @Label.setter
    def Label(self, l: str) -> None:
        pass

    @property
    def Notes(self) -> str:
        pass
    @Notes.setter
    def Notes(self, n: str) -> None:
        pass

class IElementManager:
    @property
    def Count(self) -> int:
        pass

    def ElementIDs(self) -> List[int]:
        pass

    def Exists(self, id: int) -> bool:
        pass


class IElementInput:
    pass

class IElementResults:
    pass

class IElementsInput:
    pass

class IElementsResults:
    pass

TElementManagerType = TypeVar("TElementManagerType", IElementManager)
TElementType = TypeVar("TElementType", IElement)
TElementTypeEnum = TypeVar("TElementTypeEnum", Enum)
TUnitsType = TypeVar("TUnitsType")
TElementInputType = TypeVar("TElementInputType", IElementInput)
TElementResultsType = TypeVar("TElementResultsType", IElementResults)
TElementsInputType = TypeVar("TElementsInputType", IElementsInput)
TElementsResultsType = TypeVar("TElementsResultsType", IElementsResults)

class IElements(Generic[TElementType], IElementManager):
    def Elements(self) -> List[TElementType]:
        pass
    def SelectElements(self, sorts: SortContextCollection, filters: FilterContextCollection) -> List[TElementType]:
        pass

class IModelingElementsBase(Generic[TElementManagerType, TElementType, TElementTypeEnum], IElements[TElementType]):
    @property
    def ElementType(self) -> TElementTypeEnum:
        pass
    
    # IFieldManager

    def Create(self) -> TElementType:
        pass
    @overload
    def Element(self, id: int) -> TElementType:
        pass
    @overload
    def Element(self, label: str) -> TElementType:
        pass

    def Elements(self, label: str) -> List[TElementType]:
        pass

class IModelingElementBase(Generic[TElementManagerType, TElementType, TElementTypeEnum], IElement, ILabeled):
    @property
    def Manager(self) -> TElementManagerType:
        pass
    @property
    def ElementType(self) -> TElementTypeEnum:
        pass
    def Delete(self) -> None:
        pass

class ElementStateType(Enum):
    ALL = 0
    ACTIVE = 1
    INACTIVE = 2


class INetworkElements(IModelingElementsBase[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType,
    TElementsInputType, TElementsResultsType], IElements[TElementType], IElementManager):
    
    def Results(self) -> TElementsResultsType:
        pass
    def Input(self) -> TElementInputType:
        pass
    # IFieldManager

    def Elements(self, state: ElementStateType = ElementStateType.ALL) -> List[TElementType]:
        pass

class INetworkElement(IModelingElementBase[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType,
    TElementsInputType, TElementsResultsType], IElement, ILabeled):
    @property
    def GISIDs(self) -> str:
        pass
    @GISIDs.setter
    def GISIDs(self, gisids: str) -> None:
        pass

    @property
    def Input(self) -> TElementInputType:
        pass
    @property
    def Results(self) -> TElementResultsType:
        pass
    @property
    def Units(self) -> TUnitsType:
        pass

class IElementUnits:
    pass

