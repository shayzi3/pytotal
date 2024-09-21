
from methods.files import Files
from methods.domains import Domains



class PyTotal:
     __slots__ = (
          '__api'
     )
     def __init__(self, api: str) -> None:
          self.__api = api
     
     
     @property
     def files(self) -> Files:
          return Files(self.__api)
     
     
     @property
     def domain(self) -> Domains:
          return Domains(self.__api)
     
     
     @property
     def ip(self) -> None:
          return
     
     
     @property
     def url(self) -> None:
          return