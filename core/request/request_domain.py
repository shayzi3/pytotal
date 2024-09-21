import httpx

from core.schemas.schemas import GetDomain, RescaneDomain
from core.schemas.enums import Mode
from core.utils.exception import RequestError


class RequestDomain:
     __slots__ = (
          '__headers'
     )
     
     def __init__(self, api: str) -> None:
          self.__header = {
               "accept": "application/json",
               "x-apikey": api 
          }          
          
     async def _request_domain_report(
          self,
          domain_name: str,
          mode: Mode | None = None
     ) -> dict | GetDomain:
          url = 'https://www.virustotal.com/api/v3/domains/' + domain_name
          
          async with httpx.AsyncClient() as session:
               response = await session.get(url, headers=self.__header)
               
               if response.status_code != 200:
                    raise RequestError(f'failed to complete request - {response.text}')
               
          response_json = response.json()
          if mode == Mode.CLASS:
               return GetDomain(
                    results=response_json['data']['attributes']['last_analysis_results'],
                    creation_date=response_json['data']['attributes']['creation_date'],
                    whois=response_json['data']['attributes']['whois'],
                    analysis_stats=response_json['data']['attributes']['last_analysis_stats']
               )
          return response_json
     
     
     
     
     async def _request_domain_rescane(
          self,
          domain_name: str,
          mode: Mode | None = None
     ) -> dict | RescaneDomain:
          url = f'https://www.virustotal.com/api/v3/domains/{domain_name}/analyse'
          
          async with httpx.AsyncClient() as session:
               response = await session.post(url, headers=self.__header)
               
               if response.status_code != 200:
                    raise RequestError(f'failed to complete request - {response.text}')
               
               links = response.json()['data']['links']['self']
               links_response = await session.get(links, headers=self.__header)
               
               
          response_json = links_response.json()
          if mode == Mode.CLASS:
               return RescaneDomain(
                    results=response_json['data']['attributes']['results'],
                    date=response_json['data']['attributes']['date'],
                    stats=response_json['data']['attributes']['stats']
               )
          return response_json