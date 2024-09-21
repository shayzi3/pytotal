
from core.request.request_domain import RequestDomain
from core.schemas.enums import Mode
from core.schemas.schemas import GetDomain, RescaneDomain



class Domains(RequestDomain):
     def __init__(self, api: str) -> None:
          super().__init__(api)
          
          
     async def domain_scane(
          self,
          domain_name: str,
          mode: Mode | None = None
     ) -> dict | GetDomain:
          """Check info about domain

          Args:
              domain_name (str): Domain name. example.com or example.ru or example.net
              mode (Mode | None) = None: For output class(File) or dict. Mode.CLASS or Mode.DICT

          Returns:
              dict | GetDomain
          """
          return await self._request_domain_report(
               domain_name=domain_name,
               mode=mode
          )
          
     
     async def domain_rescane(
          self,
          domain_name: str,
          mode: Mode | None = None
     ) -> dict | RescaneDomain:
          """Rescane domain

          Args:
              domain_name (str): Domain name. example.com or example.ru or example.net
              mode (Mode | None) = None: For output class(File) or dict. Mode.CLASS or Mode.DICT

          Returns:
              dict | GetDomain

          """
          return await self._request_domain_rescane(
               domain_name=domain_name,
               mode=mode
          )