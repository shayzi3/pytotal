
from dataclasses import dataclass



@dataclass
class GetFile:
     md5: str
     results: dict
     date: int
     size: int
     sandbox_verdict: str | None = None
     status: str | None = None
     
     
