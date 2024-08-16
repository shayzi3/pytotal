import os
import httpx


class FilesUtil:
     
     async def _check_size(self, path: str, api: str):
          url = "https://www.virustotal.com/api/v3/files"
          
          size = (os.path.getsize(path) // (1024**2))
          if size > 650:
               raise MemoryError('Max size 650mb')
          
          if size > 32 and size < 650:
               url = await self.__get_new_url(api)
          return url
     
     
     
     async def __get_new_url(self, api: str) -> str:
          url = 'https://www.virustotal.com/api/v3/files/upload_url'
          
          headers = {
               "accept": "application/json",
               "x-apikey": api 
          }
          async with httpx.AsyncClient() as session:
               response = await session.get(url, headers=headers)
          return response.json()['data']