
from core.request.request_files import RequestFiles
from core.utils.files_util import FilesUtil
from core.schemas.schemas import GetFile
from core.schemas.enums import Mode





class Files(RequestFiles):
     __slots__ = (
          '__util'
     )
     
     def __init__(self, api: str) -> None:
          super().__init__(api)
          
          self.__util = FilesUtil(api)          
          
     async def upload_file(
          self,
          filepath: str,
          filename: str,
          mode: Mode | None = None,
          password_archive: str | None = None
     ) -> dict | GetFile:
          """Upload file for analysis

          Args:
              filename (str): Name file
              filepath (str): Path to file
              mode (Mode | None) = None: For output class(File) or dict. Mode.CLASS or Mode.DICT
              password (str | None) = None: For archive while protect password
              

          Returns:
              dict | GetFile
          """
          if password_archive:
               password_archive = {'password': password_archive}
          
          url = await self.__util._check_size(path=filepath)
          files = {"file": (filename, open(filepath, 'rb'))}
          
          return await self._request_upload_file(
               url=url,
               files=files,
               password_archive=password_archive,
               mode=mode
          )      
          
     
     async def get_file_report(
          self,
          id: str,
          mode: Mode | None = None
     ) -> dict | GetFile:
          """Get info about file by his id
          
          Args:
              id (str): sha-256, md5, sha1
              mode (Mode | None) = None: For output class(File) or dict. Mode.CLASS or Mode.DICT
              
          Returns:
               dict | GetFile
          """
          return await self._request_get_file_report(
               id=id,
               mode=mode
          )
          
          
     async def rescane_file(
          self,
          id: str,
          mode: Mode | None = None
     ) -> dict | GetFile:
          """Rescane file by his id

          Args:
              id (str): sha-256, md5, sha1
              mode (Mode | None) = None: For output class(File) or dict. Mode.CLASS or Mode.DICT

          Returns:
              dict | GetFile
          """
          
          return await self._request_rescane_file(
               id=id,
               mode=mode
          )
          