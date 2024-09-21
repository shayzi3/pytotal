import httpx

from core.utils.schemas import GetFile
from core.utils.exception import RequestError
from core.utils.enums import Mode



class RequestFiles:
     __slots__ = (
          '__headers'
     )
     
     def __init__(self, api: str) -> None:
          self.__headers = {
               "accept": "application/json",
               "x-apikey": api 
          }      
          
     async def _request_upload_file(
          self, 
          url: str,
          files: dict, 
          mode: Mode | None = None,
          password_archive: dict | None = None
     ) -> dict | GetFile:
          async with httpx.AsyncClient() as session:
               response_post = await session.post(
                    url, 
                    files=files, 
                    headers=self.__headers, 
                    data=password_archive
               )
               if response_post.status_code != 200:
                    raise RequestError(f'failed to complete request - {response_post.text}')
               
               link = response_post.json()['data']['links']['self']
               response_get = await session.get(link, headers=self.__headers)
               
               response_json = response_get.json()    
               if mode == Mode.CLASS:
                    return GetFile(
                         status=response_json['data']['attributes']['status'],
                         date=response_json['data']['attributes']['date'],
                         md5=response_json['meta']['file_info']['md5'],
                         size=response_json['meta']['file_info']['size'],
                         results=response_json['data']['attributes']['results']
                    )
               return response_json
               
               
     async def _request_get_file_report(
          self,
          id: str,
          mode: Mode | None = None
     ) -> dict | GetFile:
          url = 'https://www.virustotal.com/api/v3/files/' + id
          
          async with httpx.AsyncClient() as session:
               response_post = await session.get(url, headers=self.__headers)
               
               if response_post.status_code != 200:
                    raise RequestError(f'failed to complete request - {response_post.text}')
               
               
          response_json = response_post.json()
          if mode == Mode.CLASS:
               return GetFile(
                    md5=id,
                    results=response_json['data']['attributes']['last_analysis_results'],
                    sandbox_verdict=response_json['data']['attributes']['sandbox_verdicts']['C2AE']['category'],
                    date=response_json['data']['attributes']['last_modification_date'],
                    size=response_json['data']['attributes']['size']
               )
          return response_json  
     
     
     
     async def _request_rescane_file(
          self,
          id: str,
          mode: Mode | None = None
     ) -> dict | GetFile:
          url = f'https://www.virustotal.com/api/v3/files/{id}/analyse'
          
          async with httpx.AsyncClient() as session:
               response = await session.post(url, headers=self.__headers)
               
               links = response.json()['data']['links']['self']
               links_response = await session.get(links, headers=self.__headers)
               
               
          response_json = links_response.json()
          if mode == Mode.CLASS:
               return GetFile(
                    md5=id,
                    date=response_json['data']['attributes']['date'],
                    size=response_json['meta']['file_info']['size'],
                    results=response_json['data']['attributes']['results'],
                    status=response_json['data']['attributes']['status']
               )
          return response_json
               
     
     
     