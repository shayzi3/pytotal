import httpx




class IP:
     def __init__(self, api: str):
          self.__headers = {
               "accept": "application/json",
               "x-apikey": api 
          }
          self.api = api
          
          
     async def ip_address_report(
          self,
          ip: str
     ) -> dict:
          """_summary_

          Args:
              ip (str): _description_

          Returns:
              dict: _description_
          """
          url = 'https://www.virustotal.com/api/v3/ip_addresses/' + ip
          
          async with httpx.AsyncClient() as session:
               response = await session.get(url, headers=self.__headers)
          return response.json()