import json
import httpx



class Urls:
     def __init__(self, api: str) -> None:
          self.__headers = {
               "accept": "application/json",
               "x-apikey": api 
          }
          self.api = api
          
          
     async def scan_url(
          self,
          scan_url: str
     ) -> dict:
          """_summary_

          Args:
              url (str): _description_

          Returns:
              dict: _description_
          """
          url = f'https://www.virustotal.com/api/v3/urls'
          
          payload = {'url': scan_url}
          
          async with httpx.AsyncClient() as session:
               response = await session.post(url, data=payload, headers=self.__headers)

               links = response.json()['data']['links']['self']
               links_response = await session.get(links, headers=self.__headers)
          return links_response.json()
     
     
     async def get_url_analysis_report(
          self,
          id: str
     ) -> dict:
          """_summary_

          Args:
              id (str): _description_

          Returns:
              dict: _description_
          """
          url = 'https://www.virustotal.com/api/v3/urls/' + id
          
          
          async with httpx.AsyncClient() as session:
               response = await session.get(url, headers=self.__headers)
          return response.json()
     
     
     async def url_rescane(
          self,
          id: str
     ) -> dict:
          """_summary_

          Args:
              id (str): _description_

          Returns:
              dict: _description_
          """
          url = f'https://www.virustotal.com/api/v3/urls/{id}/analyse'
          
          async with httpx.AsyncClient() as session:
               response = await session.post(url, headers=self.__headers)
               
               links = response.json()['data']['links']['self']
               links_response = await session.get(links, headers=self.__headers)
          return links_response.json()