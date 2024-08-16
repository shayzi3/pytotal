import httpx




class Domains:
     def __init__(self, api: str) -> None:
          self.__header = {
               "accept": "application/json",
               "x-apikey": api 
          }
          self.api = api
          
          
     async def domain_report(
          self,
          domain_name: str
     ) -> dict:
          """_summary_

          Args:
              domain_name (str): _description_

          Returns:
              dict: _description_
          """
          url = 'https://www.virustotal.com/api/v3/domains/' + domain_name
          
          async with httpx.AsyncClient() as session:
               response = await session.get(url, headers=self.__header)
          return response.text
     
     
     
     async def domain_rescane_analyze(
          self,
          domain_name: str
     ) -> dict:
          """_summary_

          Args:
              domain_name (str): _description_

          Returns:
              dict: _description_
          """
          url = f'https://www.virustotal.com/api/v3/domains/{domain_name}/analyse'
          
          
          async with httpx.AsyncClient() as session:
               response = await session.post(url, headers=self.__header)
               
               links = response.json()['data']['links']['self']
               links_response = await session.get(links, headers=self.__header)
          return links_response.text