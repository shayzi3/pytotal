
from methods.files import Files
from methods.domains import Domains
from methods.ip import IP
from methods.urls import Url


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
     def ip(self) -> IP:
          return IP(self.__api)

     
     
     @property
     def url(self) -> Url:
          return Url(self.__api)