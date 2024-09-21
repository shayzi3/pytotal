import httpx

from core.schemas.enums import Mode
from core.utils.exception import RequestError
from core.schemas.schemas import GetIP




class RequestIP:
     __slots__ = (
          '__headers'
     )
     
     def __init__(self, api: str):
          self.__headers = {
               "accept": "application/json",
               "x-apikey": api 
          }          
          
          
     async def _request_ip_scane(
          self,
          ip: str,
          mode: Mode | None = None
     ) -> dict | GetIP:
          url = 'https://www.virustotal.com/api/v3/ip_addresses/' + ip
          
          async with httpx.AsyncClient() as session:
               response = await session.get(url, headers=self.__headers)
               
               if response.status_code != 200:
                    raise RequestError(f'failed to complete request - {response.text}')
          
          response_json = response.json()
          if mode == Mode.CLASS:
               return GetIP(
                    stats=response_json['data']['attributes']['last_analysis_stats'],
                    country=response_json['data']['attributes']['country'],
                    whois=response_json['data']['attributes']['whois'],
                    as_owner=response_json['data']['attributes']['as_owner'],
                    continent=response_json['data']['attributes']['continent'],
                    results=response_json['data']['attributes']['last_analysis_results']
               )
          return response_json