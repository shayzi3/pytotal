import httpx

from core.utils.files_util import  FilesUtil


class Files:
     def __init__(self, api: str) -> None:
          self.__headers = {
               "accept": "application/json",
               "x-apikey": api 
          }
          self.api = api
          self.util = FilesUtil()
          
          
          
     async def upload_file(
          self, 
          filename: str, 
          filepath: str, 
          password_archive: str | None = None
     ) -> dict:
          """Upload file for analysis

          Args:
              filename (str): Name file
              filebyte (bytes): open('name_file', 'rb')
              password (str | None) = None: For archive while protect password

          Returns:
              dict: dict keeping info about analysis of file
          """
          if password_archive:
               password_archive = {'password': password_archive}
               
          url = await self.util._check_size(filepath, self.api)
          
          files = {"file": (filename, open(filepath, 'rb'))}
          async with httpx.AsyncClient() as session:
               response = await session.post(
                    url, 
                    files=files, 
                    headers=self.__headers, 
                    data=password_archive
               )
               response = response.json()
               
               if 'data' in response.keys():
                    link = response['data']['links']['self']
                    link_response = await session.get(link, headers=self.__headers)
                    
                    return link_response.json()
               return response
               
               
          
          
     async def get_file_report(
          self,
          id: str
     ) -> dict:
          """Get info about file by his id
          
          Args:
              id (str): sha-256, md5, sha1
              
          Returns:
               dict: info about file
          """
          url = 'https://www.virustotal.com/api/v3/files/' + id
          
          async with httpx.AsyncClient() as session:
               response = await session.get(url, headers=self.__headers)
          return response.json()
     
     
     
     async def rescane_file(
          self,
          id: str
     ) -> dict:
          """Rescane file by his id

          Args:
              id (str): sha-256, md5, sha1

          Returns:
              dict: info about file
          """
          url = f'https://www.virustotal.com/api/v3/files/{id}/analyse'
          
          async with httpx.AsyncClient() as session:
               response = await session.post(url, headers=self.__headers)
               links = response.json()['data']['links']['self']

               links_response = await session.get(links, headers=self.__headers)
          return links_response.json()
               
     
     
     