
from core.request.request_url import RequestUrl
from core.schemas.enums import Mode
from core.schemas.schemas import GetUrl



class Url(RequestUrl):
     def __init__(self, api: str) -> None:
          super().__init__(api)
          
          
     async def scane_url(
          self,
          scan_url: str,
          mode: Mode | None = None
     ) -> dict | GetUrl:
          """Scan url

          Args:
              scan_url (str):  https://example.com/
              mode (Mode | None) = None: For output class or dict. Mode.CLASS or Mode.DICT

          Returns:
              dict | GetUrl
          """
          return await self._request_scan_url(
               scan_url=scan_url,
               mode=mode
          )
         
     
     async def get_url_analysis(
          self,
          id: str,
          mode: Mode | None = None
     ) -> dict | GetUrl:
          """Get data url by id

          Args:
              id (str): GetUrl.id
              mode (Mode | None) = None: For output class or dict. Mode.CLASS or Mode.DICT

          Returns:
              dict | GetUrl
          """
          return await self._request_get_url_analysis(
               id=id,
               mode=mode
          )
          
          
     async def url_rescane(
          self,
          id: str,
          mode: Mode | None = None
     ) -> dict:
          """Rescane url

          Args:
              id (str): GetUrl.id
              mode (Mode | None) = None: For output class or dict. Mode.CLASS or Mode.DICT

          Returns:
              dict | GetUrl
          """
          return await self._request_url_rescane(
               id=id,
               mode=mode
          )
          