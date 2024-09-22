import json
import httpx

from core.schemas.enums import Mode
from core.utils.exception import RequestError
from core.schemas.schemas import GetUrl



class RequestUrl:
     __slots__ = (
          '__headers'
     )
     
     def __init__(self, api: str) -> None:
          self.__headers = {
               "accept": "application/json",
               "x-apikey": api 
          }
           
     async def _request_scan_url(
          self,
          scan_url: str,
          mode: Mode | None = None
     ) -> dict | GetUrl:
          url = f'https://www.virustotal.com/api/v3/urls'
          
          payload = {'url': scan_url}
          async with httpx.AsyncClient() as session:
               response = await session.post(url, data=payload, headers=self.__headers)
               
               if response.status_code != 200:
                    raise RequestError(f'failed to complete request - {response.text}')

               links = response.json()['data']['links']['self']
               links_response = await session.get(links, headers=self.__headers)
               
          response_json = links_response.json()
          if mode == Mode.CLASS:
               return GetUrl(
                    stats=response_json['data']['attributes']['stats'],
                    results=response_json['data']['attributes']['results'],
                    id=response_json['meta']['url_info']['id']
               )
          return response_json
     
     
     
     async def _request_get_url_analysis(
          self,
          id: str,
          mode: Mode | None = None
     ) -> dict | GetUrl:
          url = 'https://www.virustotal.com/api/v3/urls/' + id
          
          async with httpx.AsyncClient() as session:
               response = await session.get(url, headers=self.__headers)
               
               if response.status_code != 200:
                    raise RequestError(f'failed to complete request - {response.text}')
               
          response_json = response.json()
          if mode == Mode.CLASS:
               return GetUrl(
                    results=response_json['data']['attributes']['last_analysis_results'],
                    stats=response_json['data']['attributes']['last_analysis_stats'],
                    id=id
               )
          return response_json
     
     
     
     async def _request_url_rescane(
          self,
          id: str,
          mode: Mode | None = None
     ) -> dict | GetUrl:
          url = f'https://www.virustotal.com/api/v3/urls/{id}/analyse'
          
          async with httpx.AsyncClient() as session:
               response = await session.post(url, headers=self.__headers)
               
               if response.status_code != 200:
                    raise RequestError(f'failed to complete request - {response.text}')
               
               links = response.json()['data']['links']['self']
               links_response = await session.get(links, headers=self.__headers)
               
          response_json = links_response.json()
          if mode == Mode.CLASS:
               return  GetUrl(
                    results=response_json['data']['attributes']['results'],
                    stats=response_json['data']['attributes']['stats'],
                    id=id
               )
          return response_json