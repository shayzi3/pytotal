
from core.request.request_ip import RequestIP
from core.schemas.enums import Mode
from core.schemas.schemas import GetIP



class IP(RequestIP):
     def __init__(self, api: str):
          super().__init__(api)
          
          
     async def ip_address_scane(
          self,
          ip: str,
          mode: Mode | None = None
     ) -> dict | GetIP:
          """Scane ip adderss

          Args:
              ip (str): ip address
              mode (Mode | None) = None: For output class(File) or dict. Mode.CLASS or Mode.DICT

          Returns:
              dict | GetIP
          """
          return await self._request_ip_scane(
               ip=ip,
               mode=mode
          )          
         