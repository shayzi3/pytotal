import os
import httpx



class FilesUtil:
     __slots__ = (
          '__headers'
     )
     
     def __init__(self, api: str) -> None:
          self.__headers = {
               "accept": "application/json",
               "x-apikey": api
          }
     
     
     async def _check_size(self, path: str):
          url = "https://www.virustotal.com/api/v3/files"
          
          size = (os.path.getsize(path) // (1024**2))
          if size > 650:
               raise MemoryError('Max size 650mb')
          
          if size > 32 and size < 650:
               url = await self.__get_new_url()
          return url
     
     
     async def __get_new_url(self) -> str:
          url = 'https://www.virustotal.com/api/v3/files/upload_url'
          
          async with httpx.AsyncClient() as session:
               response = await session.get(url, headers=self.__headers)
          return response.json()['data']